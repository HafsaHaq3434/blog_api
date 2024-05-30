from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
