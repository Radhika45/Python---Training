class Polygon:

    def render(self):
        print("Render Polygon...")

class Square(Polygon):

    def render(self):
        print("Render Square..")

class Circle(Polygon):

    def render(self):
        print("Render Circle...")

p1 = Polygon()
print(p1.render())

s1 = Square()
print(s1.render())

c1 = Circle()
print(s1.render())