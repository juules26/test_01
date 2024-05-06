import tkinter as tk
from tkinter import ttk

def validate_number(number): # Just 1 digit number can be added
    return len(number)<=1

def create_design(window):
    window.geometry("500x500")
    window.title("My first GUI for a SUDOKU")
# create main frame
    main_frame = ttk.Frame()
    main_frame.pack()

# create subframe for the label + place it in main_frame(master)
    label_frame = ttk.Frame(main_frame)
    label_frame.pack()

# pack the label inside the label_frame(master)
    label = tk.Label(label_frame, text="SUDOKU", font=('Helvetica',15))
    label.pack(pady=20)

# Create Buttons for difficulty
    button_easy = tk.Button(
        label_frame,
        text="Dumb",
        background= "Green yellow",
        foreground="Black",
        activebackground="Green4",
        activeforeground="Black",
        width=10
        )
    button_easy.pack(pady=10,padx=10,side=tk.LEFT)
    button_medium = tk.Button(
        label_frame,
        text="Meh, okay",
        background= "gold2",
        foreground="Black",
        activebackground="chocolate3",
        activeforeground="Black",
        width=10
        )
    button_medium.pack(pady=10, padx=10, side=tk.LEFT)
    button_hard = tk.Button(
        label_frame,
        text="Good luck",
        background= "red2",
        foreground="Black",
        activebackground="black",
        activeforeground="red2",
        width=10
        )
    button_hard.pack(pady=10, padx=10, side=tk.LEFT)
    
# create a subframe for the grid frames
    grid_frame = ttk.Frame(main_frame)
    grid_frame.pack()

# create gird frames inside the grid frame(master)   
    for i in range(3):
        for j in range(3):
            frame = ttk.Frame(grid_frame, width=100, height=100, relief=tk.GROOVE, borderwidth=3)
            frame.grid(row=i, column=j, padx=1,pady=1)

            for x in range(3):
                for y in range(3):
                    background_color = "LightSkyBlue1"
                    num_entry = tk.Entry(frame,width=3,background=background_color,font=("Helvetica",12),justify="center",highlightthickness=1)
                    num_entry.grid(row=x, column=y, padx=1,pady=1)
                    vlcm = (window.register(validate_number), "%P")
                    num_entry.configure(validate="key",validatecommand=vlcm)
                    num_entry.config(insertbackground=background_color)

if __name__=="__main__":
    window = tk.Tk()
    create_design(window)
    window.mainloop()
    

