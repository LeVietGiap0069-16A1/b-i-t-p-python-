set1=set()
set2=set()
while True:
    a=int(input("Nhập các phần tử set1:"))
    z=int(input("Nhập 1 là tiếp tục, 0 là dừng lại:"))
    set1.add(a)
    if z==1 :
        continue
    if z==0:
        break

while True:
    b=int(input("Nhập các phần tử set2:"))
    x=int(input("Nhập 1 là tiếp tục, 0 là dừng lại:"))
    set2.add(b)
    if x==1:
        continue
    if x==0:
        break
# In set1, set2
print("Phần tử set1:",set1)
print("Phần tử set2:",set2)
# Mỗi set có bn phần tử
print("Set1 có",len(set1),"phần tử")
print("Set2 có",len(set2),"phần tử")
# Tổng các phần tử
sum1=0
for i in set1:
    sum1+=i
print("Tổng các phần tử set1 là:",sum1)
sum2=0
for z in set2:
    sum2+=z
print("Tổng các phần tử set2 là:",sum2)
# Tìm giá trị lớn nhất, nhỏ nhất của mỗi set
print("Giá trị nhỏ nhất trong set1:",min(set1))
print("Giá trị lớn nhất trong set1:",max(set1))
print("Giá trị nhỏ nhất trong set2:",min(set2))
print("Giá trị lớn nhất trong set2:",max(set2))
# Thực hiện set union của set1 và set2 và in kết quả
print("set1 union:",(set1.union(set2)))
# Thực hiện set intersection 
print("set1 difference:",set1.difference(set2))
# Thực hiện set difference
print("set1 difference:",set1.difference(set2))
# Thực hiện set symmetric diference
print("set1 symmetricdifference:",set1.symmetric_difference(set2))
print("set2 symmetric difference:",set2.symmetric_difference(set1))
# Sắp xếp set1 theo thứ tự tăng dần, set2 giảm dần 
print("set1 tăng dần:",sorted(set1))
print("set2 giảm dần:",sorted(set2,reverse=True))
# Lấy ra một phần tử ở set1 và set2 và in ra kết quả
print("Lấy ra 1 phần tử trong set1:",set1.pop())
print("set1 sau khi pop",set1)