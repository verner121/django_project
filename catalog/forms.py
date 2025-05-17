from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
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
    'радар',
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(ModelForm, StyleFormMixin):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name', )
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'{word} нельзя использовать для имени')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', )
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'{word} нельзя использовать для описания')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price
