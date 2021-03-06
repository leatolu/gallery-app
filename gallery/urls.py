from django.conf.urls import url
from . import views


app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<gallery_title>\w+)/$', views.gallery, name='gallery')
]
