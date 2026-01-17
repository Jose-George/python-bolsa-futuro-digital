from django.urls import path
from .views import LogMensagemView

urlpatterns = [
    path('logs/', LogMensagemView.as_view()),
]

