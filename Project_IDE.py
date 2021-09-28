from tkinter import *                
from tkinter.filedialog import asksaveasfile, askopenfilenames,askopenfilename, asksaveasfilename ,asksaveasfile  
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as tmsg
from typing import Any
from PIL import Image,ImageTk
import subprocess



# Inatializing tkinter window setup

root = Tk()
root.title("Python IDE")      
root.configure(bg="Black")
root.geometry("1300x800")
root.minsize(700,600)
root.maxsize(1520,770)


file_path = ""
code = ""

# File Handeling

def New_File(event=None):
    global code , file_path
    New = asksaveasfile(filetypes=[("Python Files","*.py")])
    file_path = New
    

    with open(New,"r") as NewFile :
        code = NewFile.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)

root.bind("<Control-n>",New_File)                  # Bind mouse controls to commands

def Open_File(event=None):

    class OpenFiles:

        global code , file_path
        openfile = askopenfilename(filetypes=[("Python File","*.py")])
        file_path = openfile

        with open(openfile,"r") as file :
            code = file.read()
            editor.delete(1.0, END)
            editor.insert(1.0, code)
    OpenObj = OpenFiles()
    fileTrace = OpenObj.file_path

root.bind("<Control-o>",Open_File)             # Bind mouse controls to commands



def Save(event=None):
    global code, file_path

    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path = save_path
    else:
        save_path = file_path


    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)
        tmsg.showinfo("Saved","Python File Saved Succesfully!")    
root.bind("<Control-s>",Save)                            # Bind mouse controls to commands
       
def Save_As(event=None):
    global code, file_path
    code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
root.bind("<Control-S>", Save_As)                          # Bind mouse controls to commands

def Close(event=None):

    User_Reply = tmsg.askquestion("Confirmation","Close this Python IDE?")


    if User_Reply == "yes":
        exit()

    elif User_Reply == "no" :
        tmsg.showinfo(":)","Let's continue with your programming")   # Notification

root.bind("<Control-q>",Close)                                 # Bind mouse controls to commands

def Cut():
    editor.event_generate(("<<Cut>>"))                         

def Copy():
    editor.event_generate(("<<Copy>>"))

def Paste():
    editor.event_generate(("<<Paste>>"))

def Run(event=None):
    
    global code ,file_path

    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path = save_path
    else:
        save_path = file_path


    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)

    code = editor.get(1.0, END)
    exec(code)

    cmd = f"python {file_path}"

    # Calling Command prompt to Initialize python interpreter

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    oupt , er = process.communicate()    # Insert & Fetch user written code in created shell

    output.delete(1.0, END)
    output.insert(1.0, oupt)              
    output.insert(1.0, er)

root.bind("<F5>", Run)

# Configure Light Theme

def LT():                         
    editor.config(bg="white",fg="black")
    output.config(bg="white",fg="black")
    Sym.config(fg="Black",bg="white")
    f.config(bg="white")
    
    
# Configure Dark Theme   
def DT():
    editor.config(bg="black",fg="orange")
    output.config(bg="black",fg="white")
    Sym.config(fg="Orange",bg="black")
    f.config(bg="black")

    
# Initialise Code Colours   

def red():
    editor.config(fg="red")
def blue():
    editor.config(fg="blue")
def green():
    editor.config(fg="green")
def white():
    editor.config(fg="white")
def orange():
    editor.config(fg="orange")
def cyan():
    editor.config(fg="cyan")
def yellow():
    editor.config(fg="yellow")
def magenta():
    editor.config(fg="magenta")

# Initialise Output Colours 

def red1():
    output.config(fg="red")
def blue1():
    output.config(fg="blue")
def green1():
    output.config(fg="green")
def white1():
    output.config(fg="white")
def orange1():
    output.config(fg="orange")
def cyan1():
    output.config(fg="cyan")
def yellow1():
    output.config(fg="yellow")
def magenta1():
    output.config(fg="magenta")
    
# Help/Support     

def Help():
    tmsg.showinfo("Help","Python IDE provides you platform to enhance your programing skills\n\nPlease visit https://www.programiz.com/python-programming")


# Setting up Menu snd SubMenus 

M = Menu(root ,tearoff=0)
m1 = Menu(M , tearoff=0,font=("Helvetica",9))
m1.add_command(label="New File    Ctrl + N", command=New_File)
m1.add_command(label="Open File  Ctrl + O" ,command=Open_File)
m1.add_command(label="Save           Ctrl + S" ,command=Save)
m1.add_command(label="Save As" ,command=Save_As)
m1.add_command(label="Exit             Ctrl+Q" ,command=Close)
M.add_cascade(label="File",menu=m1)
root.configure(menu=M)


m2 = Menu(M,tearoff=0,font=("Helvetica",10))
m2.add_command(label="Cut",command=Cut)
m2.add_command(label="Copy",command=Copy)
m2.add_command(label="Paste",command=Paste)
M.add_cascade(label="Edit",menu=m2)
root.configure(menu=M)


m3 = Menu(M,tearoff=0,font=("Helvetica",10))
m3.add_command(label="Run Ctrl + F5",command=Run)
M.add_cascade(label="Run",menu=m3)
root.configure(menu=M)


m4 = Menu(M,tearoff=0,font=("Helvetica",10))
m4.add_command(label="Light Theme",command=LT)
m4.add_command(label="Dark Theme",command=DT)

mx = Menu(m4,tearoff=0,font=("",9))
mx.add_command(label="Red",font=("",9),command=red)
mx.add_command(label="Blue",font=("",9),command=blue)
mx.add_command(label="Green",font=("",9),command=green)
mx.add_command(label="White",font=("",9),command=white)
mx.add_command(label="Orange",font=("",9),command=orange)
mx.add_command(label="Cyan",font=("",9),command=cyan)
mx.add_command(label="Yellow",font=("",9),command=yellow)
mx.add_command(label="Magenta",font=("",9),command=magenta)


m4.add_cascade(label="Code Colour",menu=mx)
root.configure(menu=m4)

my = Menu(m4,tearoff=0,font=("",9))
my.add_command(label="Red",font=("",9),command=red1)
my.add_command(label="Blue",font=("",9),command=blue1)
my.add_command(label="Green",font=("",9),command=green1)
my.add_command(label="White",font=("",9),command=white1)
my.add_command(label="Orange",font=("",9),command=orange1)
my.add_command(label="Cyan",font=("",9),command=cyan1)
my.add_command(label="Yellow",font=("",9),command=yellow1)
my.add_command(label="Magenta",font=("",9),command=magenta1)

m4.add_cascade(label="Output Colour",menu=my)



M.add_cascade(label="View",menu=m4)
root.configure(menu=M)                         # Pack menus in Main Menu

m5 = Menu(M,tearoff=0,font=("Helvetica",10))
m5.add_cascade(label="Help",command=Help)
M.add_cascade(label="Help",menu=m5)
root.configure(menu=M)

# Scroll bar

editor = ScrolledText(root, height=18,wrap=None,bg="black",fg="Orange",font="Srif 17 bold")
editor.pack(fill=BOTH)
editor.focus()

# Output frame setup

f = Frame(root,width=200,height=4,bg="black")
f.pack(side=LEFT,fill=BOTH)
Sym = Label(f,text=">>>\n>>>\n>>>\n>>>\n>>>\n>>>\n>>>\n>>>\n>>>",font="srif 20 bold",bg="black",fg="orange")
Sym.pack(anchor="w")

# Scroll bar

output = ScrolledText(root,height=13,fg="white",bg="black",font="srif 16 bold")
output.pack(fill=BOTH)
output.focus()

root.mainloop()          
