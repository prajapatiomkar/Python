from tkinter import *
from tkinter import messagebox
import pymysql

window = Tk()
window.geometry("300x200")
window.title("Student_Form")
window.resizable(0,0)
main_frame=Frame(window).place()

stud_id=IntVar()
seat=IntVar()
roll=IntVar()
name_s=StringVar()

# Insert
def insert():
    ent1=stud_id.get()
    ent2=seat.get()
    ent3=roll.get()
    ent4=name_s.get()


    if (ent1=="" or ent2=="" or ent3=="" or ent4==""):
        # print("Fill all")
        messagebox.showinfo("Insert status","All Fields Are Required")
    else:
        connection=pymysql.connect(host="localhost",user="root",passwd=77187718,db="student")
        cursors=connection.cursor()
        cursors.execute("insert into student values(%d,%d,%d,%s)",(ent1,ent2,ent3,ent4))
        cursors.close()
        connection.commit()

lable1 = Label(main_frame,text="Student_Id",font=("Arial", 10,"bold"),border=2,relief="solid",bg="sky blue",width=9).place(x=10,y=10)

entry1=Entry(main_frame,bd=2,bg="sky blue",font=("Arial", 11),textvariable=stud_id).place(x=100,y=10)
print(entry1)

lable2 = Label(main_frame,text="Seat_No",font=("Arial", 10,"bold"),border=2,relief="solid",bg="sky blue",width=9).place(x=10,y=40)

entry2=Entry(main_frame,bd=2,bg="sky blue",font=("Arial", 11),textvariable=seat).place(x=100,y=40)


lable3 = Label(main_frame,text="Roll_No",font=("Arial", 10,"bold"),border=2,relief="solid",bg="sky blue",width=9).place(x=10,y=70)

entry3=Entry(main_frame,bd=2,bg="sky blue",font=("Arial", 11),textvariable=roll).place(x=100,y=70)


lable4 = Label(main_frame,text="Name",font=("Arial", 10,"bold"),border=2,relief="solid",bg="sky blue",width=9).place(x=10,y=100)
entry4=Entry(main_frame,bd=2,bg="sky blue",font=("Arial", 11),textvariable=name_s).place(x=100,y=100)

insert_button = Button(text="Insert",width=35,command=insert).place(x=10,y=130)
insert_button = Button(text="Clear",width=10).place(x=95,y=160)

window.mainloop()


