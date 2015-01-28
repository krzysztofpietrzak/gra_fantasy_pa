from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Gracz(models.Model):
    #dziedziczenie po userze
    user = models.OneToOneField(User, primary_key=True)

    nazwa = models.CharField(max_length=50)
    power = models.IntegerField(default=100)
    rasa = models.CharField(default="czlowiek", max_length=50)

    nazwa_grodu = models.CharField(max_length=20)

    gold = models.IntegerField()

    zamek = models.BooleanField(default=True)
    koszary = models.BooleanField(default=True)
    kopalnia = models.IntegerField(default=1)
    uniwersytet = models.BooleanField(default=False)
    prorok = models.BooleanField(default=False)


    #technologie
    #ludzie
    waluta = 0
    teologia = 0

    #gobliny
    sidla = 0
    lupienie = 0


    #jednostki
    wojownik = 5
    lucznik = 1
    rycerz = 0

