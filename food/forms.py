from django import forms

from food.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "item_name",
            "item_price",
            "item_description",
            "item_image"
        ]