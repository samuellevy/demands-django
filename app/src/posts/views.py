from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def post_create(request):
    # return HttpResponse("<h1>"+os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"</h1>")
    return render(request, "index.html", {})

def post_detail(request):
    return HttpResponse("<h1>post_detail</h1>")

def post_list(request):
    return render(request, "index.html", {})

def post_update(request):
    return HttpResponse("<h1>post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")