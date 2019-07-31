from django import forms


class AddForm(forms.Form):
    name = forms.CharField(
        label='name',
        max_length=200,
        required=True,
    )

    phone = forms.IntegerField(
        label='phone',
        required=True,
    )

    home = forms.CharField(
        label='home',
        max_length=200,
        required=True,
    )

    address = forms.CharField(
        label='address',
        max_length=200,
        required=True,
    )
