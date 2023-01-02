print("Tính tiền điện")
a=int(input( "số KWh ="))
b="Số tiền điện là :"
c="VND"
if a <= 50:
    print(b,(a*1.678),c)
elif 51<=a<=100:
    print(b,(a*1.734),c)
elif 101<=a<=200:
    print(b,(a*2.014),c)
elif 201<=a<=300:
    print(b,(a*2.536),c)
elif 301<=a<=400:
    print(b,(a*2.834),c)
else:
    print(b,(a*2.927),c)