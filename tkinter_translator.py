from tkinter import *


app = Tk()

container = Frame(master=app)
container.pack(padx=10,pady=10,fill="both", expand=True)

button1 = Button(master=container, text="Click Me!1")
button2 = Button(master=container, text="Click Me!2")
button3 = Button(master=container, text="Click Me!3")

button1.pack(padx=10,pady=10,fill="both", expand=True)
button2.pack(padx=10,pady=10,fill="both", expand=True)
button3.pack(padx=10,pady=10,fill="both", expand=True)

app.mainloop()