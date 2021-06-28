from django.test import TestCase

from ..models import *
from django.contrib.auth.models import User

#Buscamos testear que la cateogoria sea creada con exito y luego devolver un assert de que esa categoria existe
#Y si esa cateogoria existe va a pasar el test
class TestCategoriaModel(TestCase):
    def setUp(self):
        self.data1 = Categoria.objects.create(nombre="Cuerdas", slug="cuerdas")

    def test_category_model_entry(self):
        """
        Testear el modelo de la categoria con la insercion de datos
        """

        data = self.data1
        self.assertTrue(isinstance(data, Categoria))


    def test_category_model_entry(self):
        """
        Vamos a testear que el nombre que creamos sea el de por defecto
        """

        data = self.data1
        self.assertEqual(str(data), 'Cuerdas')



class TestProductoModel(TestCase):

    def setUp(self):
        Categoria.objects.create(nombre="Cuerdas",slug="cuerdas")
        
        self.data1 = Producto.objects.create(categoria_id=1, tipo_categoria=2, slug='fab-124', modelo='Flash', marca="LOL",
                                            precio='12423', imagen='cuerdas', stock='34')


    def test_producto_model_entry(self):
        """
        Testear el modelo del producto con la insercion de datos
        """

        data = self.data1
        self.assertTrue(isinstance(data, Producto))
        self.assertEqual(str(data), 'LOL')



class TestUsuarioModel(TestCase):
    def setUp(self):
        User.objects.create(username="admin1")
        self.data1 =  Usuario.objects.create(name="admin1", email="admin1@admin.cl")

    def test_usuario_model_entry(self):
        data = self.data1

        self.assertTrue(isinstance(data, Usuario))
        self.assertEqual(str(data), 'admin1')



class TestContactoModel(TestCase):
    def setUp(self):
        self.data1 = Contacto.objects.create(nombre="Pepe", correo="locura@admin.com", tipo_consulta=3, mensaje="adjsdaklja", avisos=0)

    def test_contacto_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'Pepe')




class TestOrdenModel(TestCase):
    def setUp(self):
        User.objects.create(username="admin1")
        Usuario.objects.create(name="admin1", email="admin1@admin.cl")

        self.data1 = Orden.objects.create(id=1, dia_orden="2021-05-13 12:54:23", entregado=0, transaccion_id=12412213)

    def test_orden_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Orden))
        self.assertEqual(str(data), '1')