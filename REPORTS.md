# Automated Reports

## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
cli/__init__.py             0      0   100%
core/__init__.py            0      0   100%
core/backgammon.py         52     32    38%   22-27, 30, 33, 36-38, 44-51, 54, 57, 60, 63, 70-74, 81-83, 86
core/board.py              29      3    90%   40-42
core/const.py               2      0   100%
core/dice.py               19      0   100%
core/exceptions.py          4      0   100%
core/judge.py               1      0   100%
core/player.py             17      1    94%   13
core/point.py              27      0   100%
core/scheduler.py          13      0   100%
pygame_ui/__init__.py       0      0   100%
-----------------------------------------------------
TOTAL                     164     36    78%

```

## Pylint Report
```text
************* Module tests.test_scheduler
tests/test_scheduler.py:10:62: C0303: Trailing whitespace (trailing-whitespace)
tests/test_scheduler.py:23:0: C0305: Trailing newlines (trailing-newlines)
tests/test_scheduler.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_scheduler.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_scheduler.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_scheduler.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_player
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:5:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_backgammon
tests/test_backgammon.py:48:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammon.py:1:0: W0611: Unused import unittest (unused-import)
tests/test_backgammon.py:2:0: W0611: Unused Scheduler imported from core.scheduler (unused-import)
tests/test_backgammon.py:3:0: W0611: Unused Player imported from core.player (unused-import)
tests/test_backgammon.py:4:0: W0611: Unused black imported from core.const (unused-import)
tests/test_backgammon.py:4:0: W0611: Unused white imported from core.const (unused-import)
tests/test_backgammon.py:5:0: W0611: Unused Backgammon imported from core.backgammon (unused-import)
************* Module tests.test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_dice.py:5:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_point
tests/test_point.py:48:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_point.py:54:0: C0305: Trailing newlines (trailing-newlines)
tests/test_point.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_point.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_point.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:13:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_board
tests/test_board.py:62:0: C0305: Trailing newlines (trailing-newlines)
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:10:8: W0212: Access to a protected member _Board__bar of a client class (protected-access)
tests/test_board.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:16:14: W0212: Access to a protected member _Board__bar of a client class (protected-access)
tests/test_board.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:45:4: E0102: method already defined line 15 (function-redefined)
tests/test_board.py:52:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.judge
core/judge.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/judge.py:12:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/judge.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.point
core/point.py:13:0: C0301: Line too long (114/100) (line-too-long)
core/point.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/point.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:36:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/point.py:44:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:2:0: W0611: Unused black imported from core.const (unused-import)
core/point.py:2:0: W0611: Unused white imported from core.const (unused-import)
************* Module core.const
core/const.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/const.py:1:0: C0103: Constant name "black" doesn't conform to UPPER_CASE naming style (invalid-name)
core/const.py:2:0: C0103: Constant name "white" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module core.scheduler
core/scheduler.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
core/scheduler.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/scheduler.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
core/scheduler.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
core/scheduler.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.board
core/board.py:3:39: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:42:52: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:10:8: C0103: Attribute name "_Board__bar" doesn't conform to snake_case naming style (invalid-name)
core/board.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:42:12: W0707: Consider explicitly re-raising using 'except Exception as exc' and 'raise InvalidMove('Movimiento invalido') from exc' (raise-missing-from)
core/board.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:51:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.exceptions
core/exceptions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/exceptions.py:3:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:7:4: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module core.player
core/player.py:12:45: C0303: Trailing whitespace (trailing-whitespace)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/player.py:12:11: R1714: Consider merging these comparisons with 'in' by using 'color not in (black, white)'. Use a set instead if elements are hashable. (consider-using-in)
core/player.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
core/player.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
core/player.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
core/player.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.dice
core/dice.py:41:19: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.backgammon
core/backgammon.py:1:30: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon.py:18:0: C0301: Line too long (122/100) (line-too-long)
core/backgammon.py:25:35: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon.py:27:30: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:53:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:71:12: W0719: Raising too general exception: Exception (broad-exception-raised)
core/backgammon.py:73:8: W0612: Unused variable 'dice_numbers' (unused-variable)
core/backgammon.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
core/backgammon.py:24:8: W0238: Unused private member `Backgammon.__judge` (unused-private-member)
************* Module cli.cli
cli/cli.py:52:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:131:0: C0301: Line too long (103/100) (line-too-long)
cli/cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/cli.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
cli/cli.py:21:12: C0206: Consider iterating with .items() (consider-using-dict-items)
cli/cli.py:20:20: W0612: Unused variable 'starter' (unused-variable)
cli/cli.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
cli/cli.py:48:15: W0718: Catching too general exception Exception (broad-exception-caught)
cli/cli.py:43:16: W0612: Unused variable 'i' (unused-variable)
cli/cli.py:53:4: C0116: Missing function or method docstring (missing-function-docstring)
cli/cli.py:55:8: C0104: Disallowed name "bar" (disallowed-name)
cli/cli.py:53:4: R0912: Too many branches (17/12) (too-many-branches)
cli/cli.py:53:4: R0915: Too many statements (56/50) (too-many-statements)
cli/cli.py:3:0: C0411: standard import "time.sleep" should be placed before first party imports "core.backgammon.Backgammon", "core.const.black"  (wrong-import-order)
************* Module cli.__main__
cli/__main__.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module pygame_ui.pygame_ui
pygame_ui/pygame_ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pygame_ui/pygame_ui.py:5:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
pygame_ui/pygame_ui.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 6.99/10


```
