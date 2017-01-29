import requests
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from search.forms import SearchForm


class SearchView(FormMixin, TemplateView):
    form_class = SearchForm
    template_name = 'search.html'
    success_url = reverse_lazy('search:search')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():

                api_url = 'https://' if self.request.is_secure() else 'http://'
                api_url += self.request.META.get('HTTP_HOST') + str(reverse('api:messages-for-chat'))

                self.response = requests.post(api_url, data=form.cleaned_data)

                if self.response.status_code != 200:
                    return render(request, self.template_name,
                                  context=self.get_context_data(**{'no_messages': True}))

                return render(request, self.template_name, context=self.get_response_context())
            return render(request, self.template_name,
                          context=self.get_context_data(**{'form': form}))
        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_response_context(self):
        context = {
            'messages': [
                {
                    'user': message.get('user'),
                    'text': message.get('text'),
                    'date': message.get('date'),
                }
                for message
                in self.response.json().get('messages')
                ]
        }
        return self.get_context_data(**context)
