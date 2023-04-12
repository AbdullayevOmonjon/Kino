# from unittest import TestCase
# from asosiy_app.models import *
# from rest_framework.test import APIClient


# class TestAktyorViewset(TestCase):
#   def setUp(self) -> None:
#     self.client=APIClient()
    
#   def test_aktyorlar(self):
#     natija=self.client.get('/aktyorlar/')
#     assert natija.status_code ==200
#     aktyorlar=natija.data
#     assert len(aktyorlar) == Aktyor.objects.count()
#     # print(aktyorlar[0])
#     assert aktyorlar[0]['ism'] == Aktyor.objects.first().ism
#     assert aktyorlar[0]['jins'] == Aktyor.objects.first().jins
#     assert aktyorlar[0]['davlat'] == Aktyor.objects.first().davlat
    
    
  # def test_aktyor_valid(self):
  #   natija=self.client.get('/aktyor/1/')
  #   assert natija.status_code == 200
  #   assert natija.data['id'] == 3
  #   assert natija.data[0]['ism'] == Aktyor.objects.first().ism
  #   assert natija.data[0]['jins'] == Aktyor.objects.first().jins
  #   assert natija.data[0]['davlat'] == Aktyor.objects.first().davlat 
    
  # def test_aktyor_qoshish(self):
  #   aktyor={
  #     "id":7,
  #     'ism':"Ulugbek Qodirv",
  #     'davlat':'uzbekiston',
  #     "jins":"Erkak"
  #   }
  #   natija=self.client.post('/aktyorlar/',data=aktyor)
  #   assert natija.status_code==400
  #   assert natija.data['jins'][0] == 'Erkak yoki Ayol sozidan birini yozish munkun halos'
    
    
  # def test_aktyor_qoshish(self):
  #   aktyor={
  #     "id":7,
  #     'ism':"Ulugbek Qodirv",
  #     'tugulgan_yil':'1986-02-15',
  #     'davlat':'uzbekiston',
  #     "jins":"ogilbola"
  #   }
  #   natija=self.client.post('/aktyorlar/',data=aktyor)
  #   assert natija.statuc_code==201
  #   assert natija.data['id'] is not None
  #   assert natija.data['ism']==Aktyor.objects.last().ism
  #   assert natija.data['davlat']==Aktyor.objects.last().davlat
  #   assert natija.data['jins']==Aktyor.objects.last().jins
  
  # def test_aktyor_updet(self):
  #   aktyor={
  #     "id":"2",
  #     "ism":"Ulugbek Qodirov",
  #     "tugulgan_yil":"1983-08-03",
  #     "jins":"Erkak",
  #     "davlat":"Qozogiston"
  #   }
  #   eski=Aktyor.objects.get(id=2)
  #   natija=self.client.put('/aktyor/2/',data=aktyor)
  #   assert natija.status_code == 202
  #   assert natija.data['ism']==Aktyor.objects.get(id=2).ism
  #   assert natija.data['davlat']==Aktyor.object.get(id=2).davlat
    

    
  
    