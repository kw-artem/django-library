from django.forms import Form, ModelForm
from .models import Author

#class AddNewAuthorForm(forms.Form):
#
#    first_name = forms.CharField()
#    last_name = forms.CharField()
#    date_of_birth = forms.DateField()
#    date_of_death = forms.DateField()

class AddNewAuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']