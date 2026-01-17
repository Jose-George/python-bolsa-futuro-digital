from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LogMensagem
from .serializers import LogMensagemSerializer

class LogMensagemView(APIView):
    def get(self, request):
        logs = LogMensagem.objects.all()
        serializer = LogMensagemSerializer(logs, many=True)
        return Response(serializer.data)