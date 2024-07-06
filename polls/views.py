from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import info
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.

def HomePage(request):
    if request.method == "GET":
        return render(request, 'HomePage.html')


def add(request):
    if request.method == "GET":
        return render(request, 'Add.html')
    if request.method == "POST":
        info.objects.create(
            name = request.POST['name'],
            nationality = request.POST['nationality'],
            reason = request.POST['reason'],
            year = request.POST['year']
            )
    return render(request, 'Add.html')

def search(request):
    if request.method == "GET":
        return render(request, 'search.html')
    if request.method == "POST":
        number = request.POST['year']
        if number:
            information = info.objects.filter(year__contains=number)
            return render(request, 'result.html', {'information': information})
