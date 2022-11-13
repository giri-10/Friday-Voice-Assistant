#login
from tkinter import *
from tkinter import messagebox


def Login_Info():
    user_name = e1.get()
    password = e2.get()
 
    if(user_name == "" and password == "") :
        messagebox.showinfo("", "Please enter username and password")
 
 
    elif(user_name == "mvj1" and password == "1234"):
 
        messagebox.showinfo("","Login Successfull!")
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrect Username and Password")
 
 
root = Tk()
root.title("Login: Jarvis")
root.iconbitmap(r'C:\\Users\\Giridharan U\\Downloads\\j.ico')


# bgimg= tk.PhotoImage(file = r'C:\\Users\\Giridharan U\\Downloads\\download.ppm')
# limg= Label(root, i=bgimg)
# limg.pack()



root.geometry("350x200")
global e1
global e2
 
Label(root, text="User name").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Login_Info ,height = 2, width = 10).place(x=10, y=100)
 
root.mainloop()
