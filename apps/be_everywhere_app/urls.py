from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^about$', views.about),
	url(r'^admin_manage_events$', views.admin_manage_events),
	url(r'^admin_manage_my_account$', views.admin_manage_my_account),
	url(r'^admin_manage_products$', views.admin_manage_products),
	url(r'^admin_manage_users$', views.admin_manage_users),
	url(r'^admin_product_sales$', views.admin_product_sales),
	url(r'^attendees_manage_my_account$', views.attendees_manage_my_account),
	url(r'^attendees_become_an_operator$', views.attendees_become_an_operator),
	url(r'^attendees_manage_events$', views.attendees_manage_events),
	url(r'^$', views.homepage),
	url(r'^log_reg$', views.log_reg),
	url(r'^my_messages$', views.my_messages),
	url(r'^shopping_cart$', views.shopping_cart),
	url(r'^view_event$', views.view_event),
	url(r'^view_product$', views.view_product),
	url(r'^view_user$', views.view_user),
	url(r'^welcome_admin$', views.welcome_admin),
	url(r'^welcome_attendee$', views.welcome_attendee),
#  all above url's are page render routes and urls

	url(r'^login$', views.login),
<<<<<<< HEAD
	url(r'^register$', views.register),
=======
<<<<<<< HEAD
=======
	url(r'^admin_manage_events$', views.admin_manage_events),
	# url(r'^admin_manage_users$', views.admin_manage_users),
	url(r'^user_manage_events$', views.user_manage_events),
	# url(r'^admin_manage_products$', views.admin_manage_products),
	# url(r'^admin_product_sales$', views.admin_product_sales),
	# url(r'^attendees_become_an_operator$', views.attendees_become_an_operator),
	# url(r'^my_messages$', views.my_messages),
	# url(r'^view_event$', views.view_event),
	# url(r'^view_user$', views.view_user),
	url(r'^welcome_admin$', views.welcome_admin),
	# url(r'^welcome_attendee$', views.welcome_attendee),
	# url(r'^create_event$'. views.create_event),
>>>>>>> 50c4834b05f7390ae149a48ad4484e4fbe71deb1
>>>>>>> a2f413581dc0f771eff440e005bef4a394aedc0b
]
