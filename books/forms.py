from django import forms 
from books.models import BookStoreModel

class bookStoreForm(forms.ModelForm):
    
    class Meta:
        model = BookStoreModel
        fields = ['id','book_name','author','category']
        