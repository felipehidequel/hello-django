from django.shortcuts import render, HttpResponse

# Create your views here.

def Hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')
