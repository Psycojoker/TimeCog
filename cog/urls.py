from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^question/(?P<uuid>.+)/$', views.email_question, name='email_question'),
)
