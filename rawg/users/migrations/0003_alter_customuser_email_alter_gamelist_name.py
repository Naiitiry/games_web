# Generated by Django 5.2.1 on 2025-05-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_gamelistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gamelist',
            name='name',
            field=models.CharField(choices=[('whishlist', 'Lista de deseos'), ('completed', 'Completados'), ('playing', 'Jugando'), ('backlog', 'Pendientes'), ('review', 'Reviews')], max_length=255),
        ),
    ]
