from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms


def hello_world(request):
    return render(request, 'home.html')


def Suggestion_view(request):
    form = forms.SuggesstionForm()
    if request.method == 'POST':
        form = forms.SuggesstionForm(request.POST)
        if form.is_valid():
            send_mail(
                'suggestion from {}'.format(form.cleaned_data['name']), #subject
                form.cleaned_data['suggestion'],
                '{name} <email>'.format(**form.cleaned_data),
                ['mody5060@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'thanks for your suggestion')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})
