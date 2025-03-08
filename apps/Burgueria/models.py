from django.db import models

# Create your models here.

class Sanduiche(models.Model):
    """
        Modelo que representa um sanduiche no banco de dados   
    """    
    nome = models.CharField(max_length=100),
    