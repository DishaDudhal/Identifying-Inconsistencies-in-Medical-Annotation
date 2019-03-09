from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns=[
url(r'^$',views.home,name='home'),
url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
url(r'^view/clusters/$', views.view_clusters, name='view_clusters'),
url(r'^Search/$', views.Search, name='Search'),
url(r'^search/word/$', views.search_by_word, name='search_by_word'),
url(r'^search/annot/$', views.search_by_annot, name='search_by_annot'),
url(r'^back/$', views.back, name='back')
]
