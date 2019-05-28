from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def post_create(request):
    return render(request, "index.html", {})

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)

def post_list(request):
    context = {
        "title":"List"
    }
    # if request.user.is_authenticated:
    #     context = {
    #         "title":"My User List"
    #     }
    # else:
    #     context = {
    #         "title":"List"
    #     }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")