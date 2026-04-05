import tkinter as tk
from tkinter import messagebox

def xu_ly_tap_hop():
    du_lieu_vao = entry.get()

    try:
        danh_sach_so = list(map(int, du_lieu_vao.split()))

        tap_hop_duy_nhat = []
        for so in danh_sach_so:
            if so not in tap_hop_duy_nhat:
                tap_hop_duy_nhat.append(so)

        ket_qua = ", ".join(map(str, tap_hop_duy_nhat))
        label_ket_qua.config(text=f"Tập hợp A: {{ {ket_qua} }}")

    except ValueError:
        print("Lỗi", "Vui lòng chỉ nhập các số cách nhau bởi dấu cách!") 

linh = tk.Tk()
linh.title("Bài 82: Lọc tập hợp số")
linh.geometry("400x200")  
                
tk.Label(linh, text="Nhập các số (cách nhau bằng dấu cách):").pack(pady=10)

entry = tk.Entry(linh, widt=40)
entry.pack(pady=5)

btn_xuly = tk.Button(linh, text="Tạo Tập Hợp", command=xu_ly_tap_hop)
btn_xuly.pack(pady=10)

label_ket_qua = tk.Label(linh, text="Tập hợp A: { }", font=("Arial", 10, "bold"))
label_ket_qua.pack(pady=10)

linh.mainloop()