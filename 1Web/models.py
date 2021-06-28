from django.db import models
from django.contrib.auth.models import User

#las opciones disponibles en tipo consulta
opciones_consultas = [
    [0, "consultas"],
    [1, "reclamos"],
    [2, "reservas"],
    [3, "felicitaciones"]
]


sub_categorias = [
    [0, "Guitarras"],
    [1, "Bajos"],
    [2, "Pianos"],
    [3, "Baterias Acusticas"],
    [4, "Bateria Electronica"],
    [5, "Cabezales"],
    [6, "Cajas"],
    [7, "Audifonos"],
    [8, "Monitores"],
    [9, "Parlantes"],
    [10, "Cables"],
    [11, "Microfonos"],
    [12, "Interfaces"],
    [13, "Mixers"],
]

#Modelo para el usuario logeado

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.name



#modelo para el contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre




#CUERDAS, PERCUSION, AMPLIFICADORES, ACCESORIOS
class Categoria(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre    



#modelo del producto
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    tipo_categoria = models.IntegerField(choices=sub_categorias)
    slug = models.SlugField(max_length=255, unique=True)
    modelo = models.CharField(max_length=250 ,blank= False, null= False)
    marca  = models.CharField(max_length = 200, blank = False, null = False)
    precio = models.IntegerField(blank= False, null= False)
    imagen = models.ImageField(upload_to = "productos/", null=True)
    stock = models.IntegerField(blank= False, null= False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['marca']   


    def __str__(self):
        return self.marca

class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    dia_orden = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)
    transaccion_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        ordenitem = self.ordenitem_set.all()
        total = sum([item.getTotal for item in ordenitem])
        return total

    @property
    def get_items_total(self):
        ordenitem = self.ordenitem_set.all()
        total = sum([item.cantidad for item in ordenitem])
        return total

class OrdenItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)


    @property
    def getTotal(self):
        total = self.producto.precio * self.cantidad
        return total


class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=250, null=False)
    comuna = models.CharField(max_length=250, null=False)
    codigo_postal = models.CharField(max_length=255, null=False)
    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.direccion



