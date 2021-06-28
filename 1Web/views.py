from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .forms import ContactoForm,CustomUserCreationForm, ProductoForm
from rest_framework import viewsets
import requests
from django.contrib import messages
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, response
import json
from django.contrib.auth.models import User
from .filters import ProductoFilter
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
import random
import datetime







#vista para el inicio
def home(request):
    #Vista de los ultimos productos añadidos
    ultimos = Producto.objects.all()[0:4]
    data = {
        'ultimos' : ultimos
    }
    return render(request, "index.html", data)

@login_required(login_url='login')
@permission_required('1Web.view_categoria')
def informe(request):
    return render(request, 'admin/informes.html')

@login_required(login_url='login')
@permission_required('1Web.view_categoria')
def desempeno(request):
    return render(request, 'admin/desempeno.html')

#vista para la api
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenItemView(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    serializer_class = OrdenItemSerializer



        


#vista para el contacto
def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "FORMULARIO DE CONTACTO ENVIADO"
            messages.success(request,"FORMULARIO DE CONTACTO ENVIADO")
        else:
            data["form"] = formulario
    return render(request,'contacto.html', data)



#vista para registro
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            User =  authenticate(username=formulario.cleaned_data["username"],password =formulario.cleaned_data["password1"])
            login(request, User)
            data["mensaje"] = "Usuario Registrado"
            messages.success(request, "Usuario registrado correctamente.")
            return redirect(to="home")
        data["form"] =  formulario
    return render(request, 'registration/registro.html', data)





#vista para catalogo cuerdas
def catalogoCuerdas(request):
    productos = Producto.objects.all()

    filtro = ProductoFilter(request.GET, queryset=productos)
    productos = filtro.qs

    data = {
        'productos': productos,
        'filtro': filtro
    }
    return render(request, "Catalogo/catalogoCuerdas.html",data)


#vista para catalogo uuerdas
def catalogoPercusion(request):
    productos = Producto.objects.all() # error que no influye

    filtro = ProductoFilter(request.GET, queryset=productos)
    productos = filtro.qs
    data = {
        'productos': productos,
        'filtro':filtro
    }
    return render(request, "Catalogo/catalogoPercusion.html",data)


def catalogoAmpli(request):
    productos = Producto.objects.all() # error que no influye
    filtro = ProductoFilter(request.GET, queryset=productos)
    productos = filtro.qs
    data = {
        'productos': productos,
        'filtro':filtro
    }
    return render(request, "Catalogo/catalogoAmplificadores.html",data)


def catalogoAccesorios(request):
    productos = Producto.objects.all() # error que no influye
    filtro = ProductoFilter(request.GET, queryset=productos)
    productos = filtro.qs
    data = {
        'productos': productos,
        'filtro':filtro
    }
    return render(request, "Catalogo/catalagoAccesorios.html",data)




#vista para listar
@login_required(login_url='login')
@permission_required('1Web.view_producto')
def listar_producto(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    return render(request,'GestionProductos/listar.html',{'response':response})


#vista para modificar producto
@login_required(login_url='login')
@permission_required('1Web.update_producto')
def modificar_producto(request,id):
    productos = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario
    return render(request, 'GestionProductos/modificar.html', data)



#vista para agregar producto,las fotos de los productos estan en media 
@login_required(login_url='login')
@permission_required('1Web.add_producto')
def agregar_producto(request):
    #capturo lo del formulario
    data = {
        'form' : ProductoForm()
    }
    #si el formulario esta ingresado envio un mensaje
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, 'Producto agregado correctamente')
            formulario.save()
            data["mensaje"] = "Producto Almacenado"
        else: 
            data["form"] = formulario
    return render(request,'GestionProductos/agregar.html', data)



#vista para eliminar produco
@login_required(login_url='login')
@permission_required('1Web.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")




#vista para carrito
def carro(request):
    if request.user.is_authenticated:
        usuario = request.user.usuario
        orden, created = Orden.objects.get_or_create(usuario=usuario, entregado=False)
        items = orden.ordenitem_set.all()
        itemsCarro = orden.get_items_total        
    else:
        items = []
        orden = {'get_cart_total':0, 'get_items_total':0}
        itemsCarro = orden['get_items_total'] 

    context = {'items':items, 'orden':orden, 'itemsCarro':itemsCarro}
    return render(request, "carro.html", context)



def bodega(request):
    productos = Producto.objects.all() # error que no influye
    data = {
        'productos': productos
    }
    return render(request, 'bodega/bodega.html', data)




def actualizarCarro(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Accion: ', action)
    print('Producto id', productId)
    
    user = request.user.usuario
    producto = Producto.objects.get(id=productId)
    orden, created = Orden.objects.get_or_create(usuario=user, entregado=False)
    ordenItem, created = OrdenItem.objects.get_or_create(orden=orden, producto=producto)
    if action == 'add':
        messages.success(request, 'Producto Añadido con exito')
        ordenItem.cantidad = (ordenItem.cantidad + 1)
    elif action == 'eliminar':
        messages.info(request, 'Cantidad reducida')
        ordenItem.cantidad = (ordenItem.cantidad - 1)
    ordenItem.save()
    if ordenItem.cantidad <= 0:
        ordenItem.delete()

    return JsonResponse('Producto fue añadido', safe=False)


def procesar_orden(self):
    return JsonResponse('Orden completada', safe=False)




def create(request):
    if request.user.is_authenticated:
        usuario = request.user.usuario
        orden, created = Orden.objects.get_or_create(usuario=usuario, entregado=False)   
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        amount = orden.get_cart_total
        return_url = 'http://localhost:8000/commit/'

        response = Transaction.create(buy_order, session_id, amount, return_url)
        print(response)
        context = {'response':response}
        return render(request, 'webpay/create.html', context )



def webpay_commit(request ):
    if request.POST['token_ws']:
        transaction_id = datetime.datetime.now().timestamp()
        token = request.POST['token_ws']
        response = Transaction.commit(token=token,)
        
        if request.user.is_authenticated:
            usuario = request.user.usuario
            orden = Orden.objects.get_or_create(usuario=usuario, entregado=False)
            orden.transaccion_id = transaction_id
            orden.entregado = True
            orden.save()
        else:
            print('Usuario no logeado')

        context = {'token':token,'response':response}
        return render(request, 'webpay/commit.html', context) 







@login_required(login_url='login')
@permission_required('1Web.view_orden_item')
def listar_ordenes(request):
    response = requests.get('http://127.0.0.1:8000/api/Orden%20Item/').json()
    return render(request,'Vendedor/listar-orden.html',{'response':response})

    





