from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200,unique=True,blank=False,null=False)
    def __str__(self):
        return self.username
    
    
class GameList(models.Model):
    LIST_TYPES = [
        ('whishlist','Lista de deseos'),
        ('completed','Completados'),
        ('playing','Jugando'),
        ('backlog','Pendientes'),
        ('review','Reviews'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='game_lists')
    name = models.CharField(max_length=255, choices=LIST_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_name_display()} de {self.user.username}"


# Crear automáticamente las listas de juegos al crear un nuevo usuario.
@receiver(post_save, sender=CustomUser)
def create_default_lists(sender, instance, created, **kwargs):
    if created:
        for list_type, _ in GameList.LIST_TYPES:
            GameList.objects.create(user=instance, name=list_type)

class GameListItem(models.Model):
    game_list = models.ForeignKey(GameList, on_delete=models.CASCADE, related_name='items')
    game_id = models.IntegerField() # ID del juego en la API de RAWG
    game_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Juego {self.game_id} en {self.game_list.name}"

