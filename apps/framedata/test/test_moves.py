from rest_framework.test import APITestCase
from apps.framedata.models import Character, Move
from django.urls import reverse
from rest_framework import status

class CharacterTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('moves-list')
        self.character_1 = Character.objects.create(
            character_name = 'guile'
        )
        self.move_1 = Move.objects.create(
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
            character = self.character_1
        )
    # def test_fail(self):
    #     self.fail('falhou rapazes')

    def test_request_get_move(self):
        """Verifying if the GET request is working for characters"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_move(self):
        """Verifying if the POST request is working for characters"""
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
            'character': self.character_1
        }
        response = self.client.post(self.list_url, golpe)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_delete_character(self):
        """Verifying if the DELETE request is working for characters"""
        response = self.client.delete('/moves/1/')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_put_character(self):
        """Verifying if the PUT request is working for characters"""
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
            'character': self.character_1
        }
        response = self.client.put('/moves/1/', golpe)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)