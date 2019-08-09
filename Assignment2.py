class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    # adds imaginary numbers
    def sum(self, realnum, imagnum):
        self.real = realnum
        self.imag = imagnum
        complex_one = complex(self.r,self.i)
        complex_two = complex(self.real, self.imag)
        return complex_one + complex_two

x = Complex(3.0,-4.5)
print(x.r, x.i)
#print(x.sum())

print('Imaginary sum:', x.sum(2,-5))


