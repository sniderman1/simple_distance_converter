import tkinter as tk
import tkinter.font as font
from tkinter import ttk


root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

meter_value = tk.StringVar()
feet_value = tk.StringVar(value="0.000")

def calculate_feet(*args):
    try:
        meters = float(meter_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet: .3f}")
    except ValueError:
        pass

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

#Widget Def

meters_label = ttk.Label(main, text="Meters: ")
meter_input = ttk.Entry(main, width=10, textvariable=meter_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_btn = ttk.Button(main, text="Calculate", command=calculate_feet)

#Grid Def

meters_label.grid(column=0, row=0, sticky="W")
meter_input.grid(column=1, row=0, sticky="EW")
meter_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_btn.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop() 