from django.contrib import admin

from asker.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
	search_fields = ['question_text']
	list_display = ('question_text',)

class ChoiceAdmin(admin.ModelAdmin):
	search_fields = ['choice_text']
	list_display = ('question', 'choice_text', 'is_right',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
