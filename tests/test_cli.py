import unittest
from cli.cli import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
