#!/usr/bin/python3
""" Square class: child class of Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """ Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """ Print rectangle object """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id,
            self.x, self.y, self.width
            )

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update object atrributes with contents of args """
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for attr, value in kwargs.items():
                self.__setattr__(attr, value)
            return

    def to_dictionary(self):
        """ Rturns dictionary representation """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'size': getattr(self, "size")}
