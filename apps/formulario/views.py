from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from apps.formulario.serializers import FormularioSerializer
from config.utils.utlis_view_api import CustomPagination

# Create your views here.


class FormularioController(viewsets.ModelViewSet):
    serializer_class = FormularioSerializer
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    permission_classes = [IsAuthenticated]

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
