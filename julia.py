#git status
#git add archivo
#git add 
#git commit 
#git push origin main

import tkinter as tk

root = tk.Tk()
root.geometry("400x350")
#root.minsize(300,300)
root.title("My first GUI")


label = tk.Label(root, text="Title for This", font=('Arial',15))
label.pack(padx=10, pady=10)

textbox = tk.Text(root, width=40, height=10, font=('Arial',12))
textbox.pack(pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 10))
btn1.grid(row=0, column=0, sticky="nsew")

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 10))
btn2.grid(row=0, column=1, sticky="nsew")

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 10))
btn3.grid(row=0, column=2, sticky="nsew")

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 10))
btn4.grid(row=1, column=0, sticky="nsew")

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 10))
btn5.grid(row=1, column=1, sticky="nsew")

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 10))
btn6.grid(row=1, column=2, sticky="nsew")


buttonframe.pack()

button = tk.Button(root, text="Clikea", font=('Arial', 12))
button.pack(pady=10)

root.mainloop()