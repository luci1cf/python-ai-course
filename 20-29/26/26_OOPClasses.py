# OOP - Object Oriented Programming for Beginners

# Syntax Basics
#---------------------------------------------------------------------------
# Template
# class Element:
#     id_count = 1
#
#     def __init__(self, w, h, loc, mat):
#         self.width      = 10
#         self.height     = 20
#         self.location   = loc
#         self.material   = mat
#         self.id         = self.gen_id()
#
#         print(f'Creating an element <{self.id}>...')
#
#
#     def gen_id(self):
#         el_id = Element.id_count
#         Element.id_count += 1
#         return el_id
#
#     def print_data(self):
#         print(f'Element ID: <{self.id}>')
#         print(f'Material: {self.material}')
#         print(f'Location: {self.location}')
#         print(f'Width: {self.width}')
#         print(f'Height: {self.height}')
#         print('-'*50)
#
#     def move(self, x, y):
#         print(f'Moving an Element X: {x}, Y: {y}')
#         old_x = self.location[0]
#         old_y = self.location[1]
#         self.location = (old_x + x, old_y + y)
#
#     def __repr__(self):
#         return f'Element ID: <{self.id}>'
#
# # Object Instances Based on Template
# elem_a = Element(10, 20, (0, 0), 'Wood')
# elem_b = Element(15, 30, (10, 10), 'Concrete')
#
# # Print Statements
# print(elem_a)
# print(elem_b)

# OOP - Inheritance

class Element:
    def __init__(self):
        print('Element __init__ executed.')
        self.category = self.cat

    def cat(self):
        return self.__class__.__name__

    def move(self):
        print(f'Moving {self.cat()}.')

    def rotate(self):
        print(f'Rotating {self.cat()}.')

    def scale(self):
        print(f'Scaling {self.cat()}.')

# Children Classes (Inherited)
class Wall(Element):
    def __init__(self):
        super().__init__()
        print('Wall __init__ executed.')

    def move(self):
        print(f'Moving Wall based on Line.')

class Floor(Element):
    def __init__(self):
        super().__init__()
        print('Floor __init__ executed.')

    def move(self):
        print(f'Moving Floor based on Point.')

wall_a = Wall()
floor_a = Floor()

wall_a.move()
floor_a.move()