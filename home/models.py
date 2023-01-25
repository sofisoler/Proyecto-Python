from django.db import models

class Card(models.Model):
    CATEGORY_CHOICES = (
        ("face", "face"),
        ("body", "body"),
    )
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    imagen = models.ImageField(upload_to="home_images", null=True)