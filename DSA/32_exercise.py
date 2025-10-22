class Circle:
    def __init__(self, radius):
        self.radius_circle = radius

    def area(self):
        area = 3.14 * self.radius_circle * self.radius_circle
        print(area)

    def circumference(self):
        circum = 2 * 3.14 * self.radius_circle
        print(circum)


circle_1 = Circle(10)  # initialize
circle_1.area()
circle_1.circumference()
