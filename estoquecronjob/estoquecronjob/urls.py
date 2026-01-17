# estoque/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('produtos.urls')),
]