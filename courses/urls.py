from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    # text_detail
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_detail, name='text'),
    # Quiz Detail
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_detail, name='quiz'),
    # Create Quiz
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name='create_quiz'),
    # Quiz Edit
    url(r'(?P<course_pk>\d+)/edit_quiz(?P<quiz_pk>\d+)/$', views.quiz_edit, name='edit_quiz'),
    #  Create Question
    url(r'(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$', views.create_question, name='create_question'),
    # Edit Question
    url(r'(?P<quiz_pk>\d+)/edit_question/(?P<question_pk>\d+)/$', views.edit_question, name='edit_question'),
    # detail
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
