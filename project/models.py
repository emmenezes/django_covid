from django.db import models
from django.utils import timezone

# Create your models here.
class Paciente(models.Model):
    # 
    RT_PCR = 'RT-PCR'
    Sorologia = 'Sorologia'
    TR_Antigenos = 'Teste Rápido - Antígenos'
    TR_Anticorpos = 'Teste Rápido - Anticorpos'
    
    TESTE_CHOICES = [
        (RT_PCR, 'RT-PCR'),
        (Sorologia, 'Sorologia'),
        (TR_Antigenos, 'Teste Rápido - Antígenos'),
        (TR_Anticorpos, 'Teste Rápido - Anticorpos'),
    ]

    Positivo = 'Positivo'
    Negativo = 'Negativo'

    RESULTADO_CHOICES = [
        (Positivo, 'Positivo'),
        (Negativo, 'Negativo'),
    ]
    
    class Meta:
        db_table = 'paciente'

    nome = models.CharField(("Nome"), max_length=100)
    data_nascimento = models.DateField()
    teste = models.CharField(
        max_length = 30,
        choices = TESTE_CHOICES,
        default = RT_PCR,
    )
    resultado = models.CharField(
        max_length = 30,
        choices = RESULTADO_CHOICES,
        default = Negativo,
    )

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.nome


