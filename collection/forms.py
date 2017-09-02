from django.forms import ModelForm

from collection.models import Resources

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = ('name', 'description', 'url')
        