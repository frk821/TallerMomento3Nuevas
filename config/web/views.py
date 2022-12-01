from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request): #como parámetro la petición del cliente
    return render(request, "home.html") #en el retorno se renderiza lo que pide el cliente
                                        #en este caso es el "home.html"

def PlatosVista(request):

    #Rutina para consulta de platos
    platosConsultados = Platos.objects.all()

    #Esta vista va a utilizar un formulario de django
    #ENTONCES DEBO CREAR UN OBJETO DE LA CLASE FormularioPlatos
    formularioPlatos = FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARION AL HTML (TEMPLATE)
    dataPlatos = {
        'formularioPlatos':formularioPlatos,
        'bandera':False
    }

    #-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    #RECIBIENDO LOS DATOS DEL FORMULARIO
    if request.method == 'POST': #si la peticion es de tipo 'POST'
        datosFormulario = FormularioPlatos(request.POST) #guardar todos los datos en 'datosFormulario'
        if datosFormulario.is_valid():  #si los datos ingresados en el formulario son válidos
            datosLimpios = datosFormulario.cleaned_data #limpie los datos y guardelos en 'datosLimpios'
            print(datosLimpios)
            #Construir un diccionario (objeto) de envio de datos hacia la BD
            platoNuevo = Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )

            #Intentando llevar mis datos a la BD
            try:
                platoNuevo.save()
                dataPlatos["bandera"]=True
                print("éxito guardando...")
            except Exception as error:
                print("error al intentar guardar... ",error)
                dataPlatos["bandera"]=False

    #-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.        
    return render(request, "menuPlatos.html",dataPlatos)

def EmpleadosVista(request):

    #Rutina para consulta de empleados
    empleadosConsultados = Empleados.objects.all()

    formularioEmpleados = FormularioEmpleados()

    dataEmpleados = {
        'formularioEmpleados':formularioEmpleados,
        'bandera':False
    }

    #-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    #RECIBIENDO LOS DATOS DEL FORMULARIO
    if request.method == 'POST': #si la peticion es de tipo 'POST'
        datosFormulario = FormularioEmpleados(request.POST) #guardar todos los datos en 'datosFormulario'
        if datosFormulario.is_valid():  #si los datos ingresados en el formulario son válidos
            datosLimpios = datosFormulario.cleaned_data #limpie los datos y guardelos en 'datosLimpios'
            print(datosLimpios)

            #Construir un diccionario (objeto) de envio de datos hacia la BD
            empleadoNuevo = Empleados(
                nombre=datosLimpios["nombre"],
                apellido=datosLimpios["apellido"],
                foto=datosLimpios["foto"],
                cargo=datosLimpios["cargo"],
                salario=datosLimpios["salario"],
                contacto=datosLimpios["contacto"]
            )

            #Intentando llevar mis datos a la BD
            try:
                empleadoNuevo.save()
                dataEmpleados["bandera"]=True
                print("éxito guardando...")
            except Exception as error:
                print("error al intentar guardar... ",error)
                dataEmpleados["bandera"]=False

    #-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. 

    return render(request, "empleados.html", dataEmpleados)

def PlatosRegistrados(request):
     #Rutina para consulta de platos
    platosConsultados = Platos.objects.all()

    dataPlatosRegistrados = {
        'platos':platosConsultados
    }
    return render(request,"platosRegistrados.html",dataPlatosRegistrados)

def EmpleadosRegistrados(request):
    #Rutina para consulta de empleados
    empleadosConsultados = Empleados.objects.all()

    dataEmpleadosRegistrados = {
        'empleados':empleadosConsultados #consulta de empleados registrados
    }
    return render(request,"empleadosRegistrados.html",dataEmpleadosRegistrados)
