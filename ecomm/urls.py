from django.urls import path
from ecomm import views

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
]