import tkinter
from tkinter.constants import TRUE

from PIL import ImageTk,Image   #pip install pillow
from tkinter import StringVar,IntVar, Widget,scrolledtext,messagebox,filedialog
from tkinter import END
#define window

root = tkinter.Tk()
root.title("PyPad")
root.iconbitmap("icons/pypad.ico")
root.geometry("600x600")
root.resizable(0,0)

#define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"

root.config(bg=root_color)

#define functions
#dropdown need a event param
def change_font(event):
    if options_var.get() == "normal":
        my_font = (font_family.get(),size_var.get())
    else:
        my_font = (font_family.get(),size_var.get(),options_var.get())#

    #change the font
    input_text.config(font=my_font)

#make new note=>delete the input from scrolledtext widget [!]start is 1.0
def new_note():
    question = messagebox.askyesno("Are you sure?","Clear the workspace")
    if question == TRUE:
        input_text.delete("1.0",END)

def save_note():
    save_name = filedialog.asksaveasfilename(initialdir="./",title="Save Note",filetypes=(("Plain Text","*.txt"),("All Files","*.*")))
    with open(save_name,'w') as f:
        f.write(font_family.get()+ "\n")
        f.write(str(size_var.get()) + "\n")
        f.write(options_var.get() + "\n")
        
        f.write(input_text.get("1.0",END))

def open_note():
    
    open_name = filedialog.askopenfilename(initialdir="./",title="Open Note",filetypes=(("Plain Text","*.txt"),("All Files","*.*")))

    with open(open_name,'r') as f:
        input_text.delete("1.0",END)
        font_family.set(f.readline().strip())
        size_var.set(int(f.readline().strip()))
        options_var.set(f.readline().strip())

        #I dont know why this function need a argument....(Marco: kamikaze häschen?)
        change_font(1)
        
        text = f.read()
        input_text.insert("1.0",text)
        

#---Define Layour--#

#define frames
menu_frame = tkinter.Frame(root,bg=menu_color)
text_frame = tkinter.Frame(root,bg=text_color)

menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

#Menu : new, open, save, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open("icons/new.ico"))
new_btn = tkinter.Button(menu_frame,image=new_image,command=new_note)
new_btn.grid(row=0,column=0,padx=5,pady=5)

open_image = ImageTk.PhotoImage(Image.open("icons/open.ico"))
open_btn = tkinter.Button(menu_frame,image=open_image,command=open_note)
open_btn.grid(row=0,column=1,padx=5,pady=5)

save_image = ImageTk.PhotoImage(Image.open("icons/save.ico"))
save_btn = tkinter.Button(menu_frame,image=save_image,command=save_note)
save_btn.grid(row=0,column=2,padx=5,pady=5)

#list of fonts
families = ["Terminal","Modern","Script","SimSun"]
font_family = StringVar()
font_family_dropdown = tkinter.OptionMenu(menu_frame,font_family,*families,command=change_font)
font_family.set("SimSun")
font_family_dropdown.config(width=15)
font_family_dropdown.grid(row=0,column=3)

#list of font size
size = [10,12,14,16]
size_var = IntVar()
size_dropdown = tkinter.OptionMenu(menu_frame,size_var,*size,command=change_font)
size_dropdown.config(width=10)
size_var.set(12)
size_dropdown.grid(row=0,column=4)

#list of options
options = ["bold","italic","normal"]
options_var = StringVar()
options_dropdown = tkinter.OptionMenu(menu_frame,options_var,*options,command=change_font)
options_var.set("normal")
options_dropdown.config(width=10)
options_dropdown.grid(row=0,column=5)

#layout text frame
picked_font = (font_family.get(),size_var.get())
input_text = tkinter.scrolledtext.ScrolledText(text_frame,bg=text_color,font=picked_font,width=100,height=100)
input_text.pack()
root.mainloop()