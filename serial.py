class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial generator instance."""
        self.start = start
        self.currentNum = start

    def __repr__(self):
        """Return representation of serial generator instance."""
        return f"<SerialGenerator start={self.start} currentNum={self.currentNum}>"

    def generate(self):
        """Return next sequential number and increment self.currentNumber."""
        self.currentNum += 1
        return self.currentNum - 1

    def reset(self):
        """Reset current number to self.start."""
        self.currentNum = self.start