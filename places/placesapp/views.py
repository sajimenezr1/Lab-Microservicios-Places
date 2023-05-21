from django.shortcuts import render
from .models import Place

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def placesList(request):
    if request.method == 'GET':
        queryset = Place.objects.all()
        context = list(queryset.values('id', 'name'))
        return JsonResponse(context, safe=False)

@csrf_exempt
def createPlaces(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        name = data_json['name']
        place = Place(name=name)
        place.save()
        return HttpResponse('OK')
    else:
        return render(request, 'createPlaces.html', {})