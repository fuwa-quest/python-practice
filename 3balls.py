import tkinter as tk

balls = [
    {"x" : 400,"y" : 300,"mae" : None,"dx" : 1,"dy" : 1,"color":"red"},
    {"x" : 200,"y" : 100,"mae" : None,"dx" : -1,"dy" : 1,"color":"green"},
    {"x" : 100,"y" : 200,"mae" : None,"dx" : 1,"dy" : -1,"color":"blue"}]
    
def move():
    global balls
    for b in balls:
        if b["mae"] is not None:
            canvas.delete(b["mae"])
        
        b["x"] = b["x"] + b["dx"]
        b["y"] = b["y"] + b["dy"]
        b["mae"] = canvas.create_oval(b["x"] - 20, b["y"] - 20,
                                  b["x"] + 20,b["y"] + 20, fill=b["color"],width=0)

        if b["x"] >= canvas.winfo_width():
            b["dx"] = -1
        if b["x"] <= 0:
            b["dx"] = +1

        if b["y"] >= canvas.winfo_height():
            b["dy"] = -1
        if b["y"] <= 0:
            b["dy"] = +1
    
    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg="white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()
