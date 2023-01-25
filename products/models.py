from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("face", "face"),
        ("body", "body"),
    )
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
    categoria = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to="products_images", null=True)

    def __str__(self):
        return self.nombre