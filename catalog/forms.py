from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in FORBIDDEN_WORDS) :
            raise ValidationError('В имени запретное слово')
        return name


    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in FORBIDDEN_WORDS) :
            raise ValidationError('В описании запретное слово')
        return description