#imports
import tkinter as tk
import sys


#global variables

#booleans for keeping track of 2nd click
red_clicked=False
blue_clicked=False
#global root, used in handlers
root = tk.Tk()

#event handlers
def get_red():
    global red_clicked
    global root
    if red_clicked==True:
      root.destroy()
    else:
      root.configure(background = 'red')
      red_clicked=True

def get_blue(root):
    global blue_clicked
    if blue_clicked==True:
      root.destroy()
    else:
      root.configure(background = 'blue')
      blue_clicked=True

def get_green():
    root.configure(background = 'green')

def get_yellow():
    root.configure(background = 'yellow')

def main():

  #set up window
  global root
  frame = tk.Frame(root)
  frame.pack()

  #red/left button
  button = tk.Button(frame,
                     text="Red",
                     fg="red",
                     bg="black",
                     width=30,
                     height=15,
                     command=get_red)
  button.pack(side=tk.LEFT)

  #blue/right button
  slogan = tk.Button(frame,
                     text="Blue",
                     fg="blue",
                     bg="black",
                     width=30,
                     height=15,
                     command=get_blue)
  slogan.pack(side=tk.RIGHT)
  root.mainloop()#run loop for 1st window

  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()

  button = tk.Button(frame,
                     text="Green",
                     fg="green",
                     bg="black",
                     width=30,
                     height=15,
                     command=get_green)
  button.pack(side=tk.LEFT)

  slogan = tk.Button(frame,
                     text="Yellow",
                     fg="yellow",
                     bg="black",
                     width=30,
                     height=15,
                     command=get_yellow)
  slogan.pack(side=tk.RIGHT)
  root.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    main()
