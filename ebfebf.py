students = []

while True:
    print("\n--- Quản lý danh sách sinh viên ---")
    print("1. Xem danh sách sinh viên")
    print("2. Nhập thông tin sinh viên mới")
    print("3. Chỉnh sửa thông tin sinh viên")
    print("4. Xóa thông tin sinh viên")
    print("5. Thoát chương trình")
    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        print("\nDanh sách sinh viên:")
        if not students:
            print("Danh sách trống.")
        else:
            for student in students:
                print(f"Mã: {student['id']}, Họ đệm: {student['last_name']}, Tên: {student['first_name']}, "
                      f"Toán: {student['math']}, Lý: {student['physics']}, Hóa: {student['chemistry']}, "
                      f"Trung bình: {student['average']}")

    elif choice == "2":
        print("\nNhập thông tin sinh viên mới:")
        student = {}
        student['id'] = input("Mã sinh viên: ")
        student['last_name'] = input("Họ đệm: ")
        student['first_name'] = input("Tên: ")
        student['math'] = float(input("Điểm Toán: "))
        student['physics'] = float(input("Điểm Lý: "))
        student['chemistry'] = float(input("Điểm Hóa: "))
        student['average'] = round((student['math'] + student['physics'] + student['chemistry']) / 3, 2)
        students.append(student)
        print("Đã thêm sinh viên mới.")

    elif choice == "3":
        print("\nChỉnh sửa thông tin sinh viên:")
        edit_id = input("Nhập mã sinh viên cần chỉnh sửa: ")
        found = False
        for student in students:
            if student['id'] == edit_id:
                print(f"Đang chỉnh sửa sinh viên có mã {edit_id}.")
                student['last_name'] = input("Họ đệm mới (để trống nếu không thay đổi): ") or student['last_name']
                student['first_name'] = input("Tên mới (để trống nếu không thay đổi): ") or student['first_name']
                new_math = input("Điểm Toán mới (để trống nếu không thay đổi): ")
                if new_math:
                    student['math'] = float(new_math)
                new_physics = input("Điểm Lý mới (để trống nếu không thay đổi): ")
                if new_physics:
                    student['physics'] = float(new_physics)
                new_chemistry = input("Điểm Hóa mới (để trống nếu không thay đổi): ")
                if new_chemistry:
                    student['chemistry'] = float(new_chemistry)
                student['average'] = round((student['math'] + student['physics'] + student['chemistry']) / 3, 2)
                print("Đã cập nhật thông tin sinh viên.")
                found = True
                break
        if not found:
            print("Không tìm thấy sinh viên có mã đã nhập.")

    elif choice == "4":
        print("\nXóa thông tin sinh viên:")
        delete_id = input("Nhập mã sinh viên cần xóa: ")
        for i, student in enumerate(students):
            if student['id'] == delete_id:
                del students[i]
                print(f"Đã xóa sinh viên có mã {delete_id}.")
                break
        else:
            print("Không tìm thấy sinh viên có mã đã nhập.")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
