from django import forms

class Status_Form(forms.Form):
    status_attrs = {
        'type': 'text',
        'rows': 4,
        'class' : 'form-control',
        'placeholder':"What's happening?",
        'style' : 'resize:none'
    }

    status = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=status_attrs))
