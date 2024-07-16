from tkinter import *
from tkinter import messagebox

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("APP")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello Everyone!', bg='#fff', font=('calibri', 50, 'bold')).pack(expand=True)

    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Invalid username and password")

    elif password != '1234':
        messagebox.showerror("Invalid", "Invalid password")

    elif username != 'admin':
        messagebox.showerror("Invalid", "Invalid username")


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


def on_enter_password(e):
    code.delete(0, 'end')


def on_leave_password(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


root = Tk()
root.title('Login')
root.geometry("925x500+150+100")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file="login2.png")
Label(root, image=img, bg='white').place(x=20, y=20)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Login In', fg='#FF7F7F', bg='white', font=("Microsoft YaHei UI Light", 23))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign In', bg='#FF7F7F', fg='white', border=0, command=signin).place(x=35, y=204)
Label(frame, text="Don't have an account?", fg='black', bg='white', font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor='hand2', fg='#FF7F7F')
sign_up.place(x=215, y=270)

root.mainloop()
