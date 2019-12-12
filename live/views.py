from django.shortcuts import render

from django.http import JsonResponse
from django.core import serializers

from .models import Live


def index(request):
    return JsonResponse({'data': list(Live.objects.all().values())})


def handler404(request, exception):
    return JsonResponse(data={'code': 404, 'msg': 'http 404'})


def handler500(request):
    return JsonResponse(data={'code': 500, 'msg': 'server error'})
