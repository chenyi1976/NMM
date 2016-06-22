from django.conf.urls import url
from django.contrib import admin
from django.views.generic import UpdateView, ListView

from patato.views import *
from patato.models import *


urlpatterns = [
    url(r'^accounts/', admin.site.urls),
    url(r'^query_movie/', query_movie),
    url(r'^enable_movie/', import_movie),
    url(r'^movie_list/all', ListView.as_view(model=Movie)),
    url(r'^movie_list/$', ListView.as_view(model=Movie, queryset=Movie.objects.filter(enabled=True))),
    url(r'^movie/detail/(?P<pk>[\w-]+)',
        UpdateView.as_view(model=Movie,
                           fields=['name', 'year', 'enabled', 'original_name', 'intro', 'tags'],
                           template_name="patato/form_detail.html", success_url='/movie_list'),
        name="movie"),
    url(r'^$', ListView.as_view(model=Movie, queryset=Movie.objects.filter(enabled=True))),
]
