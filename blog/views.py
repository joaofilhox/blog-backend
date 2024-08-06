from rest_framework import status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Post, Comment
from drf_spectacular.utils import extend_schema
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer()},
        summary="Create post",
        description="Endpoint to create a new post."
    )
    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None, 404: 'Not Found'},
        summary="Delete post",
        description="Endpoint to delete a specific post by ID."
    )
    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        responses={200: PostSerializer(many=True)},
        summary="List posts",
        description="Endpoint to list all posts."
    )
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        responses={200: PostSerializer(), 404: 'Not Found'},
        summary="Retrieve post",
        description="Endpoint to retrieve a specific post by ID."
    )
    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        request=PostSerializer,
        responses={200: PostSerializer(), 400: 'Bad Request', 404: 'Not Found'},
        summary="Update post",
        description="Endpoint to update an existing post's title and content."
    )
    def update(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer()},
        summary="Create comment",
        description="Endpoint to create a comment on a specific post."
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            post = Post.objects.get(id=request.data.get('post'))
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer.save(post=post, user=request.user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        responses={200: CommentSerializer(many=True)},
        summary="List comments",
        description="Endpoint to list all comments."
    )
    def list(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        responses={200: CommentSerializer(), 404: 'Not Found'},
        summary="Retrieve comment",
        description="Endpoint to retrieve a specific comment by ID."
    )
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=CommentSerializer, 
        responses={200: CommentSerializer()},
        summary="Update comment",
        description="Endpoint to update the content of a comment."
    )
    def update(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        responses={204: None},
        summary="Delete comment",
        description="Endpoint to delete a comment."
    )
    def destroy(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
