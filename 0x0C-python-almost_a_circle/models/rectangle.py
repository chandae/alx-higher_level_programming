#!/usr/bin/python3
""" Base Class Child Class: Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """ Constructor """
        super().__init__(id)
        # Perform data validations
        self.valid('width', width)
        self.valid('height', height)
        self.valid('x', x, True)
        self.valid('y', y, True)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """ Print rectangle object """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width, self.height
            )

    @property
    def width(self):
        """ Width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width public setter method """
        self.valid('width', value)
        self.__width = value

    @property
    def height(self):
        """ Height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height public setter method """
        self.valid('height', value)
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x public setter method """
        self.valid('x', value, True)
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y public setter method """
        self.valid('y', value, True)
        self.__y = value

    def update(self, *args, **kwargs):
        """ Update object atrributes with contents of args """
        if args:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for attr, value in kwargs.items():
                self.__setattr__(attr, value)
            return

    def area(self):
        """ Return rectangle area """
        return self.__width * self.__height

    def display(self, char='#'):
        """ Print rectangle to stdout """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x + self.width * char)

    def to_dictionary(self):
        """ Return dictionary representation of object """
        return {
            'x': getattr(self, "x"), 'y': getattr(self, "y"),
            'id': getattr(self, "id"), 'height': getattr(self, "height"),
            'width': getattr(self, "width")}

    def valid(self, name, value, greater_equal=False):
        """ Check if input is an integer """
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
