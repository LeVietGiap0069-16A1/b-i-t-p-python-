def change_list(lst):
    # Thêm vào sau list
    lst.append(10)
    lst.append(9)
    print("List trong hàm:",lst)
    return
lst=[1,2,3,4,5,6]
print("List ban đầu:", lst)
change_list(lst)
print("List ngoài hàm:",lst)