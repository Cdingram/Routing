from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^routes/$', views.route, name="route"),
    url(r'^geocode_ajax/$', views.geocode_ajax, name="geocode"),
]