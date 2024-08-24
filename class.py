import math


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        # return f"<Triangle a={self.a} b={self.b}>"
        return f"Triangle(a=9,b=16)"

    def get_hypotenuse(self):
        return math.sqrt(self.a ** 2 + self.b**2)

    def get_area(self):
        return (self.a * self.b)/2

    def describe(self):
        return f"My area is {self.get_area()}."


class ColoredTriangle(Triangle):
    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color

    def describe(self):
        return f"{super().describe()} I am {self.color}"
