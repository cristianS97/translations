# Generated by Django 4.2.19 on 2025-03-13 02:21

import applications.song.models
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("release_date", models.DateField(verbose_name="Fecha de lanzamiento")),
                (
                    "portada",
                    models.ImageField(upload_to=applications.song.models.upload_to),
                ),
                ("portada_base64", models.TextField(blank=True, null=True)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Última actualización"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Nombre artistico"),
                ),
                (
                    "real_name",
                    models.CharField(max_length=100, verbose_name="Nombre real"),
                ),
                ("nacimiento", models.DateField()),
                ("ciudad", models.CharField(max_length=100)),
                ("pais", models.CharField(max_length=100)),
                (
                    "imagen",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=applications.song.models.upload_to,
                    ),
                ),
                ("imagen_base64", models.TextField(blank=True, null=True)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Última actualización"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "name_spanish",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Nombre español",
                    ),
                ),
                (
                    "track_number",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Posición álbum"
                    ),
                ),
                (
                    "lyrics_original",
                    django_ckeditor_5.fields.CKEditor5Field(
                        verbose_name="Letra original"
                    ),
                ),
                (
                    "lyrics_spanish",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, null=True, verbose_name="Letra español"
                    ),
                ),
                ("video", models.CharField(max_length=100)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Última actualización"
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="song.album"
                    ),
                ),
                (
                    "artists",
                    models.ManyToManyField(to="song.artist", verbose_name="Artistas"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="song.artist"
            ),
        ),
    ]
