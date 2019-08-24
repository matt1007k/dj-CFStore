from django.contrib import admin
from django.urls import path

from .views import index, login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/login/', login_view, name="login"),
    path('usuarios/logout/', logout_view, name="logout"),
    path('usuarios/registro/', register_view, name="register"),
    path('', index, name="index")
]
