#Jayda Fountain
from tkinter import *
from tkinter import ttk


#This function is for one of my scrollbars
def update_scrollregion(event):
  photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

#Setting up the main window
win = Tk( )
win.title("Cook Book Journal")

title = Label(win, text="Cook Book Journal", font=('Courier', 15))
addToCanvas = False

#Functions
#The add button function allows the user to add a new recipe
def add_button():
  root = Tk()
  root.geometry("500x500")
  new_title = Entry(root, width=35, borderwidth=5)
  new_title.grid(row=0, column=0, pady=40, padx=10)
  new_title.insert(0, "Enter Your Recipe Name: ")

  #Create the name of the recipe
  def recipe_click():
    global x
    button_pressed = "yes"
    enter = new_title.get()
    x = enter.replace("Enter Your Recipe Name: ", "")
    myLabel = Label(root, text=x + " is the name" + '\n' + "of your new recipe!" + '\n' + "Now let's add" + '\n' + "the steps.", font=("Arial", 16))
    myLabel.grid(row=1, column=2, columnspan=1)
    Recipe_name = x
    root.title(Recipe_name)
    clear()
    
  Button1 = Button(root, text="Confirm", command=recipe_click)
  Button1.grid(row=2, column=0, pady=20, padx=10)

  def clear():
    new_title.destroy()
    Button1.destroy()
    recipe_steps()

  #Creating the recipe steps
  def recipe_steps():
    global steps
    #Create a frame
    frame = Frame(root)
    #Create text widget
    steps = Text(root, height=22, width=30, spacing2=2, wrap=WORD)
    #Add the text Box
    steps.grid(row=1, column=0)
    #Adding some space at the top for designing purposes
    blank_space = Label(root, text="           ")
    blank_space.grid(row=0, column=0)
    #Create Scrollbar
    sb = Scrollbar(root, orient=VERTICAL)
    #Add the scrollbar and place it to the right
    sb.grid(row=1, column=1, sticky=NS)
    steps .config(yscrollcommand=sb.set)
    sb.config(command=steps.yview)
    confirm_button()

  #This function allows the user to click on the new recipe
  def newButtonPressed():
    global recipe_label, edit_button, delete_var
    bun = Tk()
    bun.title("Recipe Journal")

    bun.geometry("450x500")
    recipe_Frame = Frame(bun)

    def forget(widget):
      # This will remove the widget from toplevel
      # basically widget do not get deleted
      # it just becomes invisible and loses its position
      # and can be retrieve
      widget.grid_forget()
  
    # method to make widget visible
    def retrieve(widget):
      widget.grid(padx = 0, pady = 0, sticky="ns")

    #Edit and save button functions
    def saveButtonPressed():
      global recipe_label, data
      bun.geometry("450x500")

      forget(recipe_text)
      forget(save_button)
      forget(sb)

      data = recipe_text.get(1.0, END)
      recipe_label.config(text=data)

      retrieve(edit_button)
      retrieve(cancel_button)
      retrieve(recipe_title)
      retrieve(recipe_label)

      edit_button.grid(row=0, column=0, padx=0, pady=0, sticky="nw")
      cancel_button.grid(row=0, column=0, padx=300, pady=0, sticky="ne")
      recipe_title.grid(padx=0, pady=2, sticky="nw")
      recipe_label.grid(padx=0, pady=0, sticky="nw")
      
      
    def editButtonPressed():
      forget(recipe_title)
      forget(recipe_label)
      forget(edit_button)
      forget(cancel_button)

      global recipe_text, save_button, sb
      bun.geometry("350x500")
      
      scrollFrame = Frame(canvasFrame)
      save_button = Button(canvasFrame, text="Save", command=saveButtonPressed)
      recipe_text = Text(canvasFrame, height=22, width=30, spacing2=2, wrap=WORD)
      recipe_text.insert(1.0, data)

      sb = Scrollbar(canvasFrame, orient=VERTICAL)
      #Add the scrollbar and place it to the right
      sb.grid(row=3, column=1, sticky="ns")
      recipe_text.config(yscrollcommand=sb.set)
      sb.config(command=recipe_text.yview)

      save_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
      recipe_text.grid(row=3, column=0, padx=0, pady=5, sticky="nw")

    #What happens when the button is pressed
    def cancelButtonPressed():
      bun.destroy()

    def update_scrollregion(event):
      photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

    #Scrollbar
    photoFrame = Frame(bun, width=430, height=500)
    photoFrame.grid()
    photoFrame.rowconfigure(0, weight=1) 
    photoFrame.columnconfigure(0, weight=1) 

    photoCanvas = Canvas(photoFrame, width=430, height=500)
    photoCanvas.grid(row=0, column=0, sticky="nsew")

    canvasFrame = Frame(photoCanvas)
    photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw')

    photoScroll = Scrollbar(photoFrame, orient=VERTICAL)
    photoScroll.config(command=photoCanvas.yview)
    photoCanvas.config(yscrollcommand=photoScroll.set)
    photoScroll.grid(row=0, column=1, sticky="ns")

    canvasFrame.bind("<Configure>", update_scrollregion)

    #Layout
    recipe_title = Label(canvasFrame, text=x + " recipe:", font=("Arial", 25), justify=LEFT)
    cancel_button = Button(canvasFrame, text="Cancel", padx=35, justify=RIGHT, command=cancelButtonPressed)
    recipe_label = Label(canvasFrame, text=data, font=("Arial", 18), justify=LEFT, wraplength=400)
    edit_button = Button(canvasFrame, text="Edit Recipe", padx=100, command=editButtonPressed)

    edit_button.grid(row=0, column=0, padx=0, pady=0, sticky="nw")
    cancel_button.grid(row=0, column=0, padx=300, pady=0, sticky="ne")
    recipe_title.grid(padx=0, pady=2, sticky="nw")
    recipe_label.grid(padx=0, pady=0, sticky="nw")
    

  #This allows the user to confirm their recipe
  def confirm_action():
    global data, new_button, addToCanvas
    addToCanvas = True
    data = steps.get(1.0, END)

    new_button = Button(canvasFrame, text=x, padx=126, pady=75, command=newButtonPressed)
    new_button.grid(column=0, padx=5, sticky="nw")

    delete_root()

    if addToCanvas == True:
      no_recipes.destroy()

  def confirm_button():
    confirm = Button(root, text="Confirm", padx=20, pady=5, command=confirm_action)
    confirm.grid(row=2, column=2)

  def delete_root():
    root.destroy()


#Making a scrollbar for the main window
photoFrame = Frame(win, width=300, height=415)
photoFrame.grid()
photoFrame.rowconfigure(0, weight=1) 
photoFrame.columnconfigure(0, weight=1) 

photoCanvas = Canvas(photoFrame, width=300, height=415)
photoCanvas.grid(row=0, column=0, sticky="nsew")

canvasFrame = Frame(photoCanvas)
photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw')

photoScroll = Scrollbar(photoFrame, orient=VERTICAL)
photoScroll.config(command=photoCanvas.yview)
photoCanvas.config(yscrollcommand=photoScroll.set)
photoScroll.grid(row=0, column=1, sticky="ns")

canvasFrame.bind("<Configure>", update_scrollregion)


#Buttons
button_add = Button(canvasFrame, text="Add", padx=135, pady=5, command=add_button)


#No recipes label
no_recipes = Label(canvasFrame, text="You Have No" + '\n' + "Recipes Added Yet!", padx=35, font=("Arial", 18), fg='grey')


#Grid layout
button_add.grid(column=0, row=0, padx=0, pady=5, sticky="nw")
no_recipes.grid(column=0, padx=0, pady=200, sticky="nw")







win.mainloop()