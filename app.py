import tkinter

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



root.mainloop()