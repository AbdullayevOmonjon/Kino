# Generated by Django 4.1.7 on 2023-03-30 15:57

import asosiy_app.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tugulgan_yil', models.DateField()),
                ('jins', models.CharField(max_length=20)),
                ('davlat', models.CharField(max_length=50, validators=[asosiy_app.models.validate_davlat])),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('narx', models.IntegerField(validators=[django.core.validators.MinValueValidator(5)])),
                ('muddat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('yil', models.DateField()),
                ('janr', models.CharField(max_length=50)),
                ('aktyor', models.ManyToManyField(to='asosiy_app.aktyor')),
            ],
        ),
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=255)),
                ('vaqt', models.DateTimeField(auto_now_add=True)),
                ('kino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy_app.kino')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]