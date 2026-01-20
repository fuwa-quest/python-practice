import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg="white")
canvas.place(x = 0, y = 0)

canvas.create_oval(300 - 20, 200 - 20, 300 + 20,200 + 20, fill="red", width=0)

root.mainloop()
