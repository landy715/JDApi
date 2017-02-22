
from django.conf.urls import url
from Japi import views
urlpatterns = [
	url(r'^jcut$', views.jcut),
	url(r'^jpos$', views.jpos),
]
