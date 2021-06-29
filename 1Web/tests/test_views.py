from django.http import HttpRequest
from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY, get_user_model

from ..views import *

from django.test import Client, RequestFactory
from django.urls import reverse

from ..views import home



class TestViewsResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin1")
        Categoria.objects.create(nombre="Percusion", slug="percusion")
        Producto.objects.create(categoria_id=1, tipo_categoria=2, slug='fab-124', modelo='Flash', marca="LOL",
                                            precio='12423', imagen='cuerdas', stock='34')
        
    
    def test_url_hosts(self):
        
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)



class LoginTest(TestCase):
    def setUp(self):
        self.c = Client()
        #Esto para probar el form

        self.username = 'testuser1'
        self.password = 'secret011'



        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create(**self.credentials)

    def TestLogin(self):
        #
        response = self.c.post('/accounts/login/', **self.credentials)

        self.assertTrue(response.context['user'].is_active())


    def test_login_url(self):
        response = self.c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/login.html')

    
    def test_login_form(self):
        response = self.c.post(reverse('login'), data={
            'username': self.username,
            'password': self.password
        })

        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)



class RegistroTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.username = 'pepeito1'
        self.first_name = 'juan'
        self.last_name = 'perez'
        self.email = 'admin@admin.com'
        self.password = 'asdadsadasd@@'
    

    def test_registro_url(self):
        response = self.c.get('/registro/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/registro.html")


    def test_registro_view(self):
        response = self.c.get(reverse('registro'), data={
            'username': self.username,
            'name': self.first_name,
            'last': self.last_name,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)





class TestsUrls(TestCase):
    def setUp(self):
        self.c = Client()


    def test_api_url(self):
        response = self.c.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_silk_url(self):
        response = self.c.get('/silk/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_url(self):
        response = self.c.get('/informe/')
        #Si no eres admin, al momento de querer ingresar a la pagina, esta te rediccionara
        #Por eso el status code es de 302 que significa que la pagina redirecciono, dado que al hacer testeos
        #Este no se encuentra en el modo SuperUser
        self.assertEqual(response.status_code, 302)

        

