import tkinter as tk

x = 400
y = 300

mae = None
def move():
    global x,y,mae
    if mae is not None:
        canvas.delete(mae)
    x = x + 1
    mae = canvas.create_oval(x - 20, y - 20,x + 20,y + 20, fill="red",width=0)
    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg="white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()
