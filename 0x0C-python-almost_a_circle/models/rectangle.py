#!/usr/bin/python3
"""rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle shape class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """init class function
        Args:
            width: width of rectangle
            height: height of rectangle
            x: position x
            y: position y
            id: id of rectangle
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """display rectangle shape"""
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        text = "[Rectangle] ({}) {}/{} - {}/{}"
        return text.format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """ display rectangle width height and x, y"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def to_dictionary(self):
        """return dict of rectangle class """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        def update(self, *args, **kwargs):
            """ update class args """
            if len (args) == 0:
                for key, value in kwargs.items():
                    self.__setattr__(key, value)
                return
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError
                pass
