import os
_path=""
lsthoadon=[]
def luu_ds_hoa_don(lsthoadon):
    return
def them_hoa_don(lstHoadon):
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
        lsthoadon.append({'so_hd':so_hd,'ngay_hd':ngay_hd,'ho_ten_kh':ho_ten_kh,'dia_chi':dia_chi,'quan':quan,'dien_thoai':dien_thoai, 'tong_tien_hd':tong_tien_hd, 'tam_ung':tam_ung, 'con_lai':con_lai})
        #hết lệnh append
        tt=input('Bạn có muốn tiếp tục thêm? (1:TT):')
        if tt!=1:
            break
    return 
# --------------------------------------------------------------------
def in_ds_hoa_don(lsthoadon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_hd','ngay_hd','ho_ten_kh','dia_chi','quan','dien_thoai','tong_tien_hd','tam_ung','con_lai'))

    for hd in lsthoadon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],hd['ngay_hd'],hd['ho_ten_kh'],hd['dia_chi'],hd['quan'],hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))
    return
def tra_cuu_hoa_don(lsthoadon):
    return 
def thong_ke(lsthoadon):
    return
def xoa_hoa_don(lsthoadon):
    return
def doc_hoa_don(lsthoadon):
    return


    
        
    
    