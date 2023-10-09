from rest_framework.test import APITestCase
from apps.framedata.models import Character
from django.urls import reverse
from rest_framework import status

class CharacterTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('characters-list')
        self.curso_1 = Character.objects.create(
            character_name = 'teste1'
        )
        self.curso_2 = Character.objects.create(
            character_name = 'teste2'
        )

    # def test_fail(self):
    #     self.fail('falhou rapazes')

    def test_request_get_character(self):
        """Verifying if the GET request is working for characters"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_character(self):
        """Verifying if the POST request is working for characters"""
        character = {
            'character_name': 'poison'
        }
        response = self.client.post(self.list_url, character)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_delete_character(self):
        """Verifying if the DELETE request is working for characters"""
        response = self.client.delete('/characters/1/')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_put_character(self):
        """Verifying if the PUT request is working for characters"""
        character = {
            'character_name': 'poison'
        }
        response = self.client.put('/characters/1/', character)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)