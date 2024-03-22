chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(" Chỉ số BMI của bạn là: ", bmi)
if bmi < 18.5:
    print("Phân loại BMI: Gầy")
elif bmi >=18.5 and bmi < 25.0:
    print("Phân loại BMI: Bình thường")
elif bmi >=25.0 and bmi < 30.0:
    print("Phân loại BMI: Hơi béo")
else:
    print("Phân loại BMI: Béo")