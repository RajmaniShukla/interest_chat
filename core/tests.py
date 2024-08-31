# core/tests.py
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.register_url = reverse('register')  # Adjust according to your URL pattern

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)  # Ensure one user is created

    def test_login_user(self):
        # Register a user first
        self.client.post(self.register_url, self.user_data, format='json')

        login_url = reverse('login')  # Adjust according to your URL pattern
        response = self.client.post(login_url, {
            'username': 'testuser',
            'password': 'password123'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  # Check if 'access' token is in the response
