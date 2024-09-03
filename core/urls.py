from django.urls import path
from .views import RegisterView, LoginView, InterestView, MessageView, InterestReceived, InterestUpdate, MessageReceived

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('interests/', InterestView.as_view(), name='interests'),
    path('interests/received/', InterestReceived.as_view(), name='interestsReceived'),
    path('interests/<int:pk>/update/', InterestUpdate.as_view(), name='interestsUpdate'),
    path('messages/', MessageView.as_view(), name='messages'),
    path('messages/received/', MessageReceived.as_view(), name='messagesReceived'),
]
