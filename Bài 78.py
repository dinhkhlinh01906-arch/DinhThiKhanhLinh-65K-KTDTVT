import tkinter as tk
from tkinter import messagebox
import random

def thuc_hien():
    try:
        n = int(entry_n.get())
        x = int(entry_x.get())
        
        if not (1 <= n <= 99):
            messagebox.showwarning("Lỗi", "Vui lòng nhập n trong khoảng [1, 99]")
            return
        mang = [random.randint(-100, 100) for _ in range(n)]
        lbl_goc.config(text=f"Mảng gôc: {mang}")

        mang.sort()
        lbl_sapxep.config(text=f"Mảng sắp xếp: {mang}")

        mang.append(x)
        mang.sort()
        lbl_chen.config(text=f"Mảng sau khi chèn {x}: {mang}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số nguyên!")

linh = tk.Tk()
linh.title("Quản lý mảng")  
linh.geometry("500x400")

tk.Label(linh, text="Nhập n (1-99):").pack(pady=5)
entry_n = tk.Entry(linh)
entry_n.pack()
 
tk.Label(linh, text="Nhập số x cần chèn:").pack(pady=5)
entry_x = tk.Entry(linh)
entry_x.pack()

btn = tk.Button(linh, text="Chạy Chương Trình", command=thuc_hien, bg="skyblue")
btn.pack(pady=15)

lbl_goc = tk.Label(linh, text="Mảng gốc: ", fg="blue")
lbl_goc.pack()

lbl_sapxep = tk.Label(linh, text="Mảng sắp xếp: ", fg="green")
lbl_sapxep.pack()

lbl_chen = tk.Label(linh, text="Mảng sau khi chèn: ", fg="red")
lbl_chen.pack()

linh.mainloop()