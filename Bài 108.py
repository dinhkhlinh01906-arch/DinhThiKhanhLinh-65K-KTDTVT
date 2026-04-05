import tkinter as tk
from tkinter import messagebox

def ve_ma_tran():
    n = int(entry.get())
    for con in frame.winfo_children(): con.destroy()

    mt = [[0] * n for _ in range(n)]
    t, b, l, r, num = 0, n-1, 0, n-1, 1

    while num <= n*n:
        for i in range(1, r +1): mt[t][i] = num; num += 1
        t += 1
        for i in range(t, b + 1): mt[i][r] = num; num += 1
        r -= 1
        for i in range(r, 1 - 1, -1): mt[b][i] = num; num += 1
        b -= 1
        for i in range(b, t -1, -1): mt[i][1] = num; num +=1
        l += 1

    for i in range(n):
        for j in range(n):
            tk.Label(frame, text=mt[i][j], width=4, relief="solid").grid(row=i, column=j)     
    
linh = tk.Tk()
linh.title("Ma trận xoắn ốc")
linh.geometry("500x300")

entry = tk.Entry(linh)
entry.pack(pady=5)
tk.Button(linh, text="Vẽ", command=ve_ma_tran).pack()
frame = tk.Frame(linh)
frame.pack(pady=10)

linh.mainloop()