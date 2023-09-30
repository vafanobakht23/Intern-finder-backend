# views.py
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
import os
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import PersonSerializer, PersonUpdateSerializer, PhotoUploadSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .serializers import FileUploadSerializer
from rest_framework.parsers import FileUploadParser
from django.contrib.auth import logout
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(["POST"])
def signup(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
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
            return Response({"token": token.key, "user": serializer.data})
            return Response({"response": "correct Password"})
        else:
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({"message": "Logout successful"}, status=200)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            uploaded_file = serializer.validated_data["file"]
            # Save the file to the media folder (upload_to should be set in your model)
            destination_folder = "uploads/"  # Adjust as needed
            file_name = uploaded_file.name  # Use the original file name

            # Create the full file path
            file_path = os.path.join(destination_folder, file_name)

            # Save the file to the destination
            with open(file_path, "wb") as destination_file:
                for chunk in uploaded_file.chunks():
                    destination_file.write(chunk)
            # user.save()

            user.photo = "/" + os.path.join("media", file_name)
            user.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.data["id"])

    def perform_update(self, serializer):
        serializer.save()


class PersonDetailAPIView:
    queryset = User.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        return self.request.user


class PersonDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        user_id = request.query_params.get("user_id")
        try:
            # Retrieve a single user instance by ID
            user_instance = User.objects.get(id=user_id)

            # Serialize the user instance
            serializer = PersonSerializer(user_instance)

            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
