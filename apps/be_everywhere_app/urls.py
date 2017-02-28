from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage),
	url(r'^log_reg$', views.log_reg),
	url(r'^about$', views.about),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	# url(r'^admin_manage_users$', views.admin_manage_users),
	# url(r'^user_manage_events$', views.user_manage_events),
	# url(r'^admin_manage_products$', views.admin_manage_products),
	# url(r'^admin_product_sales$', views.admin_product_sales),
	# url(r'^attendees_become_an_operator$', views.attendees_become_an_operator),
	# url(r'^my_messages$', views.my_messages),
	# url(r'^view_event$', views.view_event),
	# url(r'^view_user$', views.view_user),
	# url(r'^welcome_admin$', views.welcome_admin),
	# url(r'^welcome_attendee$', views.welcome_attendee),
]
