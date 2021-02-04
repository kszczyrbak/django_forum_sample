from rest_framework import viewsets, views
from .models import Section, Post, Thread, User
from .serializers import UserSerializer, ThreadSerializer, PostSerializer, SectionSerializer
from rest_framework.permissions import IsAuthenticated

# TODO: solve n+1 (prefetch)


class SectionViewset(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class ThreadViewset(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
