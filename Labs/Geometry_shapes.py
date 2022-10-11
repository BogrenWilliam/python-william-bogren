from __future__ import annotations
import math
from Geometry_shapes import circle
from Geometry_shapes import rectangle
from matplotlib.pyplot import plot as plt


class shapes(): # shape class is the super-class
    def __init__ (self, x_pos: (int  |float), y_pos: (int | float)):
        self.x_pos = x_pos 
        self.y_pos = y_pos 

    #def __repr__(self)
#------------------Getter/Shetter with both "X" and "Y" lines------------------#
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

    def __eq__(self, other: shapes) -> boo1:
        if self.area < other.area: 
            return True
        else: 
            return False
