# Tính chỉ số BMI
chieu_cao=float(input("Nhập chiều cao của bạn:"))
can_nang=float(input('Nhập cân nặng của bạn:'))
BMI=(can_nang/(chieu_cao*chieu_cao))
print(BMI)
if BMI<18.5:
    print("Bạn gầy ")
elif BMI>18.5 and BMI<24.99:
    print("Bạn bình thuường")
else:
    print("Bạn thừa cân")