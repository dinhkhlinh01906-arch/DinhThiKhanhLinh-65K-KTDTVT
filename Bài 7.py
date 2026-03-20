import tkinter as tk
from tkinter import messagebox

# 1. Hàm xử lý logic khi nhấn nút Giải
def giai_phuong_trinh():
    try:
        # Lấy giá trị từ ô nhập và chuyển sang số thực
        val_a = float(entry_a.get())
        val_b = float(entry_b.get())
        
        if val_a != 0:
            result = f"Nghiệm x = {-val_b / val_a}"
        elif val_b == 0:
            result = "Vô số nghiệm"
        else:
            result = "Vô nghiệm"
            
        # Hiển thị kết quả lên Label
        label_kq.config(text=result, fg="blue")
    except ValueError:
        # Hiển thị thông báo nếu người dùng nhập chữ thay vì số
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# 2. Thiết lập cửa sổ chính
root = tk.Tk()
root.title("Giải phương trình ax + b = 0")
root.geometry("300x250")

# 3. Tạo các thành phần giao diện (Widgets)
tk.Label(root, text="Nhập a:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Nhập b:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

btn_giai = tk.Button(root, text="Giải ngay", command=giai_phuong_trinh, bg="orange")
btn_giai.pack(pady=20)

label_kq = tk.Label(root, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 10, "bold"))
label_kq.pack()

# Chạy ứng dụng
root.mainloop()
