# Viết chương trình tính năm âm lịch từ năm dương lịch
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
a= int(input("Nhập năm dương lịch: "))
b = a % 10
c = a % 12
if can==0:
    print(can[b])
elif can==1:
    print(can[b])
elif can==2:
    print(can[b])
elif can==3:
    print(can[b])
elif can==4:
    print(can[b])
elif can==5:
    print(can[b])
elif can==6:
    print(can[b])
elif can==7:
    print(can[b])
elif can==8:
    print(can[b])
elif can==9:
    print(can[b])
if chi==0:
    print(chi[c])
elif chi==11:
    print(chi[c])
elif chi==1:
    print(chi[c])
elif chi==2:
    print(chi[c])
elif chi==3:
    print(chi[c])
elif chi==4:
    print(chi[c])
elif chi==5:
    print(chi[c])
elif chi==6:
    print(chi[c])
elif chi==7:
    print(chi[c])
elif chi==8:
    print(chi[c])
elif chi==9:
    print(chi[c])
elif chi==10:
    print(chi[c])
print("Năm âm lịch:",can[b] + " " + chi[c])