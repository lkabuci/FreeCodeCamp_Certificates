class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    ############# getter #############
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    ############# setter #############
    def set_width(self, value):
        self._width = value

    def set_height(self, value):
        self._height = value

    ############# get #############
    
    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ''
        if self.height >= 50 or self.width >= 50:
            return "Too big for picture."
        else:
            for line in range(self.height):
                picture += f"{self.width * '*'}\n"
            return picture

    def get_amount_inside(self, shape):
        wid_fit, w_rest = divmod(self.width, shape.get_width())
        hei_fit, h_rest = divmod(self.height, shape.get_height())
        return wid_fit * hei_fit

    def __repr__(self):
        return f"{__class__.__name__}(width={self.width}, height={self.height})"

    height = property(get_height, set_height)
    width = property(get_width, set_width)


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(width=side, height=side)
        self.side = side

    def get_side(self):
        return self._side

    def set_side(self, value):
        super(Square, self).__init__(width=value, height=value)
        self._side = value
    
    def set_width(self, value):
        super(Square, self).__init__(width=value, height=value)
        self._side = value
    
    def set_height(self, value):
        super(Square, self).__init__(width=value, height=value)
        self._side = value

    def __repr__(self):
        return f"{__class__.__name__}(side={self.side})"
    
    side = property(get_side, set_side)
        
