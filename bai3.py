ho_ten = input("Nhập vào họ tên đầy đủ: ")
danh_sach_tu = ho_ten.split()
ho = danh_sach_tu[0]
ten = danh_sach_tu[-1]
print(f"Họ: {ho}, Tên: {ten}")