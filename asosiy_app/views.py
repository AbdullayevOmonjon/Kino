from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *


class AktyorViewSet(ModelViewSet):
  # authentication_classes=[TokenAuthentication]
  # permission_classes=[IsAuthenticated]
  queryset=Aktyor.objects.all()
  serializer_class=AktyorSerializer

class TarifViewSet(ModelViewSet):
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  queryset=Tarif.objects.all()
  serializer_class=Tarifserializer

class KinoModelViewSet(ModelViewSet):
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  queryset=Kino.objects.all()
  serializer_class=KinoCreteSerializer
 
  
  
class IzohModelViewSet(ModelViewSet):
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  queryset=Izoh.objects.all()
  serializer_class=Izohserializer  
  def get_queryset(self):
    queryset=Izoh.objects.filter(user=self.request.user)
    return queryset 
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
    return Response(serializer.data)
  

  
  
  @action(detail=True, methods=['GET','POST'])
  def kinolar(self,request,pk):
    if request.method=='POST':
      serializer = KinoCreteSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(izoh=Izoh.objects.get(id=pk))
        return Response(serializer.data)
    kino=Kino.objects.filter(izoh__id=pk)
    serializer=KinoCreteSerializer(kino,many=True)
    return Response(serializer.data)

# class IzohModelViewSet(ModelViewSet):
#   queryset=Izoh.objects.all()
#   serializer_class=Izohserializer   
  
  
#   @action(detail=True, methods=['GET','POST'])
#   def kinolar(self,request,pk):
#     kino=Kino.objects.filter(izoh__id=pk)
#     serializer=KinoCreteSerializer(kino,many=True)
#     return Response(serializer.data)
  
# class AktiyorAPIView(APIView):
#   authentication_classes=[TokenAuthentication]
#   pagination_class=[IsAuthenticated]
#   def get(self,request):
#     aktyorlar=Aktyor.objects.all()
#     serializer=AktyorSerializer(aktyorlar,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)
  
#   def post(self,request):
#     aktyor=request.data
#     serializer=AktyorSerializer(data=aktyor)
#     if serializer.is_valid():
#       Aktyor.objects.create(
#           ism=serializer.validated_data.get('ism'),
#           tugulgan_yil=serializer.validated_data.get("tugulgan_yil"),
#           jins=serializer.validated_data.get('jins'),
#           davlat=serializer.validated_data.get("davlat")
#       )
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
  
  
# class AktyorQAPIView(APIView):
#   authentication_classes=[TokenAuthentication]
#   pagination_class=[IsAuthenticated]
#   def get(self,request,pk):
#     aktyorlar=Aktyor.objects.get(id=pk)
#     serializer=AktyorSerializer(aktyorlar,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)
  
#   def put(self,request,pk):
#     aktyor=Aktyor.objects.get(id=pk)
#     serializer=AktyorSerializer(aktyor,data=request.data)
#     if serializer.is_valid():
#       aktyor.ism=serializer.validated_data.get('ism')
#       aktyor.davlat=serializer.validated_data.get('davlat')
#       aktyor.save()
#       return Response(serializer.data,status=status.HTTP_202_ACCEPTED  )
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
# #   # def delete(self,request,pk):
# #   #   Aktyor.objects.get(id=pk).delete() 
    
  
# # class AktyorDeleteAPIView(APIView):
# #   def get(self,request,pk):
# #     aktyor=Aktyor.objects.get(id=pk).delete()
# #     serializer=Aktiyorserializer(aktyor,data=request.data)
# #     return Response(serializer.data)
    
 
 
# class TarifAPIView(APIView):
#   authentication_classes=[TokenAuthentication]
#   pagination_class=[IsAuthenticated]
#   def get(self,request):
#     tarif=Tarif.objects.all()
#     serializer=Tarifserializer(tarif,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK) 
  
#   def post(self,request):
#     tarif=request.data
#     serializer=Tarifserializer(data=tarif)
#     if serializer.is_valid():
#       Tarif.objects.create(
#           nom=serializer.validated_data.get("nom"),
#           narx=serializer.validated_data.get("narx"),
#           muddat=serializer.validated_data.get("muddat")
#       )
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
# class TarifUAPIView(APIView):
#   authentication_classes=[TokenAuthentication]
#   pagination_class=[IsAuthenticated]
#   def put(self,request,pk):
#     tarif=Tarif.objects.get(id=pk)
#     serializer=Tarifserializer(tarif,data=request.data)
#     if serializer.is_valid():
#       tarif.nom=serializer.validated_data.get('nom'),
#       tarif.narx=serializer.validated_data.get('narx')
#       tarif.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
#   def delete(self,request,pk):
#     tarif=Tarif.objects.filter(id=pk).delete()
#     serializer=serializers(tarif,data=request.data)
#     return Response(serializer.data,status=status.HTTP_200_OK
#                     )
  
# class KinoViewSet(ModelViewSet):
#   queryset=Kino.objects.all()
#   serializer_class=KinoSerializer 
# # class KinoAPIView(APIView):
# #   authentication_classes=[TokenAuthentication]
# #   pagination_class=[IsAuthenticated]
# #   def get(self,request):
# #     kinolar=Kino.objects.all()
# #     serializer=KinoSerializer(kinolar,many=True)
# #     return Response(serializer.data) 
  
# #   def post(self,request):
# #     kino=request.data 
# #     serializer=KinoCreteSerializer(data=kino)
# #     if serializer.is_valid():
# #       serializer.save()
# #       return Response(serializer.data,status=status.HTTP_201_CREATED)
# #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

# # class KinoUpdeatAPIView(APIView):
# #   authentication_classes=[TokenAuthentication]
# #   pagination_class=[IsAuthenticated]
# #   def put(self,request,pk):
# #     kino=Kino.objects.get(id=pk)
# #     serializer=KinoCreteSerializer(kino,data=request.data)
# #     if serializer.is_valid():
# #         serializer.save(),
# #         return Response(serializer.data,status=status.HTTP_200_OK)
# #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
# #   def delete(self,request,pk):
# #     kino=Kino.objects.get(id=pk).delete
# #     serializer=KinoCreteSerializer(kino,data=request.data)
# #     return Response(serializer.data,status=status.HTTP_200_OK)
  
# class IzohModelViewSet(ModelViewSet):
#   authentication_classes=[TokenAuthentication]
#   pagination_class=[IsAuthenticated]
#   queryset=Izoh.objects.all()
#   serializer_class=Izohserializer   
  
  
#   @action(detail=True, methods=['GET','POST'])
#   def kinolar(self,request,pk):
#     if request.method=='POST':
#       serializer = KinoCreteSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save(izoh=Izoh.objects.get(id=pk))
#         return Response(serializer.data)
#     kino=Kino.objects.filter(izoh__id=pk)
#     serializer=KinoCreteSerializer(kino,many=True)
#     return Response(serializer.data)