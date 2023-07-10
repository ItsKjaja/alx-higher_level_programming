#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init_(self.__size, self.__size)
