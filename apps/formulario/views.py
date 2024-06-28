import traceback

from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.formulario.serializers import FormularioSerializer
from config.utils.utlis_view_api import CustomPagination

from ..users.authentication import IsTokenValid
from .models import Formulario
from .utils.reportes import crear_reporte_completo_paciente

# Create your views here.


class FormularioController(viewsets.ModelViewSet):
    serializer_class = FormularioSerializer
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    permission_classes = [IsAuthenticated, IsTokenValid]

    filterset_fields = {
        "id": ["exact"],
        "nombre": ["contains", "exact", "icontains", "search"],
    }
    search_fields = [
        "nombre",
    ]
    ordering_fields = [
        "pk",
        "nombre",
    ]
    ordering = ["-pk"]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class GeneralReporteCompleto(APIView):
    permission_classes = [IsAuthenticated, IsTokenValid]

    def get(self, request, id):
        try:
            q = Formulario.objects.filter(id=id)
            if not q.exists():
                return JsonResponse(
                    {
                        "status": "error",
                        "message": "Error de en servidor",
                    },
                    status=404,
                )
            return crear_reporte_completo_paciente(q)

        except:
            print(traceback.format_exc())
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Error de en servidor",
                },
                status=500,
            )
