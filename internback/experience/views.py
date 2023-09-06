from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Experience
from .serializers import ExperienceSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def create(self, request, *args, **kwargs):
        # Extract the user_id from the request data (assuming it's sent from the front end)
        user_id = request.data.get("user_id")

        # Check if the user with the given user_id exists
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this user_id does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Add the user to the request data
        modified_data = request.data.copy()
        modified_data["user"] = user.id

        serializer = self.get_serializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        # Ensure that only the owner of the experience can update it
        if instance.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Extract the user_id from the request data (assuming it's sent from the front end)
        user_id = request.data.get("user_id")

        # Check if the user with the given user_id exists
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this user_id does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Add the user to the request data
        request.data["user"] = user.id

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Ensure that only the owner of the experience can delete it
        if instance.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
