from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "thumbnail",
            "excerpt",
            "description",
            "time_read",
            "published",
            "views",
        ]
