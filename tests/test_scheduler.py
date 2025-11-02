import unittest
from core.scheduler import Scheduler
from core.player import Player
from core.const import black, white

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Joaco", black)
        self.player2 = Player("Pepe", white)
        self.scheduler = Scheduler(self.player1, self.player2) 

    def test_start(self):
        self.scheduler.start(self.player1)
        turn = self.scheduler.get_turn()
        self.assertEqual(turn, self.player1)

    def test_next_turn(self):
        self.scheduler.start(self.player1)
        turn1 = self.scheduler.next_turn()
        self.assertEqual(turn1, self.player2)
        turn2 = self.scheduler.next_turn()
        self.assertEqual(turn2, self.player1)

