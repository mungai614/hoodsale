from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin.html')

def cart(request):
    return render(request, 'cart.html')
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def order(request):
    return render(request, 'order.html')
def product(request):
    return render(request, 'product.html')
def shop(request):
    return render(request, 'shop.html')









