from rest_framework import serializers
from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Exam
        fields = "__all__"
