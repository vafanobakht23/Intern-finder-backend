from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person 
        fields = ['id', 'firstname', 'lastname', 'username', 'role', 'biography', 'photo', 'invitation_token', 'invitation_expires_at', 'is_superuser', 'created_at']


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person 
        fields = ["biography"]