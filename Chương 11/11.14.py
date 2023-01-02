dictPhoneBook={
    "Ten":"So dien thoai",
    "Minh":"0989741258",
    "Hanh":"0903852147",
    "Binh":"0913753951",
    "An":"0933753654"
}
def search_name(name):
    name=str(input("Nhap ten can tim: "))
    count=0
    for key in dictPhoneBook:
        if key==name:
            count+=1
            print("Thong tin can tim:")
            print("Danh bạ:",search_name(name))
            print(key,":",dictPhoneBook.get(key))
    if count==0:
        print("Khong tim thay!")
def create(nameIn,phoneIn):
    nameIn=str(input("Nhap ten: "))
    phoneIn=str(input("Nhap so dien thoai: "))
    create(nameIn,phoneIn)
    if nameIn in dictPhoneBook:
        print("Ten tao moi da ton tai!")
    else:
        try:
            dictPhoneBook.update({nameIn:phoneIn})
            print("Tao moi thanh cong!")
        except:
            print("Tao moi that bai!")
print(dictPhoneBook)


