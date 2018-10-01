from django.urls import path
from .views import LoginView, LogoutView, RegistrationView


app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('registration/', RegistrationView.as_view(), name='registration_url'),
]

