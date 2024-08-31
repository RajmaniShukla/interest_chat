from django.urls import path
from .views import RegisterView, LoginView, InterestView, MessageView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('interests/', InterestView.as_view(), name='interests'),
    path('messages/', MessageView.as_view(), name='messages'),
]
