class InvalidMove(Exception):
    """Exception raised for invalid moves in the game."""
    pass

class NoCheckers(Exception):
    """Exception raised when attempting to remove a checker from an empty point."""
    pass


class OmitTurn(Exception):
    pass
