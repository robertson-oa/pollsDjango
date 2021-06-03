from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields


class userform(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password')