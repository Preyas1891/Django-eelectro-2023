from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from django.contrib.auth import login
from .forms import userregisterform , vendorregisterform
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

class userregisterview(CreateView):
    model = User
    form_class = userregisterform
    template_name = 'user/user_form.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class vendorregisterview(CreateView):
    model  = User
    form_class = vendorregisterform
    template_name = 'user/vendor_form.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_vendor:
                return '/vendor/'
            else:
                return '/user/'
            
class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'
        




