#!/usr/bin/python3

"""define a class square"""



class Square:
    '''Initialize Class Square
    '''

    def __init__(self, size=0):
        '''init method of class Square
        '''
        self.size = size

    @property
    def size(self):
        """get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, size):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current area of the square"""
        return (self.size * self.size)

    def my_print(self):
        """print the square with the # character"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
