from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

from .forms import SubscriberForm

def subscriber_new(request,template='subscribers/subscriber_new.html'):
	form=SubscriberForm(request.POST)
	if form.is_valid():
		# Unpack form values
		username=form.cleaned_data['username']
		password=form.cleaned_data['password1']
		email=form.cleaned_data['email']

		# Create the User record

		user=User(username=username,email=email)
		user.set_password(password)
		user.save()

		return HttpResponseRedirect('/success/')
	else:
		form=SubscriberForm()
	return render(request,template,{'form':form})


