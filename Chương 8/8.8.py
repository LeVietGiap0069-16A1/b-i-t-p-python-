print("Chào mừng quý khách đến với resort NGHỆ CẢ CỦ")
print("Resort chúng tôi có tất cả 8 loại phòng")
print("Loại 1: Standard")
print("Loại 2: Superior Garden View")
print("Loại 3: Superior Ocean View")
print("Loại 4: Garden View Bungalow")
print("Loại 5: Pool View Bungalow")
print("Loại 6: Family Room")
print("Loại 7: Beach Front Bungalow")
print("Loại 8: VIP sea View")
print("Xin mời quý khách chọn phòng")
a=int(input("Chọn loại phòng:"))
print("Xin mời quý khách chọn số đêm mà quý khách ở lại")
b=int(input("Chọn số đêm:"))
q=1260000
w=1550000
e=1830000
r=1830000
t=2120000
y=2120000
u=2540000
i=4800000
if b==1:
    print("xin chào quý khách")
    if a==1:
        print("Phòng Standard","giá tiền phòng: ",q, "VND")
    if a==2:
        print("Phòng Superior Garden View","giá tiền phòng:",w, "VND")
    if a==3:
        print("Phòng Superior Ocean View","giá tiền phòng: ",e, "VND")
    if a==4:
        print("Phòng Garden View Bungalow","giá tiền phòng: ",r, "VND")
    if a==5:
        print("Phòng Pool View Bungalow","giá tiền phòng: ",t, "VND")
    if a==6:
        print("Phòng Family Room","giá tiền phòng: ",y, "VND")
    if a==7:
        print("Phòng Beach Front Bungalow","giá tiền phòng: ",u, "VND")
    if a==8:
        print("Phòng VIP sea View","giá tiền phòng: ",i, "VND")
if b==2 or b==3:
    print("xin chào quý khách")
    if a==1:
        print("Phòng Standard","giá tiền phòng: ",q*25/100, "VND")
    if a==2:
        print("Phòng Superior Garden View","giá tiền phòng:",w*25/100, "VND")
    if a==3:
        print("Phòng Superior Ocean View","giá tiền phòng: ",e*25/100, "VND")
    if a==4:
        print("Phòng Garden View Bungalow","giá tiền phòng: ",r*25/100, "VND")
    if a==5:
        print("Phòng Pool View Bungalow","giá tiền phòng: ",t*25/100, "VND")
    if a==6:
        print("Phòng Family Room","giá tiền phòng: ",y*25/100, "VND")
    if a==7:
        print("Phòng Beach Front Bungalow","giá tiền phòng: ",u*25/100, "VND")
    if a==8:
        print("Phòng VIP sea View","giá tiền phòng: ",i*25/100, "VND")
else:
    if a==1:
        print("Phòng Standard","giá tiền phòng: ",q*30/100, "VND")
    if a==2:
        print("Phòng Superior Garden View","giá tiền phòng:",w*30/100, "VND")
    if a==3:
        print("Phòng Superior Ocean View","giá tiền phòng: ",e*30/100, "VND")
    if a==4:
        print("Phòng Garden View Bungalow","giá tiền phòng: ",r*30/100, "VND")
    if a==5:
        print("Phòng Pool View Bungalow","giá tiền phòng: ",t*30/100, "VND")
    if a==6:
        print("Phòng Family Room","giá tiền phòng: ",y*30/100, "VND")
    if a==7:
        print("Phòng Beach Front Bungalow","giá tiền phòng: ",u*30/100, "VND")
    if a==8:
        print("Phòng VIP sea View","giá tiền phòng: ",i*30/100, "VND")
       
    
    
    
