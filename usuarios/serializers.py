from rest_framework import serializers
from .models import Usuario
from rest_framework.validators import UniqueValidator

class UsuarioSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False, allow_blank=True)  # Adicionando o campo bio

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'is_superuser', 'email', 'profile_image', 'bio']  # Adicionando bio aos campos
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8  
            }
        }

    def create(self, validated_data):
        if validated_data.get('is_superuser', False):
            usuario = Usuario.objects.create_superuser(**validated_data)
        else:
            usuario = Usuario.objects.create_user(**validated_data)
        return usuario       

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
