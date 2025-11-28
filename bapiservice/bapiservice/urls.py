from django.contrib import admin
from django.urls import path
from produtos.views import listar_produtos, criar_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path("produtos/", listar_produtos),
    path("produtos/criar/", criar_produto),
]
