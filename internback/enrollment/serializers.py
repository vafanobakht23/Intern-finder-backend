from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Enrollment
        fields = "__all__"
