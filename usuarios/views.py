from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Usuario
from .serializers import UsuarioSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a list of users",
        description="Returns a list of all users.",
        responses={200: UsuarioSerializer(many=True)}
    ),
    post=extend_schema(
        summary="Create a new user",
        description="Creates a new user with the provided data.",
        request=UsuarioSerializer,
        responses={201: UsuarioSerializer}
    ),
)
class UsuarioListCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@extend_schema_view(
    get=extend_schema(
        summary="Retrieve a specific user",
        description="Returns the details of a specific user.",
        responses={200: UsuarioSerializer}
    ),
    put=extend_schema(
        summary="Update a specific user",
        description="Updates the details of a specific user.",
        request=UsuarioSerializer,
        responses={200: UsuarioSerializer}
    ),
    delete=extend_schema(
        summary="Delete a specific user",
        description="Deletes a specific user.",
        responses={204: None}
    ),
)
class UsuarioRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
