# -*- encoding: utf-8 -*-

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(
    login_view,
    register_user,
    home_view,
    logout_view,
    account_setting_view, 
    # MyPasswordChangeView,
    # MyPasswordResetDoneView
)     
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', logout_view, name='logout'),
    path("", home_view, name="home"),
    path("account_setting/<user_id>/", account_setting_view, name="account_setting"),

    # PASSWORD MANAGEMENT
    # path("password_change/", MyPasswordChangeView.as_view(), name="password_change"),
    # path("password_change_done/", MyPasswordResetDoneView.as_view(), name="password_change_done"),
    
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
