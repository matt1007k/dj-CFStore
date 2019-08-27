from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from .views import login_view, logout_view, register_view
from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/login/', login_view, name="login"),
    path('usuarios/logout/', logout_view, name="logout"),
    path('usuarios/registro/', register_view, name="register"),
    path('', ProductListView.as_view(), name="index"),
    path('productos/', include('products.urls', namespace='products'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
