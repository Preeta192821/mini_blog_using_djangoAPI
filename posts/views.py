# posts/views.py
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






