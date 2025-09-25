# Automated Reports

## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
cli/__init__.py             0      0   100%
core/__init__.py            0      0   100%
core/dice.py               16      0   100%
core/exceptions.py          4      0   100%
core/point.py              22      0   100%
pygame_ui/__init__.py       0      0   100%
-----------------------------------------------------
TOTAL                      42      0   100%

```

## Pylint Report
```text
************* Module tests.test
tests/test.py:5:0: C0305: Trailing newlines (trailing-newlines)
************* Module tests.test_point
tests/test_point.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_point.py:5:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_point.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:37:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_point.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_dice.py:5:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.dice
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/dice.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
core/dice.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
core/dice.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
core/dice.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.player
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/player.py:8:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/player.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.exceptions
core/exceptions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/exceptions.py:3:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:7:4: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module core.judge
core/judge.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/judge.py:12:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/judge.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.point
core/point.py:12:0: C0301: Line too long (114/100) (line-too-long)
core/point.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/point.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
core/point.py:30:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/point.py:37:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.backgammon
core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/backgammon.py:14:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/backgammon.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.scheduler
core/scheduler.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/scheduler.py:10:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/scheduler.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.board
core/board.py:11:0: C0301: Line too long (118/100) (line-too-long)
core/board.py:15:0: C0305: Trailing newlines (trailing-newlines)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:14:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
core/board.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module cli.cli
cli/cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/cli.py:5:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
cli/cli.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module pygame_ui.pygame_ui
pygame_ui/pygame_ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pygame_ui/pygame_ui.py:5:4: W2301: Unnecessary ellipsis constant (unnecessary-ellipsis)
pygame_ui/pygame_ui.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 5.57/10


```
