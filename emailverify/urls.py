from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.login_view, name='login'),
	path('register/', views.register_view, name='register'),
	path('emailverify/', views.email_verify, name='emailverify'),
	path('dashboard/', views.dashboard, name='dashboard')
]