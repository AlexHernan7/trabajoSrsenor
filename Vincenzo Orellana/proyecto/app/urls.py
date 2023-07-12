from django.urls import path
from .views import index, api, form, mision, noticias, tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns = [
    path('', index, name="index"),
    path('form', form, name="form"),
    path('mision', mision, name="mision"),
    path('api', api, name="api"),
    path('noticias', noticias, name="noticias"),
    path('tienda', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]