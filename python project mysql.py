from tkinter import *
import mysql.connector as mysql

root = Tk()
root.geometry('1200x1200')
root.title("Student Registration Form")


Firstname=StringVar()
Middlename=StringVar()
Lastname=StringVar()
Email=StringVar()
Mobileno=StringVar()
var = StringVar()
c=StringVar()
var1= StringVar()
c1=StringVar()
Address=StringVar()
c2=StringVar()
c2=StringVar()
c3=StringVar()
c4=StringVar()
gender=StringVar()
a='B.COM'
p='BSC'
d='Bsc cs'
f='Bsc it'
g='Bms'

def database():
   firstname=Firstname.get()
   middlename=Middlename.get()
   lastname=Lastname.get()
   email=Email.get()
   mobileno=Mobileno.get()
   gender=var.get()
   country=c.get()
   cou=var1.get()
   city=c1.get()
   address=Address.get()
   Date=str(c2.get())
   month=str(c3.get())
   Year=str(c4.get())
   DOB=Year+"/"+month+"/"+Date
   conn=mysql.connect(user='root',password='scott',host='127.0.0.1')
   d=conn.cursor()
   d.execute('create database pankaj')
   d.execute('use pankaj')
   d.execute('create table student(firstname varchar(30),middlename varchar(30),lastname varchar(30),Email_Id varchar(30),Mobile_no varchar(30),Gender varchar(30),Address varchar(30),DOB varchar(30),City varchar(30),Country varchar(30),Courses varchar(30))')
   conn.commit()
   ok=('INSERT INTO student(firstname,middlename,lastname,Email_Id,Mobile_no,Gender,Address,DOB,City,Country,Courses) VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(firstname,middlename,lastname,email,mobileno,gender,address,DOB,city,country,cou))
   d.execute(ok)
   conn.commit()
   
label_0 = Label(root, text="STUDENT REGISTRATION FORM",width=35,font=("bold", 30))
label_0.place(x=100,y=47)


label_1 = Label(root, text="First Name",width=20,font=("bold", 18))
label_1.place(x=58,y=140)

entry_1 = Entry(root,textvar=Firstname,bd=5)
entry_1.place(x=300,y=145)
Firstname.set('Enter your first name')

label_1A = Label(root, text="Middle Name",width=20,font=("bold", 18))
label_1A.place(x=70,y=178)

entry_1A = Entry(root,textvar=Middlename,bd=5)
entry_1A.place(x=300,y=186)
Middlename.set('Enter your middle name')

label_1B = Label(root, text="Last Name",width=20,font=("bold", 18))
label_1B.place(x=58,y=215)

entry_1B = Entry(root,textvar=Lastname,bd=5)
entry_1B.place(x=300,y=225)
Lastname.set('Enter your last name')

label_2 = Label(root, text="Email",width=20,font=("bold", 18))
label_2.place(x=28,y=260)

entry_2 = Entry(root,textvar=Email,bd=5)
entry_2.place(x=300,y=265)
Email.set('abc@gmail.com')

label_3 = Label(root, text="Gender",width=20,font=("bold", 18))
label_3.place(x=38,y=295)

Radiobutton(root, text="Male",padx = 5, variable=var, value='male').place(x=290,y=300)
Radiobutton(root, text="Female",padx = 20, variable=var, value='female').place(x=350,y=300)

label_4 = Label(root, text="Address",width=20,font=("bold", 18))
label_4.place(x=48,y=330)

entry_4A = Entry(root,textvar=Address,bd=10)
entry_4A.place(x=300,y=330)
Address.set('Enter your address')

label_5 = Label(root, text="City",width=20,font=("bold", 18))
label_5.place(x=30,y=360)

list1 = ['Mumbai','Delhi','Kolkata','Bengaluru','Hyderabad','Chennai','Ahmedabad','Pune','Surat','Visakhapatnam'];

droplist=OptionMenu(root,c1, *list1)
droplist.config(width=15)
c1.set('select your City') 
droplist.place(x=300,y=370)


label_6 = Label(root, text="Country:",width=20,font=("bold", 18))
label_6.place(x=470,y=335)

list2 = ['Canada','India','UK','Australia','Iceland','South Africa','UAE','Srilanka','Russia','New York','France'];

droplist=OptionMenu(root,c, *list2)
droplist.config(width=15)
c.set('select your Country') 
droplist.place(x=850,y=340)

label_1A = Label(root, text="Mobile no.",width=20,font=("bold", 18))
label_1A.place(x=475,y=186)

entry_1A = Entry(root,textvar=Mobileno,bd=5)
entry_1A.place(x=840,y=186)
Mobileno.set('Enter your 10-digit no.')

label_5 = Label(root, text="D.O.B",width=20,font=("bold", 18))
label_5.place(x=460,y=250)

list3 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];

droplist=OptionMenu(root,c2, *list3)
droplist.config(width=5)
c2.set('DATE') 
droplist.place(x=840,y=240)

list4= ['1','2','3','4','5','6','7','8','9','10','11','12'];

droplist=OptionMenu(root,c3, *list4)
droplist.config(width=5)
c3.set('month') 
droplist.place(x=900,y=240)

list5 = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003'];

droplist=OptionMenu(root,c4, *list5)
droplist.config(width=5)
c4.set('year') 
droplist.place(x=960,y=240)



label_4 = Label(root, text="Choose your Coureses:",width=20,font=("bold", 19))
label_4.place(x=540,y=140)


Radiobutton(root, text="B.com", variable=var1 , value=a).place(x=830,y=140)

Radiobutton(root, text="Bsc", variable=var1 ,value=p).place(x=900,y=140)

Radiobutton(root, text="Bsc cs", variable=var1 ,value=d).place(x=970,y=140)

Radiobutton(root, text="Bsc it", variable=var1 ,value=f).place(x=830,y=160)

Radiobutton(root, text="Bms", variable=var1 ,value=g).place(x=900,y=160)


Button(root, text='Submit',width=20,bg='red',fg='green',command=database).place(x=400,y=500)
Button(root, text='Reset',width=20,bg='yellow',fg='black',command=database).place(x=650,y=500)

      
root.mainloop()
