import django.http
from django.shortcuts import render
import forms
import json
import googlemaps
import utils

def index(request):
    form = forms.AddressForm()

    return render(request, "routes/index.html", {"form":form})

def geocode_ajax(request):
    # if the query is empty, return nothing
    query = request.GET.get('address', '')
    if query in [None, '']:
        return django.http.HttpResponse(json.dumps({}), "application/json")

    # initialize google maps client
    gmaps = googlemaps.Client(key=utils.get_google_api_key())

    # geocode the query (region set to CANADA)
    geocode_result = gmaps.geocode(query, region='CA')

    # reutrn the json
    return django.http.HttpResponse(json.dumps(geocode_result), "application/json")

def route(request):
    if request.method == 'POST':
        print request.POST

    else:
        raise django.http.Http404