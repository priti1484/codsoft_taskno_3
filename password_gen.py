import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x400")
root.resizable(0,0)
root.title("Password Generator")
label = Label(root , text="Password Generator",fg="darkblue", font=("Arial",20,"bold","underline"))
label.grid(column=0,row=0,padx=150,pady=10)

def generate():
    try:
        char = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y','z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0','1','2','3','4','5','6','7','8','9','!','@','#','$','&','*']
        password = ""
        get_password.delete(0,END)
        for i in range(int(get_len.get())):
            password += random.choice(char) 
        get_password.insert(0,password)
   
    except:
        if user_input.get() =="":
            messagebox.showwarning("Warning","Please Enter user name ! and try again..")
        else:
            messagebox.showwarning("Password length","Please enter valid password length(number)!")

def accept():
    exit()

def reset():
    user_input.delete(0,END)
    get_len.delete(0,END)
    get_password.delete(0,END)


frame = Frame(root)
frame.grid(column=0,row=1)

user_name = Label(frame, text="Enter user name:", font=("Arial",20))
user_name.grid(column=0,row=0,sticky=E)

user_input = Entry(frame, font=("Arial",20))
user_input.grid(column=1,row=0)

password_len = Label(frame, text="Enter password length:", font=("Arial",20))
password_len.grid(column=0,row=1,sticky=E)

get_len = Entry(frame, font=("Arial",20))
get_len.grid(column=1,row=1)

generate_password = Label(frame, text="Generated Password:", font=("Arial",20))
generate_password.grid(column=0,row=2,sticky=E)

get_password = Entry(frame,font=("Arial",20))
get_password.grid(column=1,row=2)

btn_generate = Button(frame, text="Generate Password",font=("Arial",15,"bold"),bg="#41C9E2",command=generate)
btn_generate.grid(column=1,row=3,pady=10)

btn_accept = Button(frame, text="Accept",font=("Arial",15,"bold"),bg="#FF7ED4",command=accept)
btn_accept.grid(column=1,row=4,pady=10)

btn_reset = Button(frame, text="Reset",font=("Arial",15,"bold"),bg="#9F70FD",command=reset)
btn_reset.grid(column=1,row=5,pady=10)

root.mainloop()