from tkinter import *
import os
import argparse
from argparse import ArgumentParser
from pathlib import *


parser = argparse.ArgumentParser()  # txt file with login and password
parser.add_argument(
        "--path",
        type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "loginpassfile.txt",
        help="Path to the pass file",
    )
parser.add_argument(
        "--prog",
        type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "pathfile.txt",
        help="Path to the path file",
    )
allowed_credentials = parser.parse_args()
scenarions = parser.parse_args()



def on_closing():  # function for frame update
    app.update()


def password_check():  # function for login and password check
    readlog = login.get()  # reads login from EntryBox
    readpass=password.get()  # reads password from EntryBox
    fi = open(allowed_credentials.path)  # open txt file
    for line in fi:  # reads file by line
        log = (line[:line.find(":")].strip())  # take login from file(first part (log)) log : pass
        pas = (line[line.find(":") + 1: ].strip())  # take password from file(second part (pass)) log : pass
        if readpass==pas and readlog == log:  # password and login check
            app.destroy()  # closes frame
            f = open(scenarions.prog)  # open file with any paths
            for line in f:
                os.startfile(line.strip())  # starts something that you specified in the file
            f.close()  # closes file


app = Tk()  # Create frame
app.attributes("-topmost", True)
app.attributes("-fullscreen",True)
login = StringVar()
password = StringVar()
loginEntry = Entry(app, textvariable=login, justify = CENTER)
passEntry = Entry(app, textvariable=password, show='*', justify = CENTER)
app.bind("<Return>", lambda event: password_check())
submit = Button(app, text='Sign In',command=password_check)


# places for EntryBox and Button
loginEntry.place(width=150,height=50,x=800,y=300)
passEntry.place(width=150,height=50,x=800,y=350)
submit.place(width=150,height=50,x=800,y=400)


app.protocol("WM_DELETE_WINDOW", on_closing)  # when you try to close the window, function starts
app.mainloop()
