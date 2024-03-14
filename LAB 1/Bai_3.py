so_tien=10.000
lai_suat=0.06
#1.
amount_after_5_years=so_tien*((lai_suat+1)**5)
#2.
amount_after_10_years=so_tien*((1+lai_suat)**10)
#3.
ty_le_tang_truong=(amount_after_10_years-amount_after_5_years)/so_tien
#4.
print("số tiền nhận được sau 5 năm là: {:.2f}".format(amount_after_5_years))
print("số tiền nhận được sau 10 năm là: {:.2f}".format(amount_after_10_years))
print("tỷ lệ tăng trưởng của số tiền có sau 10 năm so với số tiền có sau 5 năm là: {:.2f}".format(ty_le_tang_truong))