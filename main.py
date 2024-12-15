import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='black', height=400, width=400)
for i in range(50,400,50):
    canvas.create_line((0, i), (600,i), fill='white')
    canvas.create_line((i, 0), (i, 600), fill='white')
canvas.pack()
tk.mainloop()
