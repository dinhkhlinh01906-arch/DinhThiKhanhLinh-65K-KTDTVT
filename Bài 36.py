import tkinter as tk
from tkinter import messagebox

def la_so_nguyen_to(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True
def xu_ly():
    try:
        n = int(entry.get())    
        danh_sach = []
        so = 2
        while len(danh_sach) < n:
            if la_so_nguyen_to(so):
                danh_sach.append(str(so))
            so += 1
        lbl_ket_qua.config(text=" ".join(danh_sach))
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên!")
        
linh = tk.Tk()
linh.title("Giải Bài 36")
linh.geometry("450x250")

tk.Label(linh, text="Nhập n số nguyên tố cần in:", font=("Aeial", 11)).pack(pady=10)
entry = tk.Entry(linh, font=("Arial", 12))
entry.pack()
tk.Button(linh, text="Chạy Ngay", command=xu_ly, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

lbl_ket_qua = tk.Label(linh, text="", wraplength=400, font=("Arial", 10), fg="blue")
lbl_ket_qua.pack()

linh.mainloop()
  