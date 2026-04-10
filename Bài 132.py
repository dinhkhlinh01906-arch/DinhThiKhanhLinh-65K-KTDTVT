import tkinter as tk
from tkinter import messagebox
def check_strings():
    
    string_a = entry_a.get().strip().lower()
    string_b = entry_b.get().strip().lower()

    if not string_a or not string_b:
        print("Thông báo", "Vui lòng nhập cả hai chuỗi!")
        return

    
    if set(string_a) == set(string_b):
        result_label.config(text="Tạo từ cùng các ký tự", fg="green")
    else:
        result_label.config(text="Không tạo từ cùng các ký tự", fg="red")


linh = tk.Tk()
linh.title("Bài 132: Kiểm tra chuỗi ký tự")
linh.geometry("400x250")


tk.Label(linh, text="Nhập chuỗi a:", font=("Arial", 11)).pack(pady=5)
entry_a = tk.Entry(linh, font=("Arial", 11), width=30)
entry_a.pack()

tk.Label(linh, text="Nhập chuỗi b:", font=("Arial", 11)).pack(pady=5)
entry_b = tk.Entry(linh, font=("Arial", 11), width=30)
entry_b.pack()

check_button = tk.Button(linh, text="Kiểm tra", command=check_strings, 
                         font=("Arial", 11, "bold"), bg="#4CAF50", fg="white")
check_button.pack(pady=20)

result_label = tk.Label(linh, text="", font=("Arial", 12, "bold"))
result_label.pack()

linh.mainloop()