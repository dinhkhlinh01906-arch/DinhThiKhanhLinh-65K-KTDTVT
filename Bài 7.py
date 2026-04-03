import tkinter as tk
from tkinter import messagebox

def giai_phuong_trinh():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            if b == 0:
                kq.set("Vô số nghiệm")
            else:
                kq.set("Vô nghiệm")
        else:
            x = -b / a
            kq.set(f"x = {x:.2f}")        
    except:
        messagebox.showerror("Lỗi nhập dữ liêu", "Vui lòng nhập số thực!")

linh = tk.Tk()
linh.title("Giải phương trình ax + b = 0")
linh.geometry("300x200")

tk.Label(linh, text="Nhập hệ số a:").pack(pady=5)
entry_a = tk.Entry(linh)
entry_a.pack()

tk.Label(linh, text="Nhập hệ số b:").pack(pady=5)
entry_b = tk.Entry(linh)
entry_b.pack()

tk.Button(linh, text="Giải", command=giai_phuong_trinh).pack(pady=10)

kq = tk.StringVar()
tk.Label(linh, textvariable=kq, fg="blue").pack()

linh.mainloop()