from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Acharya Automated Attendence - Sahil")
# window.iconbitmap('#')

Label1 = Label(window, text="Welcome to Acharya Automated Attendence",
               fg='blue', font=("arial", 16, "bold"), relief='solid').pack()

f_name = Entry(window, width=30)
f_pass = Entry(window, width=30)

f_name.grid(row=0, column=0, padx=20)
f_pass.grid(row=0, column=0)

window.mainloop()
