from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^end/$', views.end, name='end'),
    url(r'^reward/$', views.reward, name='reward'),
    url(r'^(?P<question_id>[0-9]+)/$', views.next_question, name='next_question'),
]