from django.forms import ModelForm, BooleanField

from catalog.models import Product


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