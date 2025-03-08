from django.db import models

# Create your models here.

class Sanduiche(models.Model):
    """
        Modelo que representa um sanduiche no banco de dados   
    """    
    nome = models.CharField(max_length=100, verbose_name="Nome do Sanduiche")
    descricao = models.TextField(verbose_name="Descrição", help_text="Descreva os ingredientes e caracteristicas do sanduiche.")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço", help_text="Valor do sanduiche em R$")
    emPromocao = models.BooleanField(default=False, verbose_name="Em promoção", help_text="Marque se está em promoção")
    
    def __str__(self):
        return self.nome
    
    
class InfoNutricional(models.Model):
    """
        Modelo que armazena as informações nutricionais dos sanduiches
    """
    sanduiche = models.OneToOneField(Sanduiche, on_delete=models.CASCADE)
    calorias = models.PositiveIntegerField(verbose_name="Calorias (kcal)")
    proteinas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Proteinas (g)")
    gorduras = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gorduras (g)")
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Carboidratos (g)")
    gorduras_saturadas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gorduras saturadas (g)")
    gorduras_trans = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gorduras Trans (g)")
    sodio = models.PositiveIntegerField(verbose_name="Sódio (mg)")
    
    def __str__(self):
        return f"Informações nutricionais de {self.sanduiche.nome}"