import math
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
tinh_A= lambda x, n:math.pow((x**2+x+1),n)+math.pow((x**2-x+1),n)
print(tinh_A(x,n))