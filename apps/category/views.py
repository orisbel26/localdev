from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category


class ListCategoriesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Category.objects.all().exists():
            return Response({"categories": "Test message"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "No categories found"}, status=status.HTTP_404_NOT_FOUND
        )
