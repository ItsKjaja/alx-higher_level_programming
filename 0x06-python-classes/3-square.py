#!/usr/bin/python3

"""Square module."""


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """Constructor

           Args:
               size: size of square.

         Raises:
             TypeError: size is not integer.
             ValueError: if size less than 0.
       """
       if not isinstance(size, int):
           raise TypeError("size must be an integer")
       if size < 0:
           raise ValueError("size must be >= 0")

       self.__size = size

    def area(self):
        """Area of square

           Returns:
               size of square.

        """
        return self.__size **2
