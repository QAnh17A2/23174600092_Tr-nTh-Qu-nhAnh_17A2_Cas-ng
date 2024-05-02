sinh_vien = {}

for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm thi của sinh viên {i}: "))
    sinh_vien[ten] = diem

so_luong_sv = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for ten, diem in sinh_vien.items():
    if diem >= 8.5:
        so_luong_sv['A'] += 1
    elif diem >= 7.0:
        so_luong_sv['B'] += 1
    elif diem >= 5.5:
        so_luong_sv['C'] += 1
    elif diem >= 4.0:
        so_luong_sv['D'] += 1
    else:
        so_luong_sv['F'] += 1

print("Thống kê số lượng sinh viên ở mỗi loại học lực:")
for hoc_luc, so_luong in so_luong_sv.items():
    print(f"Học lực {hoc_luc}: {so_luong} sinh viên")