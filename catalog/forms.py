from django import forms
from .models import Author, Book, Genre

#class AddNewAuthorForm(forms.Form):
#
#    first_name = forms.CharField()
#    last_name = forms.CharField()
#    date_of_birth = forms.DateField()
#    date_of_death = forms.DateField()

class AddNewAuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AddNewBookForm(forms.Form):

    title = forms.CharField(max_length=200)
    authors = forms.ModelMultipleChoiceField(Author.objects.all())
    summary = forms.CharField(widget=forms.Textarea)
    isbn = forms.CharField(max_length=13)
    genres = forms.ModelMultipleChoiceField(Genre.objects.all())
