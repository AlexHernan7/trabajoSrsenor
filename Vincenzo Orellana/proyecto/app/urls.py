from django.urls import path
from .views import index, api, form, mision, noticias

urlpatterns = [
    path('', index, name="index"),
    path('/form', form, name="form"),
    path('/mision', mision, name="mision"),
    path('/api', api, name="api"),
    path('/noticias', noticias, name="noticias"),

]