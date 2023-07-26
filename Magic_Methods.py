class ComplexClass:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"Real Part:{self.real} and Imaginary Part:{self.imaginary}"

    def __repr__(self):
        return f"Real Part:{self.real} and Imaginary Part:{self.imaginary}"

    def __del__(self):
        print("Deleting the complex Number")

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __lt__(self, other):
        return self.real<other.real and self.imaginary <other.imaginary

    def __le__(self, other):
        return self.real<=other.real and self.imaginary<=other.imaginary

    def __gt__(self, other):
        return self.real>other.real and self.imaginary>=other.imaginary

    def __ge__(self, other):
        return self.real > other.real and self.imaginary >= other.imaginary

    def __add__(self,other):
        return ComplexClass(self.real+other.real, self.imaginary+other.imaginary)

def test_func():
    Complex_no4 = ComplexClass(1,1)
    print(Complex_no4)
test_func()
Complex_no1 = ComplexClass(2,2)
Complex_no2 = ComplexClass(3,3)
result = Complex_no1+Complex_no2
print(Complex_no1)
print(Complex_no2)
print(result)
print(Complex_no1>Complex_no2)
print(Complex_no1<Complex_no2)


