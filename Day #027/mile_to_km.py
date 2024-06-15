# Miles to Km Converter using Tkinter GUI
from tkinter import *
FONT = ('Courier New', 12, 'normal')

# Button command
def calculate():
    res = int(number.get()) * 1.609
    result.config(text=res)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry
number = Entry(width=10)
number.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)

# Button
calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)

window.mainloop()
