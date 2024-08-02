from django.urls import path
from .views import UsuarioLoginView, UsuarioCreateView, UsuarioUpdateView, UsuarioDetailView

urlpatterns = [
    path('usuarioGet/<str:userName>/<str:password>/', UsuarioLoginView.as_view(), name='usuario-login'),
    path('usuarioPost/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarioPut/<int:usuario_id>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarioDelete/<int:usuario_id>/', UsuarioDetailView.as_view(), name='usuario-delete'),
]
