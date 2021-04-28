from tkinter import *
import mysql.connector as db


def increment(title, author, quantity, root):
    """ This function is used to increment the quantity of a book which already exists """

    cnx = db.connect(user='root', password='', host='127.0.0.1', database='Library')
    cur = cnx.cursor()

    query = "UPDATE Books SET quantity=quantity+" \
            + quantity \
            + " WHERE title='" \
            + title \
            + "' AND author='" \
            + author \
            + "'"

    try:
        cur.execute(query)
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()

    cnx.close()
    root.destroy()


def add(title, author, quantity, rating, root):
    """ This function is used to add a new book """

    cnx = db.connect(host="localhost", user="root", password="", database="Library")
    cur = cnx.cursor()

    sql = "INSERT INTO Books(title, author, quantity, rating) VALUES (%s, %s, %s, %s)"
    val = (title, author, quantity, rating)
    try:
        # Executing Insert query
        cur.execute(sql, val)
        cnx.commit()
        print(cur.rowcount, "records inserted!")
    except Exception as e:
        print(e)
        cnx.rollback()

    cnx.close()
    if root:
        root.destroy()


def check(title, author, quantity, rating, base_root=None):
    """ This function is used to check if the book already exists in the database """

    # Database Connection
    cnx = db.connect(host="localhost", user="root", password="", database="Library")
    cur = cnx.cursor()

    result = list()
    query = "SELECT * FROM Books WHERE title='" + title + "' AND author='" + author + "'"

    try:
        cur.execute(query)
        result = cur.fetchall()
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()

    cnx.close()

    # If record exists, we give an option to increment the quantity
    if result and len(result) > 0:
        print("Yes it exists")
        root = Tk()
        root.title("Library Management System - Confirmation")
        root.geometry("720x480")
        question = Label(
            root,
            text="The Book already exists.\nDo you want add in to the same existing deck?",
            fg="#5D737E",
            font=('Calibri', 16)
        )
        question.place(relx=0.2, rely=0.3, relheight=0.3, relwidth=0.6)

        yes = Button(
            root,
            text='Yes',
            bg="#64B6AC",
            fg="#FCFFFD",
            font=('Calibri', 15),
            relief=FLAT,
            command=lambda: increment(title, author, quantity, root)
        )
        no = Button(
            root,
            text='No',
            bg="#64B6AC",
            fg="#FCFFFD",
            font=('Calibri', 15),
            relief=FLAT,
            command=lambda: root.destroy()
        )
        yes.place(relx=0.375, rely=0.6, relheight=0.1, relwidth=0.1)
        no.place(relx=0.525, rely=0.6, relheight=0.1, relwidth=0.1)
    else:
        add(title, author, quantity, rating, base_root)

    base_root.destroy()


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

    # Submit Button
    submit = Button(
        form,
        text='Submit',
        bg="#64B6AC",
        fg="#FCFFFD",
        font=('Calibri', 15),
        relief=FLAT,
        command=lambda: check(title.get(), author.get(), quantity.get(), rating.get(), root)
    )
    submit.place(relx=0.44, rely=0.65, relwidth=0.12, relheight=0.075)

    root.mainloop()
