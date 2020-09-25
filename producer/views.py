from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse

from producer.models import * 

def index(request):
    if request.user.is_authenticated:
        producers = Producer.objects.all()

        context = {"qq": serializers.serialize('json', list(producers), fields=('name','product_types')) }
        return render(request, 'index.html', context)
    else:
        return redirect('/login', permanent=False)