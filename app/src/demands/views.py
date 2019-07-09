from django.shortcuts import render

# Create your views here.
def demands_index(request):
    context = {
        "title": "Demands"
    }
    return render(request, "./demands/index.html", context)