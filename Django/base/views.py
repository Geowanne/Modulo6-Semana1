from django.shortcuts import render

def inicio(request):
    return render(request, "index.html")

def contato(request):
    return render(request, "contato.html")