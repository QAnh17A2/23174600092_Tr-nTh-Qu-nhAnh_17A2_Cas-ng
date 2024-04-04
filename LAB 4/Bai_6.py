so_chu = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

so = input("Nhập một số nguyên: ")

print("Kết quả in ra màn hình là:", end=" ")
i = 0
while i < len(so):
    print(so_chu[so[i]], end=" ")
    i += 1