van_ban = "Mr. Rakesh is our next door neighbor. He is not a good man. He always speak ill of others. He is very quarrelsome. He never support anyone. He drinks daily. He uses abusive language. He beat his wife and children. He does not have good terms with anybody in the colony. Everybody hates him. I also dislike him."

tu_trong_van_ban = van_ban.split()
for i in range(len(tu_trong_van_ban)):
    tu_trong_van_ban[i] = tu_trong_van_ban[i].strip('.').strip(',').strip()

dem_tu = {}
for tu in tu_trong_van_ban:
    if tu in dem_tu:
        dem_tu[tu] += 1
    else:
        dem_tu[tu] = 1

tu_nhieu_nhat = max(dem_tu, key=dem_tu.get)
tu_it_nhat = min(dem_tu, key=dem_tu.get)

print("Từ có số lượng nhiều nhất là: ", tu_nhieu_nhat)
print("Từ có số lượng ít nhất là: ", tu_it_nhat)