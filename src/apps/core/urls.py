from django.conf.urls import url
from views import IndexView, HowtoView, StoryView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^~o$', HowtoView.as_view()),
    url(r'^~s$', StoryView.as_view()),
]
