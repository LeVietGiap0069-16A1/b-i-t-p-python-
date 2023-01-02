# quản lí hóa đơn
import os 
_path=""
lstHoaDon=[]
#---------------Hàm thứ nhất------------------------
def no_file_hoa_don(_path,lstHoaDon):
    return
#---------------Hàm thứ hai-------------------------
def luu_ds_hoa_don(lstHoaDon):
    return
#---------------Hàm thứ ba--------------------------
def them_hoa_don(lstHoaDon):
    while True:
        so_hd=input('Nhập số hóa đơn :')
        ngay_hd=input('Ngày hóa đơn :')
        ho_ten_kh=input('Họ tên khách hàng :')
        dia_chi=input('Địa chỉ khách hàng :')
        quan=input('Quận :')
        dien_thoai=input('Điện thoại :')
        tong_tien_hd=float(input('Tổng tiền hợp đồng :'))
        tam_ung=float(input('Tạm ứng :'))
        con_lai=float(tong_tien_hd - tam_ung)
        lstHoaDon.append({'Số hóa đơn':so_hd,'Ngày hóa đơn':ngay_hd,   ' Tên khách hàng':ho_ten_kh,'Địa chỉ':dia_chi,'Quận':quan,'Điện thoại':dien_thoai, 'Tổng tiền hóa đơn':tong_tien_hd, 'Tạm ứng':tam_ung, 'Còn lại':con_lai})
        #hết lệnh append

        tt=input('Bạn có muốn tiếp tục thêm? (1:TT):')
        if tt!=1:
            break
         
them_hoa_don(lstHoaDon)

#---------------------------------------------------
def  in_ds_hoa_don(lstHoaDon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('Số hóa đơn','Ngày hóa đơn',   ' Tên khách hàng','Địa chỉ','Quận','Điện thoại','Tổng tiền hóa đơn','Tạm ứng','Còn lại'))
    for hd in lstHoaDon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['Số hóa đơn'],hd['Ngày hóa đơn'],hd[' Tên khách hàng'],hd['Địa chỉ'],hd['Quận'],hd['Điện thoại'],hd['Tổng tiền hóa đơn'],hd['Tạm ứng'],hd['Còn lại']))
    return
in_ds_hoa_don(lstHoaDon)
print(lstHoaDon)
#---------------------------------------------------
def tra_cuu_hoa_don(lstHoaDon):
    find=input("Nhập để tra cứu hóa đơn:")
    if lstHoaDon.values(find) in lstHoaDon:
        print(find)
    else:
        if find not in lstHoaDon:
            print("Không tìm thấy trong danh sách hóa đơn")

    return
def thong_ke(lstHoaDon):
    return 
def xoa_hoa_don(lstHoaDon):
    lstHoaDon.clear()
    return
def doc_hoa_don(lstHoaDon):
    return
def mo_file_hoa_don(lstHoaDon):
    return 

print("CHƯƠNG TRÌNH QUẢN LÝ HÓA ĐƠN:")

while True:
    print("Nhấn 1 để Thêm hóa đơn")
    print("Nhấn 2 Danh sách hóa đơn")
    print("Nhấn 3 Tra cứu hóa đơn")
    print("Nhấn 4 Xóa hóa đơn")
    print("Nhấn 5 Thống kê")
    print("Nhấn 6 Lưu danh sách hóa đơn in ra file CSV")
    print("Nhấn 7 Đọc file CSV")
    choice=int(input("Chọn chức năng cần thực hiện:"))
    if choice==1:
        print("THÊM HÓA ĐƠN MỚI")
        so_hd=input('Nhập số hóa đơn :')
        ngay_hd=input('Ngày hóa đơn :')
        ho_ten_kh=input('Họ tên khách hàng :')
        dia_chi=input('Địa chỉ khách hàng :')
        quan=input('Quận :')
        dien_thoai=input('Điện thoại :')
        tong_tien_hd=float(input('Tổng tiền hợp đồng :'))
        tam_ung=float(input('Tạm ứng :'))
        con_lai=float(tong_tien_hd - tam_ung)
        lstHoaDon.append({'Số hóa đơn':so_hd,'Ngày hóa đơn':ngay_hd,   ' Tên khách hàng':ho_ten_kh,'Địa chỉ':dia_chi,'Quận':quan,'Điện thoại':dien_thoai, 'Tổng tiền hóa đơn':tong_tien_hd, 'Tạm ứng':tam_ung, 'Còn lại':con_lai})
    if choice==2:
        print("DANH SÁCH HÓA ĐƠN")
        in_ds_hoa_don(lstHoaDon)
    if choice==3:
        print("TRA CỨU HÓA ĐƠN")
        tra_cuu_hoa_don(lstHoaDon)
            
    if choice==4:
        print("XÓA HÓA ĐƠN")
        xoa_hoa_don(lstHoaDon)
    if choice==5:
        print("THỐNG KÊ")
    if choice==6:
        print("LƯU DANH SÁCH HÓA ĐƠN VÀ IN RA FILE CSV")
    if choice==7:
        print("7: ĐỌC FILE CSV")
