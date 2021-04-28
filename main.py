from tkinter import *
from PIL import Image, ImageTk as itk
# import mysql.connector as db
from add_book import add_book
from issue_book import issue_book
from search_book import search_book
from return_book import return_book


# # Database Connection
# cnx = db.connect(host="localhost", user="root", password="", database="Library")
# cur = cnx.cursor()


# Defining Root Widget
root = Tk()
root.title("Library Management System")
root.geometry("720x480")


# Loading Images
addBookIcon = Image.open("assets/add.png").resize((50, 50), Image.ANTIALIAS)
addBookImage = itk.PhotoImage(addBookIcon)
issueBookIcon = Image.open("assets/issue.png").resize((50, 50), Image.ANTIALIAS)
issueBookImage = itk.PhotoImage(issueBookIcon)
returnBookIcon = Image.open("assets/return.png").resize((50, 50), Image.ANTIALIAS)
returnBookImage = itk.PhotoImage(returnBookIcon)
searchBookIcon = Image.open("assets/search.jpg").resize((50, 50), Image.ANTIALIAS)
searchBookImage = itk.PhotoImage(searchBookIcon)


# Defining Header
header = Frame(root, bg="#FCFFFD")
header.place(relx=0, rely=0, relwidth=1, relheight=0.2)


# Defining Content
content = Frame(root)
content.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)


# Welcome Text
welcome = Label(header,  text="Welcome to the Library", fg="#5D737E", bg="#FCFFFD", font=("Calibri", 16))
welcome.place(relx=0, rely=0, relwidth=0.5, relheight=1)


# Institute Title
institute = Label(header,  text="K. J. Somaiya \n College Of Engineering", fg="#5D737E", bg="#FCFFFD", font=("Calibri", 16))
institute.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


# Navigation Buttons
addBookButton = Button(
    content,
    text='\nAdd Book',
    image=addBookImage,
    compound=TOP,
    bg="#64B6AC",
    fg="#FCFFFD",
    font=('Calibri', 16),
    relief=FLAT,
    command=add_book
)
addBookButton.place(relx=0.1, rely=0.1, relwidth=0.18, relheight=0.4)

issueBookButton = Button(
    content,
    text='\nIssue Book',
    image=issueBookImage,
    compound=TOP,
    bg="#64B6AC",
    fg="#FCFFFD",
    font=('Calibri', 16),
    relief=FLAT,
    command=issue_book
)
issueBookButton.place(relx=0.3, rely=0.1, relwidth=0.18, relheight=0.4)

returnBookButton = Button(
    content,
    text='\nReturn Book',
    image=returnBookImage,
    compound=TOP,
    bg="#64B6AC",
    fg="#FCFFFD",
    font=('Calibri', 16),
    relief=FLAT,
    command=return_book
)
returnBookButton.place(relx=0.5, rely=0.1, relwidth=0.18, relheight=0.4)

searchBookButton = Button(
    content,
    text='\nSearch Book',
    image=searchBookImage,
    compound=TOP,
    bg="#64B6AC",
    fg="#FCFFFD",
    font=('Calibri', 16),
    relief=FLAT,
    command=search_book
)
searchBookButton.place(relx=0.7, rely=0.1, relwidth=0.18, relheight=0.4)

root.mainloop()
