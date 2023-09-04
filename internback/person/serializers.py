from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person 
        fields = "__all__"


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person 
        fields = "__all__"