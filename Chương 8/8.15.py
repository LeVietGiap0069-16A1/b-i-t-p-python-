import math
positive=math.inf
while True:
    num=int(input("Nhập một số:"))
    if num!=0 and num<positive:
        print(math.sum(num))
    else:
        break
        
        
    