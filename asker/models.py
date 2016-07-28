from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
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
