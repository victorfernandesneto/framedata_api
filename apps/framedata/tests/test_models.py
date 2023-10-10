from django.test import TestCase
from apps.framedata.models import Character, Move

class CharacterModelTestCase(TestCase):

    def setUp(self):
        self.character = Character(
            character_name = 'poison'
        )
    
    def test_verify_character(self):
        """Test that verifies if the character model is correct"""
        self.assertEquals(self.character.character_name, 'poison')

class MoveModelTestCase(TestCase):

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
    def test_verify_move(self):
        """Test that verifies if the move model is correct"""
        self.assertEquals(self.move.move_name, 'sonic boom')
        self.assertEquals(self.move.startup_frames, 'pouco')
        self.assertEquals(self.move.active_frames, 'infinitos')
        self.assertEquals(self.move.recovery_frames, 'nenhum')
        self.assertEquals(self.move.on_hit, 'combável se deus quiser')
        self.assertEquals(self.move.on_block, 'muito plus')
        self.assertEquals(self.move.cancel, 'sim')
        self.assertEquals(self.move.damage, 'muito')
        self.assertEquals(self.move.scaling, 'nenhum')
        self.assertEquals(self.move.drive_increase, 'duas barra')
        self.assertEquals(self.move.drive_decrease, 'pra caraio')
        self.assertEquals(self.move.drive_decrease_pc, 'próximo round')
        self.assertEquals(self.move.sa_increase, '3 barra de super')
        self.assertEquals(self.move.high_low, 'low')
        self.assertEquals(self.move.misc, 'golpe mais maneiro de todos')
        self.assertEquals(self.move.character, self.character)