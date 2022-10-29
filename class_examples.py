# example 1
# class Person:
#     # class attribute
#     about = 'This class stores the name and age for a person'
    
#     def __init__(self, name, age):
#             self.name = name
#             self.age = age
    
#     def details(self):
#             print(f"Person's name is {self.name} and age is {self.age}")
    
#     @classmethod
#     def info(cls):
#         print(cls.about)
 
 
# Person.info()

# candy = Person("Candy", 20)
# candy.details()

# print(candy.about)


# example 2: single inheritance
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

# # create a class Cube that inherits from Square
# class Cube(Square):
#     def surface_area(self):
#         face_area = super().area()
#         return face_area * 6

#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length


# multiple classes inheritance
# Method Resolution Order (MRO)
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# class RightPyramid(Square, Triangle):
#     def __init__(self, base, slant_height):
#         self.base = base
#         self.slant_height = slant_height
#         super().__init__(self.base)

#     def area(self):
#         base_area = super().area()
#         perimeter = super().perimeter()
#         return 0.5 * perimeter * self.slant_height + base_area

rect = Rectangle(2,4)
print(rect.area())

square = Square(4)
print(square.area())

# cube = Cube(4)
# print(cube.surface_area())
# print(cube.volume())

# pyramid = RightPyramid(5,4)
# print(pyramid.area())


# class Person:
#     def __getattribute__(self, attr_name):
#         print('hello world')


class Person:
    def __getattribute__(self, attr_name):
        raise AttributeError
        
    def __getattr__(self, attr_name):
        print('hello universe')

    
alice = Person()
getattr(alice, 'age')