#cau a
print("Các số nguyên tố từ 100 đến 1000 là:")
for num in range(100, 1001):
    if num > 1:
        n = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                n = False
                break
        if n:
            print(num, end=" ")

#cau b
print("Các số chính phương từ 1 đến 1000 là:")
for num in range(1, 1001):
    if int(num**0.5)**2==num:
        print(num, end=" ")

#cau c
print("chuỗi số Fibonacci nhỏ hơn 100 là: ")
a,b=0, 1
for i in range(1,100):
    print(a,end=" ")
    a,b=b,a+b
    if a>100:
        break    

#cau d
print("các số hoàn hảo bé hơn 500 là: ")
for i in range(1,500):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i,end=" ")
 
