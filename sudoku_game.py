import tkinter as tk
from tkinter import ttk

def create_design(window):
    window.geometry("500x550")
    window.title("My first GUI for a SUDOKU")
# create main frame
    main_frame = ttk.Frame(window)
    main_frame.pack()

# create subframe for the label + place it in main_frame(master)
    label_frame = ttk.Frame(main_frame)
    label_frame.pack()

# pack the label inside the label_frame(master)
    label = tk.Label(label_frame, text="SUDOKU", font=('Arial',15))
    label.pack(pady=20)

# create a subframe for the grid frames
    grid_frame = ttk.Frame(main_frame)
    grid_frame.pack()

# create gird frames inside the grid frame(master)   
    for i in range(3):
        for j in range(3):
            frame = ttk.Frame(grid_frame, width=150, height=150, relief=tk.GROOVE)
            frame.grid(row=i, column=j)


    


if __name__=="__main__":
    window = tk.Tk()
    create_design(window)
    window.mainloop()
    

