from django.db import models

class Hobbie(models.Model):
  FREQUENCIA = [
    ("N", "Nunca"),
    ("E", "Esporadicamente"),
    ("S", "Sempre"),
  ]
  CATEGORIA = [
    ("L", "Lazer"),
    ("E", "Estudo"),
    ("S", "Saúde"),
  ]
  title = models.CharField(max_length=50)
  frequencia = models.CharField(max_length=1, choices=FREQUENCIA)
  prioridade = models.IntegerField()
  categoria = models.CharField(max_length=1, choices=CATEGORIA)

class Carro(models.Model):
  CARROCERIA = [
    ("C","Coupé"),
    ("S", "Sedã"),
    ("SUV", "SUV"),
  ]
  COMBUSTIVEL = [
    ("C","Combustão"),
    ("H", "Híbrido"),
    ("E", "Elétrico"),
  ]
  title = models.CharField(max_length=50)
  modelo = models.CharField(max_length=50)
  montadora = models.CharField(max_length=50)
  carroceria = models.CharField(max_length=3, choices=CARROCERIA)
  tipo_motor = models.CharField(max_length=1, choices=COMBUSTIVEL)

class FichaTecnica(models.Model):
  TIPOS = [
    ("M","Motorização"),
    ("D", "Desempenho"),
  ]
  UNIDADES = [
    ("cv", "Cavalos"),
    ("Newton X metros", "Nm"),
    ("Quilômetros por hora", "km/h"),
    ("s","Segundos"),
  ]
  title = models.CharField(max_length=70)
  tipo_dados = models.CharField(max_length=1, choices=TIPOS)
  dados = models.FloatField()
  unidade = models.CharField(max_length=20, choices=UNIDADES)