from django.shortcuts import get_object_or_404, render

from .models import Business, Designer, Product

# Create your views here.
def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all products, businesses, and designers."""
    products = Product.objects.order_by("designer")
    businesses = Business.objects.order_by("name")
    designers = Designer.objects.order_by("name")
    business_name = businesses[0].name

    context = {
        "products": products,
        "businesses": businesses,
        "designers": designers,
        "name": business_name,
    }

    return render(request, "retail_app/index.html", context)
