from django.db import models

# Create your models here.


from django.utils import timezone

class Posteo(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_public = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_public = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
