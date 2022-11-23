from django import forms
from .models import Store, BusinessType


class StoreForm(forms.ModelForm):
    """
    Form for the store
    """
    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        business_type = BusinessType.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in business_type]

        self.fields['business_type'].choices = friendly_names
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'
