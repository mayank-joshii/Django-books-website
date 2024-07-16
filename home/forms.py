from django import forms
from home.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['book_name', 'author', 'cover', 'pdf']

class Userregistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')





