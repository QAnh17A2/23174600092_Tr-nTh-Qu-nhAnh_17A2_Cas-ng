so_1 = int(input("Nhập số nguyên thứ nhất: "))
so_2 = int(input("Nhập số nguyên thứ hai: "))
so_3 = int(input("Nhập số nguyên thứ ba: "))

if so_1 >= so_2 and so_1 >= so_3:
    if so_2 >= so_3:
        so_lon_thu_hai = so_2
    else:
        so_lon_thu_hai = so_3
elif so_2 >= so_1 and so_2 >= so_3:
    if so_1 >= so_3:
        so_lon_thu_hai = so_1
    else:
        so_lon_thu_hai = so_3
else:
    if so_1 >= so_2:
        so_lon_thu_hai = so_1
    else:
        so_lon_thu_hai = so_2

print("Số lớn thứ hai là:", so_lon_thu_hai)