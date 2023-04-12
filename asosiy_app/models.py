from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
def validate_davlat(qiymat):
  davlatlar=['Uzbekiston','AQSH','Angly','Russia']
  if qiymat not in davlatlar:
    raise ValidationError('bu davlatni aktiyorlarin saqlash munkin emas')
  return qiymat
  
class Aktyor(models.Model):
  ism=models.CharField(max_length=50)
  tugulgan_yil=models.DateField()
  jins=models.CharField(max_length=20)
  davlat=models.CharField(max_length=50,validators=[validate_davlat])
  def __str__(self) -> str:
    return self.ism
  
class Kino(models.Model):
  nom=models.CharField(max_length=50)
  yil=models.DateField()
  janr=models.CharField(max_length=50)
  aktyor=models.ManyToManyField(Aktyor)
  def __str__(self) -> str:
    return self.nom
  
class Tarif(models.Model):
  nom=models.CharField(max_length=50)
  narx=models.IntegerField(validators=[MinValueValidator(5)])
  muddat=models.CharField(max_length=50)
  def __str__(self) -> str:
    return self.nom
  
class Izoh(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  kino=models.ForeignKey(Kino,on_delete=models.CASCADE,blank=True,null=True)
  matn=models.CharField(max_length=255)
  vaqt=models.DateTimeField(auto_now_add=True)
