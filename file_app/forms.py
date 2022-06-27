from django import forms


class DocumentForm(forms.Form):
    document = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
