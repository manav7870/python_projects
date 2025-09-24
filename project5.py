# DIGITAL CLOCK

from tkinter import Label,Tk
import time

app = Tk()
app.title("Digital Clock")
app.geometry("1000x300")
app.resizable(False, False)
app.configure(bg="black")

clock_label = Label(app,bg="black",fg="red",font=("Papyrus",50),relief="flat")
clock_label.place(x= 200, y= 200)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000,update_time)
update_time()
app.mainloop()    