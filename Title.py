from tkinter import Tk

#create the Application and master frame
class Application(tk.Frame):
  def __init__(self, master=NONE):
    #remember parent to child relationship with master
    super().__init__(master)
    background_image = tk.PhotoImage(file='C:\Users\hp\Downloads\seven_pointed.gif')
    background_label = tk.LabelIself, image = background_image)
    self.pack()
    self.create_buttons()
  
  #create the buttons for each category
  def create_buttons(self):
    self.plants = tk.Button(self, text = "Plants")
    self.pack(side = "top")
root = tk.Tk()
app = Application(master=root)
app.mainloop()
