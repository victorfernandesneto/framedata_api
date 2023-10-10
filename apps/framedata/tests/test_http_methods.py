# from rest_framework.test import APITestCase
# from apps.framedata.models import Character, Move
# from django.urls import reverse
# from rest_framework import status

# class CharacterTestCase(APITestCase):
    
#     def setUp(self):
#         self.list_url = reverse('characters-list')
#         self.character = Character.objects.create(
#             character_name = 'teste1'
#         )

#     def test_request_get_character(self):
#         """Verifying if the GET request is working for characters"""
#         response = self.client.get(self.list_url)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)

#     def test_request_post_character(self):
#         """Verifying if the POST request is unauthorized for characters"""
#         character = {
#             'character_name': 'poison'
#         }
#         response = self.client.post(self.list_url, character)
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_request_delete_character(self):
#         """Verifying if the DELETE request is unauthorized for characters"""
#         response = self.client.delete('/characters/1/')
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_request_put_character(self):
#         """Verifying if the PUT request is unauthorized for characters"""
#         character = {
#             'character_name': 'poison'
#         }
#         response = self.client.put('/characters/1/', character)
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

# class MoveTestCase(APITestCase):
    
#     def setUp(self):
#         self.list_url = reverse('moves-list')
#         self.character = Character.objects.create(
#             character_name = 'guile'
#         )
#         self.move = Move.objects.create(
#             move_name = 'sonic boom',
#             startup_frames = 'pouco',
#             active_frames = 'infinitos',
#             recovery_frames = 'nenhum',
#             on_hit = 'combável se deus quiser',
#             on_block = 'muito plus',
#             cancel = 'sim',
#             damage = 'muito',
#             scaling = 'nenhum',
#             drive_increase = 'duas barra',
#             drive_decrease = 'pra caraio',
#             drive_decrease_pc = 'próximo round',
#             sa_increase = '3 barra de super',
#             high_low = 'low',
#             misc = 'golpe mais maneiro de todos',
#             character = self.character
#         )

#     def test_request_get_move(self):
#         """Verifying if the GET request is working for characters"""
#         response = self.client.get(self.list_url)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)

#     def test_request_post_move(self):
#         """Verifying if the POST request is unauthorized for moves"""
#         golpe = {
#             'startup_frames': 'insta',
#             'move_name': 'flash kick',
#             'active_frames': 'demais',
#             'recovery_frames': 'nenhum',
#             'on_hit': '5 dashes oki',
#             'on_block': 'safe',
#             'cancel': 'em todos os super',
#             'damage': 'próximo round',
#             'scaling': 'dale',
#             'drive_increase': '?',
#             'drive_decrease': 'burnout',
#             'drive_decrease_pc': 'burnout pra dois round',
#             'sa_increase': '3 barra de super',
#             'high_low': 'overhead',
#             'misc': 'pule nao papai',
#             'character': self.character
#         }
#         response = self.client.post(self.list_url, golpe)
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_request_delete_move(self):
#         """Verifying if the DELETE request is unauthorized for moves"""
#         response = self.client.delete('/moves/1/')
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_request_put_move(self):
#         """Verifying if the PUT request is unauthorized for moves"""
#         golpe = {
#             'startup_frames': 'insta',
#             'move_name': 'flash kick',
#             'active_frames': 'demais',
#             'recovery_frames': 'nenhum',
#             'on_hit': '5 dashes oki',
#             'on_block': 'safe',
#             'cancel': 'em todos os super',
#             'damage': 'próximo round',
#             'scaling': 'dale',
#             'drive_increase': '?',
#             'drive_decrease': 'burnout',
#             'drive_decrease_pc': 'burnout pra dois round',
#             'sa_increase': '3 barra de super',
#             'high_low': 'overhead',
#             'misc': 'pule nao papai',
#             'character': self.character
#         }
#         response = self.client.put('/moves/1/', golpe)
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)