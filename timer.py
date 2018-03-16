import tkinter as tk

counter = -1;
def inc_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
main = tk.Tk()
main.title("Incrementing Numbers")
text_label = tk.Label(main, fg="black")
text_label.pack()
inc_label(text_label)
button = tk.Button(main, text='Stop', width=25, command=main.destroy)
button.pack()
main.mainloop()