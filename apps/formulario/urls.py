from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.formulario.views import FormularioController

router = DefaultRouter()
app_name = "formulario"
router.register(r"formulario", FormularioController, basename="formulario")
urlpatterns = router.urls
