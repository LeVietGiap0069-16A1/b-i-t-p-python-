def read_file(a):
    a=str(input("Nhập tên tập tin:"))
    f= open(a,"r")
    b=f.read()
    print(b)

