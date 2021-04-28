from tkinter import *
from PIL import Image, ImageTk as itk
import mysql.connector as db


def add():
    pass


def add_book():

    root = Tk()
    root.title("Library Management System - Add Book")
    root.geometry("720x480")

    # Database Connection
    cnx = db.connect(host="localhost", user="root", password="", database="Library")
    cur = cnx.cursor()

    # Defining Header
    header = Frame(root, bg="#FCFFFD")
    header.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    # Page Heading
    headingLabel = Label(header, text="Add Books", bg='#FCFFFD', fg='#5D737E', font=('Calibri', 16))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Form Section
    form = Frame(root, bg='#DAFFEF')
    form.place(relx=0, rely=0.2, relwidth=1, relheight=1)

    # Book Name Input Field
    titleLabel = Label(form, text="Title", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    titleLabel.place(relx=0.1, rely=0.05, relheight=0.05)

    title = Entry(form)
    title.place(relx=0.1, rely=0.11, relwidth=0.8, relheight=0.05)

    # Book Author Input Field
    authorLabel = Label(form, text="Author", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    authorLabel.place(relx=0.1, rely=0.20, relheight=0.05)

    author = Entry(form)
    author.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.05)

    # Book Author Input Field
    quantityLabel = Label(form, text="Quantity", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    quantityLabel.place(relx=0.1, rely=0.35, relheight=0.05)

    quantity = Entry(form)
    quantity.place(relx=0.1, rely=0.41, relwidth=0.8, relheight=0.05)

    # Book Rating Input Field
    ratingLabel = Label(form, text="Rating", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    ratingLabel.place(relx=0.1, rely=0.50, relheight=0.05)

    rating = Entry(form)
    rating.place(relx=0.1, rely=0.56, relwidth=0.8, relheight=0.05)

    submit = Button(
        form,
        text='Submit',
        bg="#64B6AC",
        fg="#FCFFFD",
        font=('Calibri', 15),
        relief=FLAT,
    )
    submit.place(relx=0.44, rely=0.65, relwidth=0.12, relheight=0.075)

    root.mainloop()
