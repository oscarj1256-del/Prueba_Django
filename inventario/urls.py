from django.urls import path
from . import views
from .views import ProductoListAPI


urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('api/productos/', ProductoListAPI.as_view(), name='api_productos'),

]
