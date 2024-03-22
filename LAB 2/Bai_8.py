x1,x2 = map(int, input(" nhập hệ số đường thẳng thứ 1: ").split())
y1,y2 = map(int, input(" nhập hệ số đường thẳng thứ 2: ").split())
if x1 != 0 and y1 != 0:
    if x1 == y1:
        print(" hai đường thẳng song song nhau ")
    elif x1 != y1:
        if x1 * y1 == -1:
            print("Hai đường thẳng vuông góc nhau")
        else:
            print("Hai đường thẳng cắt nhau")
else:
    print("Hệ số góc phải khác 0") 