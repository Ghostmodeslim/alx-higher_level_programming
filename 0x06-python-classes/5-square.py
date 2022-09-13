#!/usr/bin/python3
""""Define an empty class"""


class Square:
    ''' a class named square'''
    __size = None

    def __init__(self, size=0):
        '''Initializes class'''
        if size != int(size):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Returns the current area square'''
        return(self.__size ** 2)

    @property
    def size(self):
        '''retrives size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''sets size'''
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''prints a square with the character #'''
        if self.__size != 0:
            for a in range(self.area()):
                print("#", end="\n" if (a+1) % self.__size == 0 else "")
        else:
            print("")
