from rest_framework import serializers
from .models import Destino, Iterinario, Reserva

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'


class IterinarioSerializer(serializers.ModelSerializer):
    destinos = DestinoSerializer(many=True, read_only=True)
    class Meta:
        model = Iterinario
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'