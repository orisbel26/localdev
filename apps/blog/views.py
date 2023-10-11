from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.category.models import Category

from .models import Post, ViewCount
from .serializers import PostSerializer


class PostListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.objects.all().exists():
            print("list_post")
            return Response({"posts": "test message"}, status=status.HTTP_200_OK)
        return Response({"error": "No post found"}, status=status.HTTP_404_NOT_FOUND)
