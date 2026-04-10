import tkinter as tk
import math

def kiem_tra():
    c1 = [float(i) for i in entry1.get().split()] # [x1, y1, r1]
    c2 = [float(i) for i in entry2.get().split()] # [x2, y2, r2]
    d = math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    r1, r2 = c1[2], c2[2]

    if d == 0 and r1 == r2:
        kq = "Trùng nhau"
    elif d > r1 + r2:
        kq = "Ở ngoài nhau"
    elif d < abs(r1 - r2):
        kq = "Trong nhau"
    else:
        kq = "Cắt nhau hoặc tiếp xúc"

    lbl_kq.config(text="Kết quả: " + kq)

linh = tk.Tk()
linh.title("Bài 166")
linh.geometry("500x300")

tk.Label(linh, text="Nhập xc, yc, R của C1:").pack()
entry1 = tk.Entry(linh)
entry1.pack()

tk.Label(linh, text="Nhập xc, yc, R của C2:").pack()
entry2 = tk.Entry(linh)
entry2.pack()

tk.Button(linh, text="Xác định vị trí", command=kiem_tra).pack()
lbl_kq = tk.Label(linh, text="...", fg="blue")
lbl_kq.pack()

linh.mainloop()