from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def produtos(request):
    return render(request,'app/produtos.html')

def sobrenos(request):
    return render(request,'app/sobrenos.html')

def contato(request):
    return render(request,'app/contato.html')