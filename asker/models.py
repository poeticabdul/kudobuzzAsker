from __future__ import unicode_literals

from django.db import models

class TopicArea(models.Model):
    topic_text = models.CharField(max_length=500)
    topic_description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.topic_text

class Question(models.Model):
	topic_area = models.ForeignKey(TopicArea, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=500)
	slug = models.CharField(max_length=50)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.question_text


class Choice(models.Model):
	IS_RIGHT = (
		('NO', 'NO'),
		('YES', 'YES'),
	)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	is_right = models.CharField(max_length=3, default='NO', choices=IS_RIGHT)

	def __unicode__(self):
		return self.choice_text
