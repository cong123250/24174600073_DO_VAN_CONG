n = int(input("Nhập một số nguyên dương: "))
total = 0
for i in range(1, n):
    if n % i == 0:  
        total += i  
if total == n:
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")