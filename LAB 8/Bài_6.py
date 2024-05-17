def loc_so_le(danh_sach):
    return list(filter(lambda x: x % 2 != 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
so_le = loc_so_le(danh_sach)
print("Các số lẻ trong danh sách:", so_le)

def loc_so_chan(danh_sach):
    return list(filter(lambda x: x % 2 == 0, danh_sach))

so_chan = loc_so_chan(danh_sach)
print("Các số chẵn trong danh sách:", so_chan)

def lap_phuong_danh_sach(danh_sach):
    return list(map(lambda x: x**3, danh_sach))

danh_sach_lap_phuong = lap_phuong_danh_sach(danh_sach)
print("Danh sách lập phương:", danh_sach_lap_phuong)

def loc_va_lap_phuong_so_chan(danh_sach):
    so_chan = filter(lambda x: x % 2 == 0, danh_sach)
    lap_phuong_so_chan = map(lambda x: x**3, so_chan)
    return list(lap_phuong_so_chan)

so_chan_lap_phuong = loc_va_lap_phuong_so_chan(danh_sach)
print("Danh sách lập phương của các số chẵn:", so_chan_lap_phuong)

def loc_va_binh_phuong_so_le(danh_sach):
    so_le = filter(lambda x: x % 2 != 0, danh_sach)
    binh_phuong_so_le = map(lambda x: x**2, so_le)
    return list(binh_phuong_so_le)

so_le_binh_phuong = loc_va_binh_phuong_so_le(danh_sach)
print("Danh sách bình phương của các số lẻ:", so_le_binh_phuong)
