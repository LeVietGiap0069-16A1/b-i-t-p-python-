# LIST NUMBERS 2
list2=[]
duong=[]
am=[]
while True:
    a=float(input("Nhập số: "))
    list2.append(a)
    if a==0:
        break
print("Danh sách list",list2)
for i in list2:
    if i>0:
        duong.append(i)
    elif i<0:
        am.append(i)
sum=0
for i in am:
    sum+=i
print("trung bình cộng các phần tử âm:",sum/len(am))
for i in duong:
    sum+=i
    print("Trung bình cộng các phần tử dương:",sum/len(duong))
for i in duong:
    if i>1:
        print(list2,"là các số nguyên tố") 
    else:
        print(list2,"không phải là các số nguyên tố")       
print("Số lớn nhất trong list",max(list2))
print("Số nhỏ nhất trong list",min(list2))
list2.sort()
print("Sắp xếp list theo thứ tự tăng dần",list2)
