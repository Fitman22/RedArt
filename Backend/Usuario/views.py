from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializer import UsuarioSerializer

class UsuarioLoginView(APIView):
    def get(self, request, userName, password, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(userName=userName, password=password)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        

class UsuarioCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioUpdateView(APIView):
    def put(self, request, usuario_id, *args, **kwargs):
        usuario = Usuario.objects.get(id=usuario_id)
        data = request.data.copy()
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioDetailView(APIView):
    def delete(self, request, usuario_id, *args, **kwargs):
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
