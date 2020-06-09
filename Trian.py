class Triangle:
    def __init__(self, a=3, b=4, c=5):
        self.a = a
        self.b = b
        self.c = c

        if not type(a) is int:
            raise TypeError("Only integers allowed")

        elif type(b) is not int:
            raise TypeError("Only integers allowed")

        elif type(c) is not int:
            raise TypeError("Only integers allowed")

        elif a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides should be positive")
        else:
            pass

        if a + b > c and a + c > b and b + c > a:
            pass
        else:
            raise ValueError("Impossible triangle")

    def compute_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

    def compute_area(self):

        h_p = Triangle.compute_perimeter(self) / 2
        area = (h_p * (h_p - self.a) * (h_p - self.b) * (h_p - self.c)) ** 0.5
        return area

    def type(self):
        if (self.a ** 2 + self.b ** 2 == self.c ** 2) or (self.a ** 2 + self.c ** 2 == self.b ** 2) or (
                self.b ** 2 + self.c ** 2 == self.c ** self.a):
            return "rectangular"

        elif (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) or (
                self.c == self.b and self.a != self.c):
            return "равнобедренный"

        elif self.a == self.b and self.a == self.c:
            print("равносторонний")
            return "равносторонний"

        elif self.a != self.b and self.a != self.c:
            print("Разносторонний")
            return "Разносторонний"


#tr1 = Triangle(3, 4, 5)
#tr1.compute_perimeter()
#tr1.compute_area()
#tr1.type()
