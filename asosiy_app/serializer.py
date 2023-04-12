from .models import *
from rest_framework import serializers

class AktyorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Aktyor
    fields='__all__'
  
    def validate_ism(self,qiymat):
      if len(qiymat)<3:
        raise serializers.ValidationError('ism uzunligi kam')
      return qiymat
        
      
  
class Tarifserializer(serializers.ModelSerializer):
  class Meta:
    model=Tarif
    fields='__all__'
      
      
class KinoSerializer(serializers.ModelSerializer):
  aktyor=AktyorSerializer(many=True)
  class Meta:
    model=Kino
    fields='__all__'
    

class KinoCreteSerializer(serializers.ModelSerializer):
  class Meta:
    model=Kino
    fields='__all__'
    
class Izohserializer(serializers.ModelSerializer):
  class Meta:
    model=Izoh
    fields='__all__'