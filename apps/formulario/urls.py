from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FormularioController, GeneralReporteCompleto

router = DefaultRouter()
app_name = "formulario"
router.register(r"formulario", FormularioController, basename="formulario")
urlpatterns = router.urls
urlpatterns += [
    path("formulario/reportecompleto/<int:id>/", GeneralReporteCompleto.as_view()),
]
