from django import urls
from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('categoria', CategoriaViewSet)
router.register('Ordenes', OrdenViewSet)
router.register('Orden Item', OrdenItemView)


urlpatterns = [
    path('', home, name="home"),
    path('carro/', carro, name="carro"),
    path('contacto', contacto, name="contacto"),
    
    #Catalago
    path('catalogoCuerdas', catalogoCuerdas, name="catalogoCuerdas"),
    path('catalogoPercusion', catalogoPercusion, name="catalogoPercusion"),
    path('catalagoAccesorios', catalogoAccesorios, name="catalagoAccesorios"),
    path('catalagoAmplificadores',catalogoAmpli, name="catalagoAmplificadores"),
    #End of Catalago
    
    #Registro / Login
    path('registro/', registro ,name="registro"),
    #End of Registro

    #API para consultar los productos
    path('api/', include(router.urls)),
    path('silk/', include('silk.urls')),


    path('actualizar_carro/', actualizarCarro, name="actualizar"),
    path('procesar_orden/', procesar_orden, name="orden"),
    path('bodega/', bodega, name="bodega"),


    #vista-admin
    path('informe/', informe, name="informes"),
    path('desempeño/', desempeno, name="tienda"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/',modificar_producto, name="modificar_producto"),
    path('agregar-producto/',agregar_producto, name="agregar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    #End of Admin    



    #URLS WEBPAY
    path('create/', create, name ="create"),
    path('commit/', webpay_commit, name="commit"),



    #URLS VENDEDOR
    path('ordenes/', listar_ordenes, name="ordenes"),
]


    
    
