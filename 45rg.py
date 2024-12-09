a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
d = float(input("Nhập hệ số d: "))
if a == 0:
    print("Đây không phải là phương trình bậc 3.")
else:
    print("Phương trình đạo hàm bậc 2 f'(x) = 3*a*x^2 + 2*b*x + c")
    print(f"f'(x) = {3*a}x^2 + {2*b}x + {c}")
    delta = (2*b)**2 - 4*(3*a)*(c) 
    if delta < 0:
        print("Phương trình không có cực trị thực.")
    elif delta == 0:
        x = -2*b / (2*3*a)  
        print(f"Có một cực trị tại x = {x}")
    else:
        x1 = (-2*b - delta**0.5) / (2*3*a) 
        x2 = (-2*b + delta**0.5) / (2*3*a) 
        print(f"Có hai cực trị tại x1 = {x1} và x2 = {x2}")
    
        f_x1 = a*x1**3 + b*x1**2 + c*x1 + d
        f_x2 = a*x2**3 + b*x2**2 + c*x2 + d
        print(f"Giá trị của hàm số tại x1: f(x1) = {f_x1}")
        print(f"Giá trị của hàm số tại x2: f(x2) = {f_x2}")