from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/', views.set_cookie, name='set_cookie'),
    path('get/', views.get_cookie, name='get_cookie'),
    path('delete/', views.del_cookie, name='delete_cookie'),    # deletion will be same in signed cookies also
    path('set_signed_cookie/', views.set_signed_cookie, name='set_signed_cookie'),
    path('get_signed_cookie/', views.get_signed_cookie, name='get_signed_cookie'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path('run_method/', views.run_methods, name='run_method'),
    path('set_test_cookie/', views.set_test_cookie, name='set_test_cookie'),
    path('get_test_cookie/', views.get_test_cookie, name='get_test_cookie'),
    path('delete_test_cookie/', views.delete_test_cookie, name='delete_test_cookie'),
]