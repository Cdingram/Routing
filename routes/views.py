import django.http
from django.shortcuts import render
import forms
import json

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        return django.http.HttpResponse(json.dumps(request.POST), "application/json")
        # create a form instance and populate it with data from the request:
        #form = forms.AddressForm(request.POST)
        # # check whether it's valid:
        # if form.is_valid():
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     render(request, "routes/routes.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.AddressForm()

    return render(request, "routes/index.html", {"form":form})

def route(request):
    if request.method == 'POST':
        print request.POST

    else:
        raise django.http.Http404