from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse("<h3>" + str(num1) + "+" + str(num2) + "=" + str(resultado) + "</h3>")

def resta(request, num1, num2):
    resultado = int(num1) - int(num2)
    return HttpResponse(str(num1) + "-" + str(num2) + "=" + str(resultado))

def multiplicacion(request, num1, num2):
    resultado = int(num1) * int(num2)
    return HttpResponse(str(num1) + "*" + str(num2) + "=" + str(resultado))

def division(request, num1, num2):
    resultado = float(num1) / float(num2)
    return HttpResponse(str(num1) + "/" + str(num2) + "=" + str(resultado))

def error(request):
    return HttpResponse("<h3>Ha ocurrido un error. Debe realizar sumas, restas, " + \
                        "divisiones y multiplicaciones. La forma es " + \
                        "'localhost:puerto/num1(operador)num2'.</h3>")
