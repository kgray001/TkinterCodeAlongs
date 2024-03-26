import tkinter as tk

window = tk.Tk()
window.title("My App")

# Below on the background, thats how you use a color code to do your own color

label1 = tk.Label(
    window, 
    text = "Hello, Tkinter",
    foreground = "white",
    background = "#34A2FE",
    width = 20,
    height = 10
)
label1.pack()

button1 = tk.Button(
    window,
    text = "Click me!",
    fg = "blue",
    bg = "red"
)
# can do the foreground, background, width, and height as well with buttons. fg = foreground. bg = background
button1.pack()

entry1 = tk.Entry(
    window
)
entry1.pack()

entry1.insert(0, "World")
entry1.insert(0, "Hello ")

some_text = entry1.get()
print(some_text)

entry1.delete(0)
# it is inclusive 
entry1.delete(0, 4)
entry1.delete(0, tk.END)

window.mainloop()