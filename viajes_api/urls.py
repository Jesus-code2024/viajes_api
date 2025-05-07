from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from viajes import views
from rest_framework.authtoken.views import obtain_auth_token  # Importación correcta


router = routers.DefaultRouter()
router.register(r'destinos', views.DestinoViewSet)
router.register(r'itinerarios', views.ItinerarioViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),  # Endpoint para obtener tokens
    path('api-auth/', include('rest_framework.urls')),  # Para login en DRF
]