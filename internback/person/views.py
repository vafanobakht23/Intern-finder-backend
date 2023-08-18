# views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from .serializers import PersonSerializer
from django.contrib.auth.hashers import check_password
# from ..services import PersonService

from django.contrib.auth import get_user_model
User = get_user_model()
# class PersonRegistrationView(RetrieveUpdateDestroyAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     http_method_names = ["get", "patch", "delete", "options"]
#     serializer_class = PersonSerializer
#     lookup_field = "invitation_token"
#     queryset = Person.objects
#     person_service: PersonService = None

#     def get_object(self):
#         user = super().get_object()
#         self.person_service.validate_user_before_registration(user)
#         return user

#     def perform_destroy(self, instance):
#         print("vaafaa")
        
#     def perform_update(self, serializer: UserSerializer):
#         user = serializer.save()
#         self.person_service.register_user(user)

# class UserCreateView(CreateAPIView):
#     permission_classes = []
#     http_method_names = ["post", "options"]
#     person_service: PersonService = None

#     def perform_create(self, serializer):
#         user = serializer.save()
#         self.person_service.invite_user(user)

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

@api_view(['POST'])
def login(request):
    user = User.objects.get(username=request.data['username'])
    if check_password(request.data['password'],user.password):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = PersonSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
# @api_view(['POST'])
# def user_login(request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = None
#         if '@' in email:
#             try:
#                 user = Person.objects.get(email=email)
#             except ObjectDoesNotExist:
#                 pass

#         if not user:
#             user = authenticate(email=email, password=password)

#         if user:
#             token, _ = Token.objects.get(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class user_login(ObtainAuthToken):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = [IsAuthenticated]
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['person']
#         token = Token.objects.get(user=user)
#         return Response({
#             'token': token.key,
#             'id': user.pk,
#             'username': user.username
#         })