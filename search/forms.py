from django import forms


class SearchForm(forms.Form):
    chat_id = forms.IntegerField(required=True, label='Chat Id (required)')
    user_id = forms.IntegerField(required=False, label='User Id (optional)')
    date = forms.DateTimeField(required=False, widget=forms.SelectDateWidget(), label='From (optional)')

