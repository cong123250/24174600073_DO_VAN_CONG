#câu lệnh vòng lặp while
n = 10
while n > 2: #True
    print(f"chay vong lap {n}")
    n = n - 1
    if n == 6:
        break
#Tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng 20
n = 20
while True:
    for i in range(n):
        if n%i==0 and i!=1 and i!=n:
            n = n - 1
            break
    else:
        break
    
    if n < 1:
        break

print(f"so nguyen to la {n}")
