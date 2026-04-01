import tkinter as tk

def convert():
    try:
        n = int(entry.get())

        # Đưa về dạng 32-bit (bù 2)
        n_32 = n & 0xFFFFFFFF

        # Nhị phân 32 bit
        binary = format(n_32, '032b')

        # Hex
        hexa = format(n_32, '08X')

        result_bin.config(text="Nhị phân: " + binary)
        result_hex.config(text="Hex: " + hexa)

    except:
        result_bin.config(text="Lỗi nhập!")
        result_hex.config(text="")

# Tạo cửa sổ
root = tk.Tk()
root.title("Chuyển đổi số")

# Nhập liệu
tk.Label(root, text="Nhập số nguyên:").pack()
entry = tk.Entry(root)
entry.pack()

# Nút bấm
tk.Button(root, text="Chuyển đổi", command=convert).pack()

# Kết quả
result_bin = tk.Label(root, text="")
result_bin.pack()

result_hex = tk.Label(root, text="")
result_hex.pack()

root.mainloop()