from django.urls import path
from .views import ComentarioListView, ComentarioCreateView, ComentarioUpdateView, ComentarioDeleteView

urlpatterns = [
    path('comentariosGet/<int:ilustracion_id>/', ComentarioListView.as_view(), name='comentarios-list'),
    path('comentariosPost/<int:ilustracion_id>/<int:usuario_id>/', ComentarioCreateView.as_view(), name='comentarios-create'),
    path('comentariosUpdate/<int:comentario_id>/', ComentarioUpdateView.as_view(), name='comentarios-update'),
    path('comentariosDelete/<int:comentario_id>/', ComentarioDeleteView.as_view(), name='comentarios-delete'),
]
