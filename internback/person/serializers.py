from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person
        fields = [
            "id",
            "firstname",
            "lastname",
            "username",
            "role",
            "biography",
            "photo",
            "title",
            "university",
            "address",
            "created_at",
            "activation_code",
        ]


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person
        fields = "__all__"


class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["photo"]


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        model = Person
        fields = (
            "id",
            "photo",
        )
