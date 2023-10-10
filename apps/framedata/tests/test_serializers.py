from django.test import TestCase
from apps.framedata.models import Character, Move
from apps.framedata.serializer import CharacterSerializer, MoveSerializer

class CharacterSerializerTestCase(TestCase):
    
    def setUp(self):
        self.character = Character(
            character_name = 'poison'
        )
        self.serializer = CharacterSerializer(instance=self.character)
    
    def test_character_serialized_fields(self):
        """Test that verifies if the character serializer is correct"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['character_name', 'id']))
    
    def test_character_serialized_content(self):
        """Test that verifies if the character serializer content is correct"""
        data = self.serializer.data
        self.assertEqual(data['character_name'], self.character.character_name)

class MoveSerializerTestCase(TestCase):

    def setUp(self):
        self.character = Character(
            character_name = 'guile'
        )
        self.move = Move(
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
        self.serializer = MoveSerializer(instance=self.move)
    
    def test_move_serialized_fields(self):
        """Test that verifies if the move serializer is correct"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['move_name', 'startup_frames', 'active_frames', 'recovery_frames', 'on_hit', 'on_block', 'cancel', 'damage', 'scaling', 'drive_increase', 'drive_decrease', 'drive_decrease_pc', 'sa_increase', 'high_low', 'misc', 'character', 'id']))
    
    def test_move_serialized_content(self):
        """Test that verifies if the move serializer content is correct"""
        data = self.serializer.data
        self.assertEqual(data['move_name'], self.move.move_name)
        self.assertEqual(data['startup_frames'], self.move.startup_frames)
        self.assertEqual(data['active_frames'], self.move.active_frames)
        self.assertEqual(data['recovery_frames'], self.move.recovery_frames)
        self.assertEqual(data['on_hit'], self.move.on_hit)
        self.assertEqual(data['on_block'], self.move.on_block)
        self.assertEqual(data['cancel'], self.move.cancel)
        self.assertEqual(data['damage'], self.move.damage)
        self.assertEqual(data['scaling'], self.move.scaling)
        self.assertEqual(data['drive_increase'], self.move.drive_increase)
        self.assertEqual(data['drive_decrease'], self.move.drive_decrease)
        self.assertEqual(data['drive_decrease_pc'], self.move.drive_decrease_pc)
        self.assertEqual(data['sa_increase'], self.move.sa_increase)
        self.assertEqual(data['high_low'], self.move.high_low)
        self.assertEqual(data['misc'], self.move.misc)
        self.assertEqual(data['character'], self.move.character.character_name)
        self.assertEqual(data['id'], self.move.id)