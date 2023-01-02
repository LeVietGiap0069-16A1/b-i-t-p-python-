''' Sử dụng Lambda để tính
diện tích, chu vi hình tròn với tham số r
diện tích, chu vi hình chữ nhật với tham số a,b'''
import math
S_hinh_tron = lambda r: math.pi*(r**2)
print("Diện tích hình tròn là:", S_hinh_tron)
C_hinh_tron= lambda r: 2*(math.pi)*(math.pow(r,2))
print("Chu vi hình tròn là:", C_hinh_tron)
S_hcn= lambda a, b: a*b
print("Diện tích hình chữ nhật là:", S_hcn)
C_hcn= lambda a, b: (a+b)*2
print("Chu vi hình chữ nhật là:", C_hcn)
r=int(input("Nhập bán kính:"))
print("Diện tích hình tròn là:",S_hinh_tron(r))
print("Chu vi hình tròn là:",C_hinh_tron(r))
a=int(input("Nhập chiều dài:"))
b=int(input("Nhập chiều rộng:"))
print("Diện tích hình chữ nhật là",S_hcn(a,b))
print("Chu vi hình chữ nhật là",C_hcn(a,b))
