# Generated by Django 4.1.5 on 2023-01-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
