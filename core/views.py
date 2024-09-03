from django.dispatch import receiver
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, TokenSerializer, InterestSerializer, MessageSerializer
from .models import Interest, Message
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class LoginView(generics.GenericAPIView):
    serializer_class = TokenSerializer

    def post(self, request):
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=400)

class InterestView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class InterestReceived(generics.GenericAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        interests = Interest.objects.filter(receiver=self.request.user)
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)
    
class InterestUpdate(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]
    

class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageReceived(generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        messages = Message.objects.filter(receiver=self.request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)