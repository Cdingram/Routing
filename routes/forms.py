from django.forms import ModelForm, Textarea
from models import Address

class AddressForm(ModelForm):


    class Meta:
        model = Address
        fields = ["street", "city", "province", "postal_code"]
        help_texts = {
            "street": ("Street"),
            "city": ("City"),
            "province": ("Province"),
            "postal_code": ("Enter six digit postal code"),
        }
        widgets = {
            'postal_code': Textarea(attrs={
                'maxlength': '6',
            }),
            'street': Textarea(attrs={
                'maxlength': '250',
            }),
            'city': Textarea(attrs={
                'maxlength': '250',
            }),
        }

