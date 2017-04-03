from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 1. Metodo para mostrar todo lo que tenemos en la basa de datos
# 2. Metodo para mostrar lo que nos pidan si lo tenemos en la base de datos
# 3. Metodo para guardar paginas

def showAll(request):
    lista = Pages.objects.all()
    respuesta = "<h2>BASE DE DATOS</h2>"
    idAux = 1
    #lo imprimimos con forma de lista con <li>
    if len(lista) != 0:
        lista_pags = Pages.objects.all()
        for pag in lista_pags:
            respuesta+="<h4><li>Id: " + str(idAux) + " | " + pag.name + " : " + pag.page + "</li></h4>"
            idAux += 1
    else :
        respuesta = "La base de datos esta vacia."
    return HttpResponse(respuesta)

@csrf_exempt
def processRequest(request,name):
    if request.method == "GET":
        try:
            page = Pages.objects.get(name=name)
            respuesta = "Has elegido " + page.name + ". Su pagina es: " + page.page + ". Su id es: " + str(page.id)
        except Pages.DoesNotExist:
            respuesta = "No existe pagina con el nombre " + name + ". Creala a continuacion."
            respuesta += '<form action="" method="POST">'
            respuesta += 'Nombre: <input type="text" name="nombre">'
            respuesta += '<br>Pagina: <input type="text" name="pagina">'
            respuesta += '<input type="submit" value="Enviar"></form>'
    elif request.method == "PUT":
        try:
            pagina = Pages.objects.get(name=name)
            respuesta = "Ya existe una pagina con ese nombre"
        except Pages.DoesNotExist:
            body = request.body.split(',');
            #print(pagina[0])
            pagina = Pages(name=body[0], page=body[1])
            pagina.save()
            respuesta = "Se ha guardado la pagina: " + name \
                        + ". Se ha guardado con identificador " + str(pagina.id)
    elif request.method == "POST":
        nombre = request.POST['nombre']
        pagina = request.POST['pagina']
        pagina = Pages(name=nombre, page=pagina)
        pagina.save()
        respuesta = "Se ha guardado la pagina: " + nombre \
                    + ". Se ha guardado con identificador " + str(pagina.id)
    else :
        respuesta = "Method not Allowed"

    return HttpResponse(respuesta)
