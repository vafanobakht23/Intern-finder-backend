from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Post
        fields = "__all__"
