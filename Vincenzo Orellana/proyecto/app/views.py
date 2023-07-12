from django.shortcuts import render, redirect
from .models import Producto
from app.Carrito import Carrito

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def api(request):
    return render(request, 'app/api.html')

def form(request):
    return render(request, 'app/form.html')

def mision(request):
    return render(request, 'app/mision.html')

def noticias(request):
    return render(request, 'app/noticias.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'app/tienda.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")