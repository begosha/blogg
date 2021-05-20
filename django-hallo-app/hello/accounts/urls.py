from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import register_view, UserDetailView, UserUpdateView, UserChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', UserUpdateView.as_view(), name='user-update-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
]
