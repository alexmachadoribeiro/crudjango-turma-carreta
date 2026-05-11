from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, "index.html", {"usuarios":usuarios})

def form(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        genero = request.POST.get('genero')
        Usuario.objects.create(nome=nome, cpf=cpf, email=email, genero=genero)
        return redirect('index')
    return render(request, 'form.html')