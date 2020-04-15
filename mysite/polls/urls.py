from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url

app_name = 'polls'
urlpatterns = [
path('', views.IndexView.as_view(), name='index'),
url('polls/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]
