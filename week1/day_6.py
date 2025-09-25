# Hacker Rank Problems


# Python: Collections.Counter()
# Problem: Count items using collections module
# Link: https://www.hackerrank.com/challenges/collections-counter/problem

# from collections import Counter
# shoe_num =  int(input())
# avail_size = list(map(int,input().split()))
# total_money = 0
# stock = Counter(avail_size)
# for _ in range (int(input())):
#     a,b = list(map(int,input().split()))
#     if stock[a] > 0:
#         total_money += b
#         stock[a] -= 1
# print(total_money)


# Python: Classes: Dealing with Complex Numbers
# Problem: Define class for complex numbers
# Link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem



# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, no):
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)

#     def __sub__(self, no):
#         return Complex(self.real - no.real, self.imaginary - no.imaginary)

#     def __mul__(self, no):
#         real = self.real * no.real - self.imaginary * no.imaginary
#         imag = self.real * no.imaginary + self.imaginary * no.real
#         return Complex(real, imag)

#     def __truediv__(self, no):
#         denominator = no.real ** 2 + no.imaginary ** 2
#         real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
#         imag = (self.imaginary * no.real - self.real * no.imaginary) / denominator
#         return Complex(real, imag)

#     def mod(self):
#         return Complex((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')

