import tkinter as tk
from tkinter import messagebox

def chuyen_doi():
    try:
        n = int(entry_n.get())
        n_32 = n & 0xFFFFFFFF
        binary = format(n_32, 'b')
        hexa = format(n_32, 'X')
        result_bin.config(text="Nhị phân: " + binary)
        result_hex.config(text="hexa: " + hexa)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ!")
linh = tk.Tk()
linh.title("Chuyển đổi số")
linh.geometry("400x250")

tk.Label(linh, text="Nhập số nguyên n (có dấu):", font=("Arial", 10)).pack(pady=10)
entry_n = tk.Entry(linh, font=("Arial", 12), justify="center")
entry_n.pack()

tk.Button(linh, text="CHUYỂN ĐỔI", command=chuyen_doi, bg="blue", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

result_bin = tk.Label(linh, text="", fg="blue")
result_bin.pack()

result_hex = tk.Label(linh, text="", fg="red")
result_hex.pack(pady=5)

linh.mainloop()