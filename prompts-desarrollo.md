## Promt 15/10
### Promt:
![Imagen de avante neovim][./screenshots/image.png]
### Codigo:
``` python
    def setUp(self):

    def test_start_game(self):
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        board = Board()
        dice = Dice()
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        result, starter_player = game.start_game()

        self.assertIn(player1.name, result)
        self.assertIn(player2.name, result)
        self.assertNotEqual(result[player1.name], result[player2.name])
        self.assertIn(starter_player, [player1, player2])

    def test_trow_dice(self):
        dice = Dice()
        board = Board()
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        dice_values = game.trow_dice()
        self.assertEqual(len(dice_values), 2)
        self.assertTrue(all(1 <= value <= 6 for value in dice_values))

    def test_is_checker_on_bar(self):
        board = Board()
        dice = Dice()
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        self.assertFalse(game.is_checker_on_bar())  # Assuming no checkers are on the bar initially

    def test_get_board_state(self):
        board = Board()
        dice = Dice()
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        board_state = game.get_board_state()
        self.assertIsInstance(board_state, list)

    def test_move_from_bar(self):
        board = Board()
        dice = Dice()
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        # Assuming the board and dice are set up for this test
        game.move_from_bar(0)  # Replace 0 with the index of the dice to use

    def test_move(self):
        board = Board()
        dice = Dice()
        player1 = Player("Player 1", black)
        player2 = Player("Player 2", white)
        scheduler = Scheduler(player1, player2)
        judge = None  # Replace with a mock or actual Judge instance if needed
        game = Backgammon(player1, player2, board, dice, scheduler, judge)

        # Assuming the board and dice are set up for this test
        game.move(0, 0)  # Replace 0, 0 with the actual positions and dice index

```
## 20/10
[Link al chat de copilot][https://github.com/copilot/share/4a1850a6-4384-8c83-9911-424c4019080c]
