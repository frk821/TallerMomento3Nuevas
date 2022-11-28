from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request): #como parámetro la petición del cliente
    return render(request, "home.html") #en el retorno se renderiza lo que pide el cliente
                                        #en este caso es el "home.html"

def Platos(request):

    #Esta vista va a utilizar un formulario de django
    #ENTONCES DEBO CREAR UN OBJETO DE LA CLASE FormularioPlatos
    formularioPlatos = FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARION AL HTML (TEMPLATE)
    dataPlatos = {
        'formularioPlatos':formularioPlatos
    }
    return render(request, "menuPlatos.html",dataPlatos)

def Empleados(request):

    formularioEmpleados = FormularioEmpleados()
    dataEmpleados = {
        'formularioEmpleados':formularioEmpleados
    }

    return render(request, "empleados.html", dataEmpleados)
