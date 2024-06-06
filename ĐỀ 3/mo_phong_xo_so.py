import random
import csv

def rut_so():
    return random.randint(1, 100)

def kiem_tra_ket_qua(so_du_doan, so_da_rut):
    return so_du_doan.intersection(so_da_rut)

def tinh_xac_suat_so_trung(so_lan_rut, thong_ke):
    return {so: thong_ke[so] / so_lan_rut for so in thong_ke}

def luu_ket_qua_csv(filename, ket_qua):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Lan_choi', 'So_du_doan', 'So_trung', 'xac_suat_trung_giai'])
        for lan_choi, (so_du_doan, so_trung, xac_suat) in enumerate(ket_qua):
            writer.writerow([lan_choi + 1, so_du_doan, so_trung, xac_suat])

def main():
    so_lan_choi_toi_da = 5
    so_lan_choi = 0
    ket_qua_choi = []

    while so_lan_choi < so_lan_choi_toi_da:
        so_lan_choi += 1
        so_du_doan = set()
        so_da_rut = []
        thong_ke_so = {}

        so_luong_du_doan = int(input("Nhập số lượng số dự đoán: "))
        while len(so_du_doan) < so_luong_du_doan:
            so = int(input(f"Nhập số dự đoán thứ {len(so_du_doan) + 1}: "))
            if 1 <= so <= 100:
                so_du_doan.add(so)
            else:
                print("Số không hợp lệ, vui lòng nhập lại.")

        so_luong_rut = int(input("Nhập số lượng số sẽ rút: "))
        for _ in range(so_luong_rut):
            so_rut = rut_so()
            so_da_rut.append(so_rut)
            if so_rut in thong_ke_so:
                thong_ke_so[so_rut] += 1
            else:
                thong_ke_so[so_rut] = 1

        so_trung = kiem_tra_ket_qua(so_du_doan, set(so_da_rut))
        xac_suat = tinh_xac_suat_so_trung(so_luong_rut, thong_ke_so)

        tong_tien_thuong = len(so_trung) * 1000000  # 1 triệu cho mỗi số trúng
        print(f"Số trúng: {so_trung}")
        print(f"Tổng tiền thưởng: {tong_tien_thuong} VND")

        ket_qua_choi.append((so_du_doan, so_trung, xac_suat))

        tiep_tuc = input("Bạn có muốn chơi tiếp không? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break

    luu_ket_qua_csv('ket_qua_xo_so.csv', ket_qua_choi)
    print("Kết quả đã được lưu vào file ket_qua_xo_so.csv")

if __name__ == "__main__":
    main()