import math

a = float(input("Nhập hệ số góc của đường thẳng: "))
b = float(input("Nhập hệ số tự do của đường thẳng: "))

tam_duong_tron_x = float(input("Nhập tọa độ x của tâm đường tròn: "))
tam_duong_tron_y = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

khoang_cach_tam_duong_tron_toi_duong_thang = abs(b) / math.sqrt(a**2 + 1)

if khoang_cach_tam_duong_tron_toi_duong_thang < ban_kinh:
    print("Đường thẳng cắt đường tròn.")
elif khoang_cach_tam_duong_tron_toi_duong_thang == ban_kinh:
    print("Đường thẳng tiếp xúc với đường tròn.")
elif khoang_cach_tam_duong_tron_toi_duong_thang > ban_kinh:
    print("Đường thẳng nằm ngoài đường tròn.")
else:
    print("Đường thẳng nằm trong đường tròn.")