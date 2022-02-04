from django import forms
from .models import Book

class UploadBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# class UploadBookForm(forms.Form):
#     title = forms.CharField(max_length=32)
#     author = forms.CharField(max_length=32)
#     pages = forms.IntegerField()
#     pdf = forms.FileField()
