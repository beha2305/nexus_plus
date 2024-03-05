from django import forms
from .models import Product
from django_summernote.widgets import SummernoteWidget


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'city', 'category', 'state', 'discount', 'address']
        widgets = {
            "title" : forms.TextInput(attrs= {
                "class": "form-control input-md", "placeholder": "Title"
            }),
            "category" : forms.Select(attrs= {
                "class" : "tg-select form-control"
            }),
            "price": forms.TextInput(attrs={
                "class" : "form-control input-md", "placeholder": "Ad your Price"
            }),
            "city" : forms.Select(attrs= {
                "class": "tg-select form-control"
            }),
            "address" : forms.TextInput(attrs= {
                "class": "form-control input-md"
            }),
            "discount": forms.TextInput(attrs={
                "class": "form-control input-md", "placeholder": "Ad your Price"
            }),
            "state": forms.Select(attrs={
                "class": "tg-select form-control"
            }),
            "description" : SummernoteWidget()
        }
