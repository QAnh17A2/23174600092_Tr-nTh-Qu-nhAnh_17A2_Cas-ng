# 1
def cubesum(n):
    digits = str(n)
    
    total = sum(int(digit)**3 for digit in digits)
    
    return total
n = 123
print(f"Tổng các lập phương của các chữ số của {n} là: {cubesum(n)}")

# 2a
def cubesum(n):
    digits = str(n)
    total = sum(int(digit)**3 for digit in digits)
    return total

def PrintArmstrong(limit):
    for num in range(1, limit + 1):
        if num == cubesum(num):
            print(num)

PrintArmstrong(1000)

# 2b
def cubesum(n):
    digits = str(n)
    total = sum(int(digit)**3 for digit in digits)
    return total

def isArmstrong(n):
    return n == cubesum(n)

numbers_to_check = [153, 370, 371, 407, 123, 947]

for number in numbers_to_check:
    if isArmstrong(number):
        print(f"{number} là số Armstrong.")
    else:
        print(f"{number} không phải là số Armstrong.")