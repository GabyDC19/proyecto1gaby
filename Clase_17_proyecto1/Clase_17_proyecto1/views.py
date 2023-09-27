from datetime import datetime as dt
from django.http import HttpResponse
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context
from django.template import loader

def probando_template(request):

    nom = "Gabriela"
    ape = "De Carlos"
   
    diccionario = {
        "nombre": nom,
        "apellido": ape,
        "notas": [7,8,9,7,4]}
    
    #El profe lo hizo de otra manera, no puso las variables al principio:

    #diccionario = {
       #"nombre": "nombre",
       #"apellido": "apellido",
       #"notas": [7,8,9,7,4]}

    # Abrimos el archivo html
    mi_html = open('./Plantillas/templates.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)


def usando_loader(request):

    diccionario = {
        "nombre": "Gabriela",
        "apellido": "DeCarlos",
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('templates.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def Saludo(request):
    return HttpResponse ("Hola Django_Coder")

#def Gaby(request, nombre):
    #hoy=dt.now()
    #return HttpResponse (f"Hola {nombre}!, hoy es :{hoy}")

def hoy(request):
    dia=dt.now()
    docu_texto=f"Hoy es: <br> {dia}"
    return HttpResponse (docu_texto)

def mi_nombre(request, nombre):
    docu_texto= f"Mi nombre es:<br><br> {nombre}"
    return HttpResponse (docu_texto)

