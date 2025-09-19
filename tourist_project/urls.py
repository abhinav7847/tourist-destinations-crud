"""
URL configuration for tourist_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from destinations.views import DestinationViewSet, home, destination_list, destination_detail, destination_create, destination_update, destination_delete

router = routers.DefaultRouter()
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),   # API Endpoints
    path('', home, name='home'),          # Homepage
    path('destinations/', destination_list, name='destination_list'),
    path('destinations/<int:pk>/', destination_detail, name='destination_detail'),
    path('destinations/create/', destination_create, name='destination_create'),
    path('destinations/<int:pk>/update/', destination_update, name='destination_update'),
    path('destinations/<int:pk>/delete/', destination_delete, name='destination_delete'),
]
