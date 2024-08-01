from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comentario
from .serializer import ComentarioSerializer

class ComentarioListView(APIView):
    def get(self, request, ilustracion_id, *args, **kwargs):
        comentarios = Comentario.objects.filter(ilustracion_id=ilustracion_id)
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

class ComentarioCreateView(APIView):
    def post(self, request, ilustracion_id, usuario_id, *args, **kwargs):
        data = request.data.copy()
        data['ilustracion'] = ilustracion_id
        data['usuario'] = usuario_id
        serializer = ComentarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ComentarioUpdateView(APIView):
    def put(self, request, comentario_id, *args, **kwargs):
        comentario = Comentario.objects.get(id=comentario_id)
        data = request.data.copy()
        serializer = ComentarioSerializer(comentario, data=data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ComentarioDeleteView(APIView):
    def delete(self, request, comentario_id, *args, **kwargs):
        comentario = Comentario.objects.get(id=comentario_id)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
