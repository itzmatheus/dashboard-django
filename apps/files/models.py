from django.db import models

class Consulta(models.Model):
  numero_guia_consulta = models.IntegerField(blank=True, null=True)
  cod_medico = models.IntegerField(blank=True, null=True)
  nome_medico = models.CharField(max_length=100, blank=True, null=True)
  data_consulta = models.DateField(blank=True, null=True)
  valor_consulta = models.DecimalField(max_digits=9, decimal_places=2)


class Exame(models.Model):
  numero_guia_consulta = models.IntegerField(blank=True, null=True)
  descricao = models.TextField(blank=True, null=True)
  valor_exame = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)