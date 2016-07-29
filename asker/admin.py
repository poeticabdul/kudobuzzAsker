from django.contrib import admin

from asker.models import TopicArea, Question, Choice

class TopicAreaAdmin(admin.ModelAdmin):
	search_fields = ['topic_text']
	list_display = ('topic_text', )

class QuestionAdmin(admin.ModelAdmin):
	search_fields = ['question_text']
	list_display = ('question_text',)

class ChoiceAdmin(admin.ModelAdmin):
	search_fields = ['choice_text']
	list_display = ('question', 'choice_text', 'is_right',)

admin.site.register(TopicArea, TopicAreaAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
