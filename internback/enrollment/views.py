# views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializers import EnrollmentSerializer
from rest_framework.response import Response
from person.models import Person
from post.models import Post
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.db.models import Q

User = get_user_model()


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def create(self, request, *args, **kwargs):
        # Customize the create behavior if necessary
        post_id = request.data.get("post_id")
        user_id = request.data.get("user_id")
        # Check if the post with the given post_id exists
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post with this post_id does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this user_id does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            is_post_founded = Q(post_id=post_id)
            is_user_founded = Q(user_id=user_id)
            founder_res = Enrollment.objects.filter(is_post_founded & is_user_founded)
            if founder_res.exists():
                return Response(
                    {"detail": "You can't apply for this post"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Enrollment.DoesNotExist:
            return Response(
                {"detail": "You can't apply for this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        modified_data = request.data.copy()
        modified_data["user"] = user.id
        modified_data["post"] = post.id
        serializer = self.get_serializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        # Customize the update behavior if necessary
        serializer.save()

    def perform_destroy(self, instance):
        # Customize the delete behavior if necessary
        instance.delete()


class EnrollmentListViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentPerUserViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.query_params.get("user_id")
        queryset = Enrollment.objects.filter(user=user_id)
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(serializer.data)


class CombinedEnrollmentListView(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = request.query_params.get("user_id")
            # Perform a join query to retrieve enrollments and related posts for a specific user
            combined_data = Enrollment.objects.filter(user=user_id).values(
                "id",
                "status",
                "answers",
                "user_id",
                "post__id",
                "post__title",
                "post__category",
                "post__description",
                "post__created_at",
            )

            return Response(combined_data)

        except Person.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)
