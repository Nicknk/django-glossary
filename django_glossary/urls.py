from django.conf.urls import re_path
from .views import TermDetailView, TermListView


app_name = 'django_glossary'
urlpatterns = [
    re_path(r'^$', TermListView.as_view(), name='term-list'),
    re_path(r'^(?P<slug>[-\w]+)/$', TermDetailView.as_view(), name='term-detail'),
]
