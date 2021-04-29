from tkinter import *
import mysql.connector as db


def issue(book_id, base_root):
    """ This function is used to Issue a Book """

    cnx = db.connect(user='root', password='', host='127.0.0.1', database='Library')
    cur = cnx.cursor()

    query = "UPDATE Books SET quantity=quantity-1 WHERE id=" + book_id + " AND quantity>=1"

    # Defining the root element wherein we will display the relevant message
    root = Tk()
    root.title("Library Management System - Issue Book")
    root.geometry("720x480")

    message = "Book Unavailable/Out Of Stock"

    # We try to issue the book whose id is given
    try:
        cur.execute(query)
        cnx.commit()
        message = "Book Issued"
    except Exception as e:
        print(e)
        cnx.rollback()

    # We Display the relevant message
    messageLabel = Label(
        root,
        text=message,
        fg="#5D737E",
        font=('Calibri', 16)
    )
    messageLabel.place(relx=0.2, rely=0.3, relheight=0.3, relwidth=0.6)

    base_root.destroy()
    cnx.close()


def issue_book():

    # Defining root element
    root = Tk()
    root.title("Library Management System - Issue Book")
    root.geometry("720x480")

    # Defining header
    header = Frame(root, bg="#FCFFFD")
    header.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    # Defining Page Heading
    headingLabel = Label(header, text="Issue Books", bg='#FCFFFD', fg='#5D737E', font=('Calibri', 16))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Defining the form section
    form = Frame(root, bg='#DAFFEF')
    form.place(relx=0, rely=0.2, relwidth=1, relheight=1)

    # Defining the ID Input Field
    idLabel = Label(form, text="Book ID", bg="#DAFFEF", fg="#5D737E", font=('Calibri', 14))
    idLabel.place(relx=0.2, rely=0.1, relheight=0.06)

    idField = Entry(form)
    idField.place(relx=0.2, rely=0.17, relwidth=0.6, relheight=0.05)

    # Submit Button
    submit = Button(
        form,
        text='Submit',
        bg="#64B6AC",
        fg="#FCFFFD",
        font=('Calibri', 15),
        relief=FLAT,
        command=lambda: issue(idField.get(), root)
    )
    submit.place(relx=0.44, rely=0.65, relwidth=0.12, relheight=0.075)

    root.mainloop()
