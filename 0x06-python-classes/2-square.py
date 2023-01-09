#!/usr/bin/python3


"""Define a class Square."""


class Square: 
    '''Class Square object intialized with size'''
    def __init__(self, size=0):
        '''init method of class Square'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of the square"""
        return (self.___size * self.__size)
