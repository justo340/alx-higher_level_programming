#!/usr/bin/python3

"""define a class sqaure"""


class Square:
    '''Initialize Class Square
    '''

    def __init__(self, size=0, position=(0, 0)):
        """the init method of square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
         """Call the function to checking property
            Returns:
                The size of the square"""
        return self.__size

    @property
    def position(self):
        """call the function to check the property
            returns a tuple position"""
        return self.__position


    @size.setter
    def size(self, size):
        """check errors and setter for size attribute
        Args:
            value: Value to checking errors
                                        
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
         """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, size):
        """checks errors and setter for attribute
        Args:
            Value: Value to check errors

        Raises:
            TypeErrrror:Exception if size is not integer
        """
        if type(size) is not tuple or len(size) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(size[0]) is not int or size[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(size[1]) is not int or size[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = size


    def area(self):
        """calculates area of the square"""
        return (self.__size * self.__size)

    def print(self):
        """print square using the #character"""
        if self.__size ==0:
            print()
            return 
        for i in range (self.__size):
            for j in range (self.__size):
                print("#",end ="")
            print()
