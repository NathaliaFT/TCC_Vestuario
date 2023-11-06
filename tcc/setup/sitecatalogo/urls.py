from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("registro", views.registro_usuario, name="registro"),
    path("catalogo_usuario", views.catalogo, name="catalogo_usuario"),
    path("user_login", views.user_login, name="user_login"),
    path("categoria", views.categoria, name="categoria")
]