from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Exam
from post.models import Post
from .serializers import ExamSerializer
import pdb
from django.contrib.auth import get_user_model
import json


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


def create(self, request, *args, **kwargs):
    # Extract the post_id from the request data (assuming it's sent from the front end)
    post_id = request.data.get("post")

    # Check if the post with the given post_id exists
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(
            {"detail": "Post with this post_id does not exist."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Check if an exam with the same post_id already exists for this post
    if Exam.objects.filter(post=post_id).exists():
        return Response(
            {"detail": "An exam for this post already exists."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Deserialize the content array directly
    content_data = request.data.get("content", [])

    # Create an Exam object with the deserialized content
    exam = Exam(post=post, content=content_data)
    exam.save()

    # Serialize the Exam object to respond with the saved content
    serializer = self.get_serializer(exam)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        post_id = request.data.get("post_id")

        # Check if the user with the given user_id exists
        try:
            post = Post.objects.get(pk=post_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this user_id does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExamListViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
