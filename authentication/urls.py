from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from authentication import views

urlpatterns = [
    # path('', views.LoginView, name='login1'),
    # path('', LoginView, {'template_name':'auth/login.html'}, name = 'login1'),
]