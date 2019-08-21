from tkinter import *
import os


loginpassfile = r"C:\Users\Prog_21\Desktop\D\LP.txt"  #txt file with login and password
inputfile = r"C:\Users\Prog_21\Desktop\D\InfoFile.txt"  #file with paths to your programs


def on_closing():  #function for frame update
    app.update()


def password_check(*args):  #function for login and password check
    readlog = login.get()  #reads login from EntryBox
    readpass=password.get()  #reads password from EntryBox
    fi = open(loginpassfile)  #open txt file
    for line in fi:  #reads file by line
        log = (line[:line.find(":")].strip())  #take login from file(first part (log)) log : pass
        pas = (line[line.find(":") + 1: ].strip())  #take password from file(second part (pass)) log : pass
        if readpass==pas and readlog == log:  #password and login check
            app.destroy()  #closes frame
            f = open(inputfile)  #open file with any paths
            for line in f:
                os.startfile(line.strip())  #starts something that you specified in the file
            f.close()  #closes file


app = Tk()  #Create frame
app.attributes("-topmost", True)
app.attributes("-fullscreen",True)
login = StringVar()
password = StringVar()
loginEntry = Entry(app, textvariable=login, justify = CENTER)
passEntry = Entry(app, textvariable=password, show='*', justify = CENTER)
app.bind("<Return>", lambda event: password_check())
submit = Button(app, text='Sign In',command=password_check)


#places for EntryBox and Button
loginEntry.place(width=150,height=50,x=800,y=300)
passEntry.place(width=150,height=50,x=800,y=350)
submit.place(width=150,height=50,x=800,y=400)


app.protocol("WM_DELETE_WINDOW", on_closing)  #when you try to close the window, function starts
app.mainloop()