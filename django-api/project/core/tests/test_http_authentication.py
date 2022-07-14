from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

"""

ALL TEST SHOUD BE WORKING WITH PYTEST - NOW ITS TESTET WITH DJANGO TEST BUT PLEASE REWRITE

"""

PASSWORD = 'pAssw0rd!'

def create_user(username='hans', password=PASSWORD, phone_number="0176827381"):
    return get_user_model().objects.create_user(
        username=username, password=password, phone_number=phone_number)

class AuthenticationTest(APITestCase):


    def test_user_can_sign_up(self):

        response = self.client.post(reverse('sign_up'), data={
            'username': 'peter0',
            'phone_number': '0176830291880',
            'password': PASSWORD,
            'password_confirm': PASSWORD,
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['phone_number'], user.phone_number)


    def test_user_can_log_in(self):
        user = create_user()
        response = self.client.post(reverse('log_in'), data={
            'username': user.username,
            'password': PASSWORD,
        })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['username'], user.username)

    def test_user_can_log_out(self):
        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)
        response = self.client.post(reverse('log_out'))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

