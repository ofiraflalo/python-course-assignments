import tkinter as tk
from ph_library import calculate_ph

def calculate():
    try:
        h_concentration = float(entry.get())
        ph = calculate_ph(h_concentration)
        result_label.config(text=f"The pH is: {ph:.2f}")
    except ValueError as error:
        result_label.config(text=f"Error: {error}")

window = tk.Tk()
window.title("pH Calculator")

label = tk.Label(window, text="Enter hydrogen ion concentration [H+] in mol/L:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Calculate pH", command=calculate)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
