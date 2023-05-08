import tkinter as tk

root = tk.Tk()

# root.iconbitmap("./bookshelf.ico")

root.title("Book Store")


def change_text():
    name = entry.get()
    new_text = "Witaj " + entry.get()
    who = "\nJesteś: " + radio_var.get()
    languages = "\nZnasz następujące języki progrmamowania:\n"
    for i in range(len(checkbox_vars)):
        if checkbox_vars[i].get() == 1:
            languages = languages + " " + checkboxes[i].cget("text")

    experience = "\nmasz " + str(slider.get()) + " lat doświadczenia."
    label.config(text=new_text + who + languages + experience)


screen_width = 1800
screen_height = 1800
root.geometry(f"{int(screen_width / 2)}x{int(screen_height / 2)}")

left_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=int(screen_width / 6), height=int(screen_width / 2))
left_frame.pack(side="left", padx=10, pady=10)
left_frame.pack_propagate(0)
right_frame = tk.Frame(root, width=int(screen_width / 4), height=left_frame["height"], borderwidth=4, relief="ridge")
right_frame.pack(side="right", padx=10, pady=10)
right_frame.pack_propagate(0)

root.resizable(width=False, height=False)

entry = tk.Entry(left_frame)
entry.pack(anchor="w", padx=10, pady=10)

label = tk.Label(right_frame, text="podaj dane")
label.pack(padx=10, pady=10)

radio_var = tk.StringVar(value=" ")
radio_button1 = tk.Radiobutton(left_frame, text="tester", variable=radio_var, value="testerem")
radio_button1.pack(anchor="w", padx=10, pady=10)

radio_button2 = tk.Radiobutton(left_frame, text="programista", variable=radio_var, value="programista")
radio_button2.pack(anchor="w", padx=10, pady=10)

button = tk.Button(left_frame, text="Ok", command=change_text)
button.pack(anchor="center", padx=10, pady=10)

checkbox_vars = []
checkboxes = []

checkbox_vars.append(tk.IntVar())
checkbox = tk.Checkbutton(left_frame, text="java", variable=checkbox_vars[0])
checkbox.pack(anchor="w", padx=10, pady=10)
checkboxes.append(checkbox)
checkbox_vars.append(tk.IntVar())
checkbox2 = tk.Checkbutton(left_frame, text="python", variable=checkbox_vars[1])
checkbox2.pack(anchor="w", padx=10, pady=10)
checkboxes.append(checkbox2)

slider = tk.Scale(left_frame, from_=0, to=25, orient=tk.HORIZONTAL)
slider.pack(anchor="w", padx=10, pady=10)

root.mainloop()
