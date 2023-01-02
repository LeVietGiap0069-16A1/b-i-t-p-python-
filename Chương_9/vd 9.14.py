def binh_phuong(x): 
    return x*x
List_1 = [1,2,3,4,5] 
List_2 = list(map(binh_phuong, List_1))
print(List_2)