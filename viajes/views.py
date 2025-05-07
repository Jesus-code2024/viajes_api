from rest_framework import viewsets, permissions
from .models import Destino, Iterinario, Reserva
from .serializers import DestinoSerializer, IterinarioSerializer, ReservaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ItinerarioViewSet(viewsets.ModelViewSet):
    queryset = Iterinario.objects.all()
    serializer_class = IterinarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filtra itinerarios del usuario o compartidos con él
    def get_queryset(self):
        user = self.request.user
        return Iterinario.objects.filter(usuario=user) | Iterinario.objects.filter(compartir_con=user)

    # Acción personalizada para compartir itinerario
    @action(detail=True, methods=['post'])
    def compartir(self, request, pk=None):
        itinerario = self.get_object()
        usuario_id = request.data.get('usuario_id')
        try:
            usuario = User.objects.get(id=usuario_id)
            itinerario.compartido_con.add(usuario)
            return Response({'status': 'Itinerario compartido'})
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=404)

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reserva.objects.all()

    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user)