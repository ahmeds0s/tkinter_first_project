import tkinter as tk


window = tk.Tk()
window.config(padx=100, pady=50)
window.grid()
window.anchor('center')
window.title('Miles to Km converter')
window.minsize(width=250, height=200)

input = tk.Entry(width=10)
input.grid(row=2, column=3)

label_miles = tk.Label(text='Miles')
label_miles.grid(row=2, column=4)

label_is_equal = tk.Label(text='is equal to')
label_is_equal.grid(row=3, column=2)

label_result = tk.Label(text='0')
label_result.grid(row=3, column=3)

label_unit = tk.Label(text='Km')
label_unit.grid(row=3, column=4)


def calculateresult():
    result = int(input.get()) * 1.6
    label_result.config(text=result)


button = tk.Button(text='Calculate', command=calculateresult)
button.grid(row=4, column=3)
button.grid(padx=20, pady=20)


window.mainloop()
