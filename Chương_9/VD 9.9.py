# THAM SỐ TỪ KHÓA (KEYWORD ARGUMENT)
import math
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang/math.pow(chieu_cao,2)
    return bmi
bmi=tinh_bmi(chieu_cao=1.7,can_nang=55)
print("BMI:",bmi)