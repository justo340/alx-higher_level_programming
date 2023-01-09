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
        return (self.__size)

    @property
    def position(self):
        """call the function to check the property
            returns a tuple position"""
        return (self.__position)

    @size.setter
    def size(self,value):
        """check errors and setter for size attribute
        Args:
            value: Value to checking errors
                                        
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
         """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self,value):
        """checks errors and setter for attribute
        Args:
            Value: Value to check errors

        Raises:
            TypeErrrror:Exception if size is not integer
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """calculates area of the square"""
        return (self.__size * self.__size)

    def print(self):
        """print square using the #character"""
        for i in range(self.__position[1]):
            print()
        for i in range (self.__size):
            for j in range (self.__position[0]):
                print(end = " ")
            for k in range(self.__size):
                print("#",end ="")
            print()
