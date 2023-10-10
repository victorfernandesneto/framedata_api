from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from apps.framedata.models import Character, Move
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    """Testing the authentication system of the API"""

    def setUp(self):
        self.list_url_characters = reverse('characters-list')
        self.list_url_moves = reverse('moves-list')
        self.character = Character.objects.create(
            character_name = 'guile'
        )
        self.move = Move.objects.create(
            move_name = 'sonic boom',
            startup_frames = 'pouco',
            active_frames = 'infinitos',
            recovery_frames = 'nenhum',
            on_hit = 'combável se deus quiser',
            on_block = 'muito plus',
            cancel = 'sim',
            damage = 'muito',
            scaling = 'nenhum',
            drive_increase = 'duas barra',
            drive_decrease = 'pra caraio',
            drive_decrease_pc = 'próximo round',
            sa_increase = '3 barra de super',
            high_low = 'low',
            misc = 'golpe mais maneiro de todos',
            character = self.character
        )
        self.user = User.objects.create_user('ru10', password='ZonkNation')
        self.super_user = User.objects.create_superuser('noutize', password='bushinzo')
    
    def test_success_auth(self):
        """Test that verifies the authentication of an user with the correct credentials"""
        user = authenticate(username='ru10', password='ZonkNation')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_name_auth(self):
        """Test that verifies the authentication of an user with the wrong name"""
        user = authenticate(username='ru2', password='ZonkNation')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_password_auth(self):
        """Test that verifies the authentication of an user with the wrong password"""
        user = authenticate(username='ru10', password='ZonkKnuckle')
        self.assertFalse((user is not None) and user.is_authenticated)
    
    def test_not_auth_get_request(self):
        """Test that verifies that GET requests work without authentication"""
        response_character = self.client.get(self.list_url_characters)
        response_move = self.client.get(self.list_url_moves)
        self.assertEquals(response_character.status_code, status.HTTP_200_OK)
        self.assertEquals(response_move.status_code, status.HTTP_200_OK)
    
    def test_auth_get_request(self):
        """Test that verifies that GET requests work with authentication"""
        response_character = self.client.get(self.list_url_characters)
        response_move = self.client.get(self.list_url_moves)
        self.assertEquals(response_character.status_code, status.HTTP_200_OK)
        self.assertEquals(response_move.status_code, status.HTTP_200_OK)

    def test_not_auth_post_request(self):
        """Test that verifies that POST requests does not work without authentication"""
        character = {
            'character_name': 'poison'
        }
        golpe = {
            'startup_frames': 'insta',
            'move_name': 'flash kick',
            'active_frames': 'demais',
            'recovery_frames': 'nenhum',
            'on_hit': '5 dashes oki',
            'on_block': 'safe',
            'cancel': 'em todos os super',
            'damage': 'próximo round',
            'scaling': 'dale',
            'drive_increase': '?',
            'drive_decrease': 'burnout',
            'drive_decrease_pc': 'burnout pra dois round',
            'sa_increase': '3 barra de super',
            'high_low': 'overhead',
            'misc': 'pule nao papai',
            'character': self.character
        }
        response_characters = self.client.post(self.list_url_characters, character)
        response_moves = self.client.post(self.list_url_moves, golpe)
        self.assertEquals(response_characters.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(response_moves.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_basic_auth_post_request(self):
        """Test that verifies that POST requests does not work with basic authentication"""
        self.client.force_authenticate(self.user)
        character = {
            'character_name': 'poison'
        }
        golpe = {
            'startup_frames': 'insta',
            'move_name': 'flash kick',
            'active_frames': 'demais',
            'recovery_frames': 'nenhum',
            'on_hit': '5 dashes oki',
            'on_block': 'safe',
            'cancel': 'em todos os super',
            'damage': 'próximo round',
            'scaling': 'dale',
            'drive_increase': '?',
            'drive_decrease': 'burnout',
            'drive_decrease_pc': 'burnout pra dois round',
            'sa_increase': '3 barra de super',
            'high_low': 'overhead',
            'misc': 'pule nao papai',
            'character': self.character
        }
        response_characters = self.client.post(self.list_url_characters, character)
        response_moves = self.client.post(self.list_url_moves, golpe)
        self.assertEquals(response_characters.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(response_moves.status_code, status.HTTP_403_FORBIDDEN)

    def test_super_user_auth_post_request(self):
        """Test that verifies that POST requests does work with super user authentication"""
        self.client.force_authenticate(self.super_user)
        character = {
            'character_name': 'poison'
        }
        golpe = {
            'startup_frames': 'insta',
            'move_name': 'flash kick',
            'active_frames': 'demais',
            'recovery_frames': 'nenhum',
            'on_hit': '5 dashes oki',
            'on_block': 'safe',
            'cancel': 'em todos os super',
            'damage': 'próximo round',
            'scaling': 'dale',
            'drive_increase': '?',
            'drive_decrease': 'burnout',
            'drive_decrease_pc': 'burnout pra dois round',
            'sa_increase': '3 barra de super',
            'high_low': 'overhead',
            'misc': 'pule nao papai',
            'character': self.character
        }
        response_characters = self.client.post(self.list_url_characters, character)
        response_moves = self.client.post(self.list_url_moves, golpe)
        self.assertEquals(response_characters.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response_moves.status_code, status.HTTP_201_CREATED)