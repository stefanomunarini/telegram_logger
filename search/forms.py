from django import forms


class SearchForm(forms.Form):
    chat_id = forms.IntegerField(required=True)
    user_id = forms.IntegerField(required=False)
