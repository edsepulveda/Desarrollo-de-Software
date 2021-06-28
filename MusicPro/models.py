from django.db import models



#las opciones disponibles en tipo consulta
opciones_consultas = [
    [0, "consultas"],
    [1, "reclamos"],
    [2, "sugrencias"],
    [3, "felicitaciones"]
]
#modelo para el contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre

