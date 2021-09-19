import tkinter as tk

def dict_to_gui():
    # fahrenheit = ent_temperature.get()
    # celsius = (5/9) * (float(fahrenheit) - 32)
    # lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    cut_dict =  {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}
    lb['text'] = '\n'.join('{} {}'.format(k, d) for k, d in cut_dict.items())

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# Set-up the window
window = tk.Tk()
window.title("CutCalculator")
window.resizable(width=False, height=False)
# window.geometry("800x600")
window.configure(bg='green')

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
lb = tk.Label(window, text='', pady=150)

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
# ent_temperature.grid(row=0, column=0, sticky="e")
# lbl_temp.grid(row=0, column=1, sticky="w")
# lb.grid(row=1,column=1, sticky='s')

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="Confirm",
    command=dict_to_gui,
    pady=100
)


# Set-up the layout using the .grid() geometry manager
# frm_entry.grid(row=0, column=0, padx=300)
# btn_convert.grid(row=0, column=1, pady=100)
# lbl_result.grid(row=0, column=2, padx=10)

# Run the application
center(window)
window.mainloop()