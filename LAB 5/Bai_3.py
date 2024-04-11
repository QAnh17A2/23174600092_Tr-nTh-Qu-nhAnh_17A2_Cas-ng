chuoi = input("Nhập 1 chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")

vi_tri_tu = chuoi.find(tu_can_tim)

if vi_tri_tu != -1:
    print("Từ", tu_can_tim, "được tìm thấy tại vị trí:", vi_tri_tu)
else:
    print("Từ", tu_can_tim, "không được tìm thấy trong chuỗi.")

danh_sach_tu = chuoi.split()
tan_suat_xuat_hien = {}
for tu in danh_sach_tu:
    tan_suat_xuat_hien[tu] = tan_suat_xuat_hien.get(tu, 0) + 1

tu_xuat_hien_nhieu_nhat = max(tan_suat_xuat_hien, key=tan_suat_xuat_hien.get)
tan_so_xuat_hien_nhieu_nhat = tan_suat_xuat_hien[tu_xuat_hien_nhieu_nhat]

print("Từ xuất hiện nhiều nhất trong chuỗi là:", tu_xuat_hien_nhieu_nhat)
print("Tần suất xuất hiện:", tan_so_xuat_hien_nhieu_nhat)