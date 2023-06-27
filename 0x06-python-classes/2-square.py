#!/usr/bin/python3

"""Square module"""



class Square:
    """ square class """
    def __init__(self, size=0):
        """Constructor
            Args:
               size: size of square
            Raises:
                TypeError: size is not integer
                ValueError: size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
