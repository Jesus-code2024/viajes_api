from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'destinos', views.DestinoViewSet)
router.register(r'itinerarios', views.ItinerarioViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = router.urls