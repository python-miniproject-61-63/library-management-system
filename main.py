from tkinter import *
from PIL import Image, ImageTk as itk
import mysql.connector as db


# Database Connection
cnx = db.connect(host="localhost", user="root", password="", database="Library")
cur = cnx.cursor()


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
addBookButton = Button(content, text='          Add Book', image=addBookImage, compound=LEFT, bg="#64B6AC", fg="#FCFFFD", font=('Calibri', 16))
addBookButton.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.18)

issueBookButton = Button(content, text='          Issue Book', image=issueBookImage, compound=LEFT, bg="#64B6AC", fg="#FCFFFD", font=('Calibri', 16))
issueBookButton.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.18)

returnBookButton = Button(content, text='       Return Book', image=returnBookImage, compound=LEFT, bg="#64B6AC", fg="#FCFFFD", font=('Calibri', 16))
returnBookButton.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.18)

searchBookButton = Button(content, text='       Search Book', image=searchBookImage, compound=LEFT, bg="#64B6AC", fg="#FCFFFD", font=('Calibri', 16))
searchBookButton.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.18)

root.mainloop()
