from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if user with the same username already exists
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username is already taken.'}, status=status.HTTP_409_CONFLICT)

    # Create the user
    user = User.objects.create_user(username=username, password=password)

    # Generate the access token for the user
    token = Token.objects.create(user=user)

    return Response({'token': token.key, 'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request=request, username=username, password=password)

    if not user:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    login(request, user)

    # Generate or retrieve the access token for the user
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key, 'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)
