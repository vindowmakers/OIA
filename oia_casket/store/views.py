from django.shortcuts import render
from .models import Casket, Order, OrderItem
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    featured = Casket.objects.filter(is_featured=True)
    return render(request, 'store/home.html', {'featured': featured})

def catalog(request):
    caskets = Casket.objects.all()
    return render(request, 'store/catalog.html', {'caskets': caskets})

def add_to_cart(request, casket_id):
    cart = request.session.get("cart", {})
    cart[str(casket_id)] = cart.get(str(casket_id), 0) + 1
    request.session["cart"] = cart
    return HttpResponseRedirect(reverse('catalog'))

def cart_view(request):
    cart = request.session.get("cart", {})
    caskets = Casket.objects.filter(id__in=cart.keys())
    items = [{"casket": c, "qty": cart[str(c.id)]} for c in caskets]
    total = sum(c.price * cart[str(c.id)] for c in caskets)
    return render(request, 'store/cart.html', {"items": items, "total": total})

def checkout(request):
    cart = request.session.get("cart", {})
    caskets = Casket.objects.filter(id__in=cart.keys())
    if request.method == "POST":
        order = Order.objects.create(
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            address=request.POST["address"]
        )
        for c in caskets:
            OrderItem.objects.create(order=order, casket=c, quantity=cart[str(c.id)])
        request.session["cart"] = {}
        return render(request, "store/thank_you.html")
    return render(request, "store/checkout.html")
