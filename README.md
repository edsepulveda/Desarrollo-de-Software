## Pasos previos para la instalacion
# Ver requirements.txt para una instalacion mas rapida. (pip install -r requirements.txt)


# Realizar 
1) En terminal con ubicacion en folder:
 
	python manage.py createsuperuser
	nombre: admin   pass: adminadmin


2) En terminal con ubicacion en folder:

	pip install -r requirements.txt


3) En terminal con ubicacion en folder:

	python manage.py makemigrations
	python manage.py migrate


4) En http://localhost:8000/admin/

	crear las siguientes categorias:
		Cuerdas, Percusion, Accesorios, Amplificadores


5) Para agregar producto logearse como admin en agregar desde el dashboard
	las fotos estan en la carpeta media.


6) para comprar registrarse y desde http://localhost:8000/admin/  
	asignar usuario creado en la primera seccion de usuarios.
