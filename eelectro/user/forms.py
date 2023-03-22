from django  import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import transaction
#from .models import User
user = get_user_model()
queryset =get_user_model().objects.all()


class userregisterform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password', 'email',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user= True
        user.save()
        return user
    
class vendorregisterform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password', 'email' )
        
    @transaction.atomic
    def save(self):
        user= super().save(commit = False)
        user.is_vendor = True
        user.save()
        return user


