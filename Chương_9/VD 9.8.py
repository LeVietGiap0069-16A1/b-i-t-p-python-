# THAM SỐ BẮT BUỘC
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
bmi=tinh_bmi(55,1.6)
print("BMI:",bmi)
tinh_bmi(60)