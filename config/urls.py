"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from asosiy_app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router=DefaultRouter()
router.register("izohlar",IzohModelViewSet),
router.register('kinolar',KinoModelViewSet),
router.register('aktyor',AktyorViewSet),
router.register('tariflar',TarifViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_token/',obtain_auth_token),
    # path('aktyorlar/',AktiyorAPIView.as_view(),name='aktyorlar'),
    # path('tariflar/',TarifAPIView.as_view(),name='tariflar'),
    # path('tarifu/<int:pk>/',TarifUAPIView.as_view(),name='tarifu'),
    # # path('kinolar/',KinoAPIView.as_view(),name='kinolar'),
    # # path('kinocrete/<int:pk>/',KinoUpdeatAPIView.as_view(),name='kinocrete'),
    # path('aktyor/<int:pk>/',AktyorQAPIView.as_view(),name='aktyoru')

]
