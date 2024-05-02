kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}

gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

mua_hang = {
    "banana": 2,
    "orange": 1,
    "pear": 3
}

hoa_don = {}

for mat_hang, so_luong in mua_hang.items():
    don_gia = gia_tien[mat_hang]
    tong_tien = don_gia * so_luong
    hoa_don[mat_hang] = {
        "Số lượng": so_luong,
        "Đơn giá": don_gia,
        "Thành tiền": tong_tien
    }

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(mat_hang + ":")
    for key, value in thong_tin.items():
        print("\t", key, ":", value)