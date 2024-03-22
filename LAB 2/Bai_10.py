print("         CÁC THỂ LOẠI PHIM         ")
print("          1. Hành động             ")
print("          2. Kinh dị               ")
print("          3. Tình cảm              ")
print("          4. Hài hước              ")
print("          5. Hoạt hình             ")

The_loai = int(input("Nhập lựa chọn từ 1-5: "))
thoi_gian = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")

# Hành động
if The_loai == 1:  
    if thoi_gian in ["sáng", "trưa", "chiều"]:
        print("Phim Hành động có suất chiếu vào", thoi_gian)
    else:
        print("Không có suất chiếu")
# Kinh dị
elif The_loai == 2:  
    if thoi_gian == "tối":
        print("Phim Kinh dị có suất chiếu vào tối")
    else:
        print("Không có suất chiếu")
# Tình cảm
elif The_loai == 3:  
    if thoi_gian == "tối":
        print("Phim Tình cảm có suất chiếu vào tối")
    else:
        print("Không có suất chiếu")
# Hài hước
elif The_loai == 4:  
    if thoi_gian in ["sáng", "trưa", "chiều", "tối"]:
        print("Phim Hài hước có suất chiếu vào", thoi_gian)
    else:
        print("Không có suất chiếu")
# Hoạt hình
elif The_loai == 5:  
    if thoi_gian in ["sáng", "trưa"]:
        print("Phim Hoạt hình có suất chiếu vào", thoi_gian)
    else:
        print("Không có suất chiếu")
else:
    print("Lựa chọn không hợp lệ")