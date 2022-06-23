from django import forms


class DocumentForm(forms.Form):
    filename = forms.CharField(label='File Name', max_length=100)
    document = forms.FileField()
