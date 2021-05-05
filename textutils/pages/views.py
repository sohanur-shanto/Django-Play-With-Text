from django.http import HttpResponse
from django.shortcuts import render


def funwithmath(request):
    return render (request, 'funwithmath.html')