from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.template.loader import render_to_string
from asker.models import TopicArea, Question, Choice
import time


def index(request):
    topics = TopicArea.objects.all().order_by('-created_on')
    return render_to_response('index.html', {
        'topics': topics
    }, context_instance=RequestContext(request))


def basic_shopify(request):
	request.session['correct_counter'] = 0
	shopify_topic = TopicArea.objects.get(slug="basic-shopify")
	if request.method == 'GET':
		return render_to_response('basic_shopify.html', {
		    'shopify_topic': shopify_topic
		}, context_instance=RequestContext(request))
	else:
		start_time = time.time()
		request.session['start_time'] = start_time
		return redirect('/basic-shopify/1/')
		

def next_question(request, question_id):
	if request.method == 'GET':
		
		try:
			question = Question.objects.get(slug=question_id)
		except Question.DoesNotExist:
			question = None

		if question is not None:
			choices = Choice.objects.filter(question=question)
			return render_to_response('next_question.html', {
			    'question': question,
			    'choices': choices,
			    'next_url':  str(int(question.slug) + 1)
			}, context_instance=RequestContext(request))
		else:
			return redirect('/asker/end/')

	else:
		try:
			question = Question.objects.get(slug=question_id)
		except Question.DoesNotExist:
			question = None

		if question is not None:

			answer = request.POST.get("answer", "")
			redirect_url = '/basic-shopify/' + str(question.slug) + '/'
			if answer == 'YES':
				new_counter = request.session['correct_counter']
				new_counter += 1
				request.session['correct_counter'] = new_counter
				print request.session['correct_counter']
				print "Yaaayyiii, it was right"
				return redirect(redirect_url)
			else:
				print request.session['correct_counter']
				print "the person got it wrong"
				return redirect(redirect_url)
		else:
			answer = request.POST.get("answer", "")

			end_time = time.time()
			elapsed_time = end_time - request.session['start_time']
			request.session['elapsed_time'] = int(elapsed_time)
			print "***********"
			print elapsed_time
			if answer == 'YES':
				new_counter = request.session['correct_counter']
				new_counter += 1
				request.session['correct_counter'] = new_counter
				return redirect('/asker/end/')
			else:
				return redirect('/asker/end/')





# def index_copy(request):
# 	question = Question.objects.first()
# 	request.session['correct_counter'] = 0
# 	print request.session['correct_counter']
# 	if request.method == 'GET':	
# 		choices = Choice.objects.filter(question=question)
# 		return render_to_response('index.html', {
# 		    'question': question,
# 		    'choices': choices
# 		}, context_instance=RequestContext(request))
# 	else:
# 		start_time = time.time()
# 		request.session['start_time'] = start_time
# 		answer = request.POST.get("answer", "")
# 		redirect_url = '/asker/' + str(question.pk+1) + '/'
# 		if answer == 'YES':
# 			# new_correct_counter = request.session['correct_counter']
# 			# new_correct_counter += 1
# 			# request.session['correct_counter'] = new_correct_counter
# 			request.session['correct_counter'] += 1
# 			print request.session['correct_counter']
# 			print "that was right"
# 			return redirect(redirect_url)
# 		else:
# 			print "that was wrong"
# 			return redirect(redirect_url)


# def next_question2(request, question_id):
# 	if request.method == 'GET':
# 		try:
# 			question = Question.objects.get(pk=question_id)
# 		except Question.DoesNotExist:
# 			question = None

# 		if question is not None:
# 			choices = Choice.objects.filter(question=question)
# 			return render_to_response('next_question.html', {
# 			    'question': question,
# 			    'choices': choices,
# 			    'next_url':  str(question.pk + 1)
# 			}, context_instance=RequestContext(request))
# 		else:
# 			# return render(request, 'end.html')
# 			return redirect('/asker/end/')
# 	else:

# 		try:
# 			question = Question.objects.get(pk=question_id)
# 		except Question.DoesNotExist:
# 			question = None

# 		if question is not None:

# 			answer = request.POST.get("answer", "")
# 			redirect_url = '/asker/' + str(question.pk) + '/'
# 			if answer == 'YES':
# 				new_counter = request.session['correct_counter']
# 				new_counter += 1
# 				request.session['correct_counter'] = new_counter
# 				print request.session['correct_counter']
# 				print "Yaaayyiii, it was right"
# 				return redirect(redirect_url)
# 			else:
# 				print "the person got it wrong"
# 				return redirect(redirect_url)
# 		else:
# 			answer = request.POST.get("answer", "")

# 			end_time = time.time()
# 			elapsed_time = end_time - request.session['start_time']
# 			request.session['elapsed_time'] = int(elapsed_time)
# 			print "***********"
# 			print elapsed_time
# 			if answer == 'YES':
# 				new_counter = request.session['correct_counter']
# 				new_counter += 1
# 				request.session['correct_counter'] = new_counter
# 				return redirect('/asker/end/')
# 			else:
# 				return redirect('/asker/end/')


def end(request):
	print "-----------------------------"
	print request.session['correct_counter']
	total_score = request.session['correct_counter']
	elapsed_time = request.session['elapsed_time']
	no_of_questions = Question.objects.all().count()

	if total_score >= 7 and elapsed_time <= 50:
		deserves_reward = True
	else:
		deserves_reward = False

	print deserves_reward

	return render_to_response('end.html', {
		    'total_score': total_score,
		    'no_of_questions': no_of_questions,
		    'elapsed_time': elapsed_time,
		    'deserves_reward': deserves_reward
		}, context_instance=RequestContext(request))


def reward(request):

	if request.method == 'GET':

		print ""
	else:
		kudobuzz_customers = ['alaya-lee-boutique.myshopify.com', 'zoomy-leisure.myshopify.com', 'be-clean.myshopify.com', 'st-augustine-lions.myshopify.com', 'bombshell-sportswear.myshopify.com']

		shopify_url = request.POST.get("shopify_url", "")

		if shopify_url in kudobuzz_customers:
			is_kudobuzz_customer = True
		else:
			is_kudobuzz_customer = False

		return render_to_response('reward.html', {
		    'is_kudobuzz_customer': is_kudobuzz_customer
		}, context_instance=RequestContext(request))
