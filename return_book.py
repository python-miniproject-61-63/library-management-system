from tkinter import *
from PIL import Image, ImageTk as itk
import mysql.connector as db


def return_book():
    # global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("Library Management System - Return Book")
    root.geometry("720x480")

    # Database Connection
    cnx = db.connect(host="localhost", user="root", password="", database="Library")
    cur = cnx.cursor()

    header = Frame(root, bg="#FCFFFD")
    header.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    headingLabel = Label(header, text="Return Books", bg='#FCFFFD', fg='#5D737E', font=('Calibri', 16))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    form = Frame(root, bg='#DAFFEF')
    form.place(relx=0, rely=0.2, relwidth=1, relheight=1)

    root.mainloop()
