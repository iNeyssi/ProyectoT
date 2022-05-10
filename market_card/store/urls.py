from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'), # 127.0.0.1:8000
    path('cart/<int:pk>/', views.cart, name="cart"), # 127.0.0.1:8000/cart/1
    path("registrarProducto/", views.crear_product),
    ]