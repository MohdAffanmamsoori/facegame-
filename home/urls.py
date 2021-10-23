# Bismillah Hir Rehman Nir Rahim


from os import name
from django.contrib.auth import logout
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this


urlpatterns=[
    path('',views.index,name='index'),
    path('signupuser/',views.signupuser,name='signup'),
    # path('signup',views.createsignupuser,name='signupcreate'),
    path('contact.html',views.contact,name='Contact'),
    path('loginuser.html',views.loginuser,name='loginuser'),
    path('logoutuser',views.logoutuser,name='logout'),
    path('maindashboard',views.maindashboard,name='maindashboard'),
    path('userearning',views.userearn,name='userearning'),
    path('bank_details',views.add_bank,name='AddBankdetails'),
    path('subscribe/pay',views.Subsuser,name='SubstoPost'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset_password/',auth_views.PasswordResetView.as_view()),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view()),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view()),
    
    # path('user_profile',views.UserDetailsView,name='userdetails'),

    # path('articles_create',views.article_create,name='articles')



    # now need to add others url and add a smtp gmail server backend to processed email and saved the error of connection refused
    
]

