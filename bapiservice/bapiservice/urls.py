from django.contrib import admin
from django.urls import path, include
from produtos.views import listar_produtos, criar_produto
from rest_framework.routers import DefaultRouter
from todo.views import TarefaViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("produtos/", listar_produtos),
    path("produtos/criar/", criar_produto),
    path("", include(router.urls)),
]
