class My_Shape:
    def __init__(self, color = "red", is_filled = bool(1)):
     self.color = color
     self.is_filled = is_filled
    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"
    def getArea(self):
        return 0

class Rectangle(My_Shape):
    def __init__(self, length, width, x_top_left, y_top_left):
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.width = width
        self.length = length
    def getArea(self):
        self.coordinates = (self.x_top_left, self.y_top_left)
        print("coordinates of rectangle's top left:", self.coordinates)
        return int(self.length * self.width)

class Circle(My_Shape):
    def __init__(self, radius, x_center, y_center):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def getArea(self):
        self.coordinates = (self.x_center, self.y_center)
        print("coordinates of circle's center:", self.coordinates)
        return (3.14 * (self.radius * self.radius))

rectangle_area = Rectangle(int(input("enter length of rectangle ")), int(input("enter width of rectangle ")), int(input("enter x top left coordinate of rectangle ")), int(input("enter y top left coordinate of rectangle ")))
print("area of your rectangle:", rectangle_area.getArea())

circle_area = Circle(int(input("enter radius of circle ")), int(input("enter x coordinate of circle's center ")), int(input("enter y coordinate of circle's center ")))
print("area of your circle:", circle_area.getArea())