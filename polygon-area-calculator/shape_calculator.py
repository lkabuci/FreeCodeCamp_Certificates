class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self):
        pass

    def set_height(self):
        pass

    def get_area(self):
        '''Returns area (width * height)'''
        pass

    def get_perimeter(self):
        '''Returns perimeter (2 * width + 2 * height)'''
        pass

    def get_diagonal(self):
        '''Returns diagonal ((width ** 2 + height ** 2) ** .5)'''
        pass

    def get_picture(self):
        '''Returns a string that represents the shape using lines of "*".'''
        pass

    def get_amount_inside(self):
        pass



class Square(Rectangle):
    def __int__(self, side):
        self.height = Rectangle.height
        self.width = Rectangle.width
        self.side = side

    def set_side(self):
        pass
