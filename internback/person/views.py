# views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import PersonSerializer,PersonUpdateSerializer
from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth import get_user_model
User = get_user_model()

@api_view(['POST'])
def signup(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

class login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if username is None or password is None:
            return Response({"response": "Invalid data"})
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            serializer = PersonSerializer(user)
            return Response({'token': token.key, 'user': serializer.data})
            return Response({"response": "correct Password"})
        else:
           return Response("missing user", status=status.HTTP_404_NOT_FOUND)
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = User.objects.get(pk=pk)
        serializer = PersonSerializer(user)
        return Response(serializer.data)
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(pk=self.request.data['id'])

    def perform_update(self, serializer):
        serializer.save()

class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        return self.request.user

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")