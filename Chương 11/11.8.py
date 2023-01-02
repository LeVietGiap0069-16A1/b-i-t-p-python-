lucky=[]
while True:
    a=float(input("Nhập phần tử trong list:"))
    lucky.append(a)
    if a==0:
        break
for i in lucky:
    if i %7==0:
        print("Danh sách các số đã cho:",lucky,"là các số may mắn")
    else:
        print("Danh sách các số đã cho:",lucky,"không phải là các số may mắn")