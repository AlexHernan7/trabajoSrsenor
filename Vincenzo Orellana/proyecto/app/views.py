from django.shortcuts import render

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
    return render(request, 'app/tienda.html')