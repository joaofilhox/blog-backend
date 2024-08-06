from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'image_url', 'created_at', 'owner']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError('O título não deve estar vazio.')
        return value

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError('O conteúdo não deve estar vazio.')
        return value

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')  # Alterado para retornar o ID do usuário
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'created_at', 'user']

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError('O conteúdo do comentário não pode estar vazio.')
        return value

    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError('O post relacionado não existe.')
        return value
