class NotImplementedStatus(Exception):
    """Not implemented status for handler"""

    def __init__(self, text: str) -> None:
        self.text = text
