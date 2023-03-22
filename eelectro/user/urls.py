from django.contrib import admin
from django.urls import path , include
from .views import userregisterview , vendorregisterview,UserLoginView,UserLogoutView


urlpatterns = [
 path('userregister/', userregisterview.as_view(), name = 'userregister'),
 path('vendorregister/', vendorregisterview.as_view(), name = 'vendorregister'),
 path('login/', UserLoginView.as_view(), name = 'login'),
 path('logout/', UserLogoutView.as_view(), name = 'logout'),
    
]