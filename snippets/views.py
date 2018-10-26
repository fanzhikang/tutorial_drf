from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.models import User
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer, UserSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)

class TagViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

