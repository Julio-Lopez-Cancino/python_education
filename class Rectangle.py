#creating a class of a Rectangle

class Rectangle():
    recs = [] #store all instances of this class created.
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2 


class Square():
    def __init__(self, s1):
        self.s1 = s1
        
    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, chg):
        self.s1 += chg

        
rec1 = Rectangle(7, 12)
sqr1 = Square(5)

print(rec1.calculate_perimeter())
print(sqr1.calculate_perimeter())

print(sqr1.s1)
sqr1.change_size(-3)
print(sqr1.s1)
sqr1.change_size(8)
print(sqr1.s1)
