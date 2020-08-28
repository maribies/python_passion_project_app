from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for the retail app, Find and Seek"""

    return render(request, "retail_app/index.html")
