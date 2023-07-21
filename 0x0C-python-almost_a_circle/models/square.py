#!/usr/bin/python3
"""models Square that inherits from Base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square obejct"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """print Method"""
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        st = st.format(self.id, self.x, self.y, self.width)
        return st

    def update(self, *args, **kwargs):
        """Functions to update arguments of each attribute"""
        arlist = ["id", "size", "x", "y"]
        ct = 0
        if args and len(args) != 0:
            for ar in args:
                if ct == 0:
                    super().update(ar)
                elif ct < len(arlist):
                    setattr(self, arlist(ct], ar)
                ct += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().update(id=value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of square """
        sqdic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return sqdic
