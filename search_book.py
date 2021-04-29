from tkinter import *
import mysql.connector as db


def search(title, base_root):
    """ This function is used to search a given Book Title """

    # Database Connection
    cnx = db.connect(user='root', password='', host='127.0.0.1', database='Library')
    cur = cnx.cursor()

    query = "SELECT * FROM Books WHERE title LIKE '%" + title + "%'"

    # We look for all books whose title contains the given substring
    try:
        cur.execute(query)
        result = cur.fetchall()
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()

    cnx.close()

    # We display all such books we found from the database
    root = Tk()
    root.title("Library Management System - Search Book")
    root.geometry("720x480")

    if result:
        head_id = Label(
            root,
            text="ID",
            bg='#FCFFFD',
            fg='#5D737E',
            font=('Calibri', 14)
        )
        head_id.place(relx=0.05, rely=0.1, relwidth=0.05, relheight=0.08)

        head_title = Label(
            root,
            text="Title",
            bg='#FCFFFD',
            fg='#5D737E',
            font=('Calibri', 14)
        )
        head_title.place(relx=0.10, rely=0.1, relwidth=0.35, relheight=0.08)

        head_author = Label(
            root,
            text="Author",
            bg='#FCFFFD',
            fg='#5D737E',
            font=('Calibri', 14)
        )
        head_author.place(relx=0.45, rely=0.1, relwidth=0.30, relheight=0.08)

        head_quantity = Label(
            root,
            text="Quantity",
            bg='#FCFFFD',
            fg='#5D737E',
            font=('Calibri', 14)
        )
        head_quantity.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.08)

        head_rating = Label(
                root,
                text="Rating",
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
        )
        head_rating.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.08)

        for i in range(len(result)):
            book_id = Label(
                root,
                text=str(result[i][0]),
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
            )
            book_id.place(relx=0.05, rely=0.2 + 0.125*i, relwidth=0.05, relheight=0.1)

            book_title = Label(
                root,
                text=str(result[i][1]),
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
            )
            book_title.place(relx=0.10, rely=0.2 + 0.125*i, relwidth=0.35, relheight=0.1)

            book_author = Label(
                root,
                text=str(result[i][2]),
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
            )
            book_author.place(relx=0.45, rely=0.2 + 0.125*i, relwidth=0.30, relheight=0.1)

            book_quantity = Label(
                root,
                text=str(result[i][3]),
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
            )
            book_quantity.place(relx=0.75, rely=0.2 + 0.125*i, relwidth=0.1, relheight=0.1)

            book_rating = Label(
                root,
                text=str(result[i][4]) + " / 5",
                bg='#FCFFFD',
                fg='#5D737E',
                font=('Calibri', 14)
            )
            book_rating.place(relx=0.85, rely=0.2 + 0.125*i, relwidth=0.1, relheight=0.1)
    else:
        message = Label(root, text="No Books Found")
        message.pack()

    if base_root:
        base_root.destroy()


def search_book():

    # Defining root element
    root = Tk()
    root.title("Library Management System - Search Book")
    root.geometry("720x480")

    # Defining header
    header = Frame(root, bg="#FCFFFD")
    header.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    # Defining Page Heading
    headingLabel = Label(header, text="Search Books", bg='#FCFFFD', fg='#5D737E', font=('Calibri', 16))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Defining the form section
    form = Frame(root, bg='#DAFFEF')
    form.place(relx=0, rely=0.2, relwidth=1, relheight=1)

    # Defining the Title Input Field
    titleLabel = Label(form, text="Title", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    titleLabel.place(relx=0.2, rely=0.1, relheight=0.06)

    titleField = Entry(form)
    titleField.place(relx=0.2, rely=0.17, relwidth=0.6, relheight=0.05)

    # Submit Button
    submit = Button(
        form,
        text='Submit',
        bg="#64B6AC",
        fg="#FCFFFD",
        font=('Calibri', 15),
        relief=FLAT,
        command=lambda: search(titleField.get(), root)
    )
    submit.place(relx=0.44, rely=0.65, relwidth=0.12, relheight=0.075)

    root.mainloop()
