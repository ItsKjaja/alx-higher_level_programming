#!/usr/bin/python3
"""square module"""


Rectangle = __import__("9-rectangle").Rectangle


"""square class"""


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """init square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.size)
