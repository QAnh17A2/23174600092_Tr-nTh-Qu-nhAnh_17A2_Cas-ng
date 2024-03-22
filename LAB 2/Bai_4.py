diem = float(input("Nhập điểm của bạn: "))

if 0 <= diem < 5:
    print("Điểm kém")
elif 5 <= diem < 7:
    print("Điểm trung bình")
elif 7 <= diem < 8.5:
    print("Điểm khá")
elif 8.5 <= diem <= 10:
    print("Điểm tốt")
else:
    print("Điểm không hợp lệ")