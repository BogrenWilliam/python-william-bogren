from __future__ import annotations # |-operator
from curses import BUTTON1_DOUBLE_CLICKED
import math
from Geometry_shapes import circle
from Geometry_shapes import rectangle
from matplotlib.pyplot import plot as plt

# Jag har haft en del svårigheter med denna labb, då jag tyckt det varit svårt att ens nå mina mål och utföra den.
# Dessutom har den stått stilla en del kring vissa classes osv, därav källkoden ser ut som den gör! (komplettering förhoppningsvis, tack!)

class shapes(): # shape class is the super-class
    def __init__ (self, x_pos: (int  |float), y_pos: (int | float)):
        self.x_pos = x_pos 
        self.y_pos = y_pos 

    #def __repr__(self)
#------------------Getter/Shetter and properties------------------#
    @property
    def x_pos(self):
        return self._x_pos

    @property 
    def y_pos(self): 
        return self._y_pos

    @x_pos.setter
    def x_pos(self, value: float):
        if not isinstance(value, (float, int)): # Using "isinstance" instead for "type()" because the function isinstance let me to check if an object partin to a class/subclass. type cant do this move #
            raise TypeError(f"float or int, not {type(value)}")
        self._x_pos = value 
        
    @y_pos.setter
    def y_pos(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"float or int, not {type(value)}")
        self._y_pos = value 

    def __1t__(self, other: shapes) -> boo1:  # Overloader
        if self.area < other.area: 
            return True
        else: 
            return False
    
    def __le__(self, other: shapes) -> boo1: # Overloaders
        if self.area <= other.area: 
            return True
        else: 
            return False
        
    def __gt__(self, other: shapes) -> boo1: # Overloaders
        if self.area > other.area:
            return True
        else: 
            return False

    def __ge__(self, other: shapes) -> boo1: # Overloaders
        if self.area >= other.area:
            return True
        else: 
            return False

    #----------Rectangle-------------------#
    class rectangle():
        def __init__(
        self, x: float = 0, y: float = 0, width: float = 1, height: float = 1
    ) -> None:
        """Init method for Rectangle class. Adds two required paramters: width and height"""
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.x_0 = self._x - self._width / 2
        self.x_1 = self._x + self._width / 2
        self.y_0 = self._y - self._height / 2
        self.y_1 = self._y + self._height / 2

   #-------properties------------------------# 

    @property 
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = self.check_measurement(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = self.check_measurement(value)


