from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    data = {
        "name": "Jhon Doe",
        "age": "30"
    }
    return JsonResponse(data)
