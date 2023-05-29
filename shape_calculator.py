class Rectangle:
    def __init__(self, width, height):
        self.class_name = "Rectangle"
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        w_str = "*" * self.width
        image = ""
        for i in range(self.height):
            image += f"{w_str}\n"
        return image

    def get_amount_inside(self, shape):
        inside = self.get_area() // shape.get_area()
        return inside

    def __str__(self):
        if self.class_name == "Rectangle":
            return f"{self.class_name}(width={self.width}, height={self.height})"
        return f"{self.class_name}(side={self.width})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.class_name = "Square"

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)
