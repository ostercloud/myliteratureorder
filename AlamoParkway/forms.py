from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from .models import *


class SpecialOrderForm(forms.ModelForm):
    order_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}))
    received_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}), required=False)
    fulfilled_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}), required=False)


    class Meta:
        # Set this form to use the User model.
        model = SpecialOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date", "received_date", "fulfilled_date")


class CreateSpecialOrderForm(forms.ModelForm):
    order_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    class Meta:
        # Set this form to use the User model.
        model = SpecialOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date",)


class BulkOrderForm(forms.ModelForm):
    order_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}))
    received_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}), required=False)
    fulfilled_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}), required=False)
    class Meta:
        # Set this form to use the User model.
        model = BulkOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date", "received_date", "fulfilled_date")


class CreateBulkOrderForm(forms.ModelForm):
    order_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    class Meta:
        # Set this form to use the User model.
        model = BulkOrder

        # Constrain the UserForm to just these fields.
        fields = ("ordered_by", "item", "quantity", "order_date",)