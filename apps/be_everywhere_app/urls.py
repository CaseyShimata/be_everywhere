from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage),
	url(r'^log_reg$', views.log_reg),
	url(r'^about$', views.about),
	url(r'^register$', views.register),
]
