from tkinter import *
from PIL import Image, ImageTk as itk
import mysql.connector as db


def issue_book():

    root = Tk()
    root.title("Library Management System - Issue Book")
    root.geometry("720x480")

    # Database Connection
    cnx = db.connect(host="localhost", user="root", password="", database="Library")
    cur = cnx.cursor()

    header = Frame(root, bg="#FCFFFD")
    header.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    headingLabel = Label(header, text="Issue Books", bg='#FCFFFD', fg='#5D737E', font=('Calibri', 16))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    form = Frame(root, bg='#DAFFEF')
    form.place(relx=0, rely=0.2, relwidth=1, relheight=1)

    root.mainloop()
