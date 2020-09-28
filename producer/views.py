from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse

from producer.models import * 

def index(request):
    if request.user.is_authenticated:
        producers = Producer.objects.all().select_related("name","product_types")

        # context = {"producer_list": serializers.serialize('json', list(producers), fields=('name','product_types')) }
        context = {"producer_list": serializers.serialize('json',producers) }
        return render(request, 'index.html', context)
    else:
        return redirect('/login', permanent=False)