from django.conf.urls import patterns, include, url
from track import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Git_Issue_Tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.result, name='result'),
)