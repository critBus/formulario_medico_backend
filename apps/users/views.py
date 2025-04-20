import traceback

from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.authentication import (
    IsTokenValid,
    SoloPuedeModificarseElMismo,
    WithAccessToken,
)
from apps.users.models import BlackListedTokenAccess
from apps.users.serializers import (
    TokenAccesBlacklistSerializer,
    UserCreateSerializer,
    UserSerializerRepresentation,
    UserUpdateSerializer,
)
from config.utils.utils import logger
from config.utils.utlis_view_api import (
    Base_Create,
    Base_Destroy,
    Base_List,
    Base_Retrieve,
    Base_Update,
)


class User_Create(Base_Create):
    serializer_class = UserCreateSerializer

    @extend_schema(
        responses={201: UserSerializerRepresentation},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class User_Update(Base_Update):
    serializer_class = UserUpdateSerializer
    permission_classes = (
        IsAuthenticated,
        IsTokenValid,
        SoloPuedeModificarseElMismo,
    )

    @extend_schema(responses={200: UserSerializerRepresentation})
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(responses={200: UserSerializerRepresentation})
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class User_List(Base_List):
    

    serializer_class = UserSerializerRepresentation
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = {
        "id": ["exact"],
        "last_login": ["gte", "lte", "gt", "lt", "exact"],
        "is_superuser": ["exact"],
        "username": ["contains", "exact", "icontains",],
        "email": ["contains", "exact", "icontains",],
        "first_name": ["contains", "exact", "icontains", ],
        "last_name": ["contains", "exact", "icontains", ],
        "is_active": ["exact"],
        "is_staff": ["exact"],
        "groups__id": ["exact"],
        "groups__name": ["contains", "exact", "icontains",],
        "groups__permissions__id": ["exact"],
        "groups__permissions__name": ["contains", "exact", "icontains",],
        "groups__permissions__codename": ["contains", "exact", "icontains",],
        "user_permissions__id": ["exact"],
        "user_permissions__name": ["contains", "exact", "icontains",],
        "user_permissions__codename": ["contains", "exact", "icontains",],
    }
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    ordering_fields = [
        "pk",
        "last_login",
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    ordering = ["username"]


class User_Retrieve(Base_Retrieve):
    serializer_class = UserSerializerRepresentation


class User_Retrieve_SinId(generics.GenericAPIView):
    permission_classes = (
        IsAuthenticated,
        IsTokenValid,
    )
    serializer_class = UserSerializerRepresentation

    @extend_schema(
        responses={200: UserSerializerRepresentation},
    )
    def get(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class User_Destroy(Base_Destroy):
    serializer_class = UserSerializerRepresentation
    permission_classes = (
        IsAuthenticated,
        IsTokenValid,
        SoloPuedeModificarseElMismo,
    )


class Logout(WithAccessToken, APIView):
    permission_classes = (
        IsAuthenticated,
        IsTokenValid,
    )

    @extend_schema(
        request=TokenAccesBlacklistSerializer,
    )
    def post(self, request, *args, **kwargs):
        """
        Vista que invalida un token de autenticación de un usuario en la aplicación.
        """
        try:
            serializer = TokenAccesBlacklistSerializer(data=request.data)
            if not serializer.is_valid():
                errors = serializer.errors
                return Response(
                    {"status": "error", "message": errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            refresh_token = serializer.validated_data["refresh"]

            user = request.user
            if user:
                token = RefreshToken(refresh_token)
                token.blacklist()
                RefreshToken.for_user(user)
                token = self.get_acces_token(request)
                tokenInBD = BlackListedTokenAccess()
                tokenInBD.token = token
                tokenInBD.user = user
                tokenInBD.save()

                return JsonResponse(
                    {"status": "success", "message": "Sesión cerrada correctamente."},
                    status=status.HTTP_200_OK,
                )
            return JsonResponse(
                {"status": "error", "message": "No existe este usuario."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
