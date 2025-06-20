# Generated by Django 5.2.2 on 2025-06-09 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.IntegerField(default=0)),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoActual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.IntegerField(default=0)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('autor', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.IntegerField(blank=True, default=0, null=True)),
                ('cantidad', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('accion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libro')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('calificacion', models.IntegerField(choices=[(1, '1 - Muy mala'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - Muy buena')], default=5)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resenas', to='app.libro')),
            ],
        ),
        migrations.CreateModel(
            name='CarritoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libro')),
            ],
            options={
                'unique_together': {('usuario', 'libro')},
            },
        ),
    ]
