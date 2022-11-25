from django import forms
from .widgets import CustomClearableFileInput
from .models import Store, BusinessType


class BusinessTypeForm(forms.ModelForm):
    """
    Form for the business type model
    """
    class Meta:
        model = BusinessType
        fields = '__all__'


class StoreForm(forms.ModelForm):
    """
    Form for the storel
    """
    class Meta:
        model = Store
        exclude = ('favourites',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        business_type = BusinessType.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in business_type]

        self.fields['business_type'].choices = friendly_names
