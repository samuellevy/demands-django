from django.shortcuts import render

# Create your views here.
def demands_index(request):
    context = {
        "page": "Demands",
        "subpage": "Retrieving all"
    }
    return render(request, "./demands/index.html", context)

def demands_create(request):
    context = {
        "page": "Demands",
        "subpage": "Creating"
    }
    return render(request, "./demands/create.html", context)