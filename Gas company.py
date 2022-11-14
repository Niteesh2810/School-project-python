#registration
import mysql.connector
import random
from win10toast import ToastNotifier
from tkinter import *
import tkinter
import datetime
from fpdf import FPDF
import time
import PIL.Image
from PIL import ImageTk
import re

print("--------------------------------------------------------------------------------")
print("NAS GAS COMPANY")
print("-------------------------------------------------------------------------------")

def log_reg():
    global top
    top = tkinter.Tk(className=' NAS GAS COMPANY')
    top.geometry("300x300")
    im=PIL.Image.open(r"C:\Users\nitee\Downloads\1.jpg")
    out = im.resize((300,300))
    render=ImageTk.PhotoImage(out)
    img= Label(top,image=render)
    img.place(x=0,y=0)
    T = Text(top, height = 5, width = 52) 
    l = Label(top, text = " NAS GAS COMPANY") 
    l.config(font =("Courier", 14))
    B_login = tkinter.Button(top, text ="LOGIN",font='Times',bg='#000000',fg='white',activebackground='cyan',command=login_fun)
    B_register = tkinter.Button(top, text ="REGISTER",font='Times',bg='#000000',fg='white',activebackground='cyan',command=register_fun)
    B_login.pack()
    B_register.pack()
    l.pack()
    img.pack()
    B_login.place(anchor=CENTER,x=150,y=115, height=40, width=75)
    B_register.place(anchor=CENTER,x=150,y=175,height=40, width=75)
    top.mainloop()   
    
def register_fun():
    top.destroy()
    top.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    #mycursor.execute("create table Customer_details(NAME char(20) NOT NULL,PHONE varchar(20) NOT NULL,EMAIL char(40) NOT NULL,ADDRESS char(200) NOT NULL,BANK varchar(20) NOT NULL,AADHAR varchar(20) primary key NOT NULL,USERNAME char(50) NOT NULL,PASSWORD CHAR(40) NOT NULL,COUNT varchar(20),DOB DATE NULL);")
    #for i in mycursor:
    #    print(i)
    name=input("Name:")
    while True:
        try:
            phone=int(input("Mobile Number:"))
            if len(str(phone))==10:
                break
            else:
                 print("The phone number should be 10 characters long.Re-enter the phone number.")
        except ValueError:print("Please enter a valid mobile number.")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    def check():
        global email
        while True:         
             email=input("Email ID:")
             if(re.search(regex,email)):  
                 break
             else:  
                 print("Invalid Email.")  
    if __name__ == '__main__' :  
        check()
    address=input("Address:")
    while True:
        try:
            bank=int(input("Account Number:"))
        except ValueError:print("Please enter a valid account number.")
        else:break
    global aadhar
    while True:
        try:
            aadhar=int(input("Aadhar Number:"))
            if len(str(aadhar))==15:
                break
            else:
                print("Invalid Aadhar number.The Aadhar number should be 15 characters long.")
        except ValueError:print("Please enter a valid Aadhar number.")
    mycursor.execute("select AADHAR from Customer_Details;")
    aad=mycursor.fetchall()
    mycursor.execute("select USERNAME from Customer_Details;")
    u=mycursor.fetchall()
    for i in range(len(aad[0])):
        if aad[0][i]==str(aadhar):
            print("You already have an account.Try logging in!")
            break
        else:
            while True:
                username=input("Username:")
                for i in range(len(u[0])):
                    if u[0][i]==username:
                        print("This username has already been taken.Try Typing another one.")
                        while u[0][i]==username:
                            username=input("Username:")
                    else:
                        break
                if username.isalnum()==False:
                    print("Invalid Username.")
                else:
                    break
            while True:
                password=input("Password:")
                if len(password)<8 :
                    print("Invalid Password.The password should be at least 8 characters long.")
                elif password.isalpha()==True:
                    print("Please include Digits and Special Characters.")
                elif password.isdigit()==True:
                    print("Please include Characters and Special Characters.")
                elif password.isalnum()==True:
                    print("Please include Special Characters.")
                else:
                    break
            while True:
                c_password=input("Confirm Password:")
                if c_password!=password:
                    print("Password Mismatched...")
                else:
                    break
            while True:
                a=random.randint(1000,9999)
                n=ToastNotifier()
                n.show_toast("Your OTP is:",str(a),duration=5)
                otp=int(input("Enter OTP:"))
                if otp==a:
                    print("Your account has been registered Successfully.")
                    b="INSERT INTO Customer_details(NAME,PHONE,EMAIL,ADDRESS,BANK,AADHAR,USERNAME,PASSWORD,COUNT) VALUES" 
                    val=(name,phone,email,address,bank,aadhar,username,password,0)
                    f=b+str(val)
                    mycursor.execute(f)
                    mydb.commit()
                    break
                else:
                    print("Wrong OTP.Enter the OTP that you will be receiving now .")
def login_fun():
    top.destroy()
    top.quit()    
    global name_entry
    global passw_var
    global root
    global name_var
    root=tkinter.Tk(className=' NAS GAS COMPANY') 
    root.geometry("600x400")
    name_var=tkinter.StringVar() 
    passw_var=tkinter.StringVar()
    im=PIL.Image.open(r"C:\Users\nitee\Downloads\1.jpg")
    out=im.resize((600,400))
    render=ImageTk.PhotoImage(out)
    img= Label(root,image=render)
    img.place(x=0,y=0)
    name_label = tkinter.Label(root, text = 'Username',font=('Times',15,'bold')) 
    name_entry = tkinter.Entry(root,textvariable = name_var,font=('calibre',10,'normal'))  
    passw_label = tkinter.Label(root,text = 'Password',font = ('Times',15,'bold')) 
    passw_entry=tkinter.Entry(root,textvariable = passw_var,font = ('calibre',10,'normal'), show = '*')   
    B_for_pass = tkinter.Button(root, text ="FORGOT PASSWORD",font='Times',bg='black',fg='white',activebackground='cyan',command=forgot_password)
    img.pack()
    B_for_pass.pack()
    B_ok=tkinter.Button(root,text = 'OK',font='Times',bg='black',fg='white',activebackground='cyan', command = check_login)
    name_label.place(anchor= NW )
    passw_label.place(anchor= W,y=50 )
    name_entry.place(x=150)
    passw_entry.place(anchor=W,x=150,y=50)
    B_for_pass.place(anchor=CENTER,x=150,y=115, height=30, width=155)
    B_ok.place(anchor=CENTER,x=150,y=155, height=30, width=55)
    root.mainloop()
    
def forgot_password():
    root.destroy()
    root.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    mycursor.execute("select USERNAME from Customer_details;")
    u=mycursor.fetchall()
    while True:
        a=random.randint(1000,9999)
        n=ToastNotifier()
        n.show_toast("Your OTP is:",str(a),duration=5)
        otp=int(input("Enter OTP:"))
        if otp==a:
            break
        else:
            print("Wrong OTP.Enter the OTP that you will be receiving now.")
    
    while True:
        username=input("Username:")
        if username not in u[0]:
            print("You do not have an account.Please register in order to continue.")
            sys.exit(0)
        else:
            break
    while True:
        n_password=input("New Password:")
        if len(n_password)<8 :
            print("Invalid Password.The password should be at least 8 characters long.")
        elif n_password.isalpha()==True:
            print("Please include Digits and Special Characters.")
        elif n_password.isdigit()==True:
            print("Please include Characters and Special Characters.")
        elif n_password.isalnum()==True:
            print("Please include Special Characters.")
        else:
            break
    while True:
        c_n_password=input("Confirm New Password:")
        if c_n_password!=n_password:
            print("Password Mismatched...")
        else:
            b="update Customer_details set PASSWORD="
            f=b+"'"+n_password+"'"+" where USERNAME="+"'"+username+"'"+';'
            mycursor.execute(f)
            mydb.commit()
            print("Your password has been changed successfully")
            break    

def details():
    master.destroy()
    master.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    s="select * from Customer_details where USERNAME="+"'"+login_name+"'"+";"
    mycursor.execute(s)
    det=mycursor.fetchall()
    mydb.commit()
    print("NAME:",det[0][0])
    print("PHONE:",det[0][1])
    print("EMAIL:",det[0][2])
    print("ADDRESS:",det[0][3])
    f,g='',''
    for i in range(len(str(det[0][4]))):
        if i>=len(str(det[0][4]))-4:
            f+=str(det[0][4][i])
        else:
            f+='x'
    for i in range(len(str(det[0][5]))):
        if i>=len(str(det[0][5]))-4:
            g+=str(det[0][5][i])
        else:
            g+='x'
    print("BANK:",f)
    print("AADHAR:",g)
    print("QUOTA:",det[0][8])

def change_address():
    master.destroy()
    master.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    new_address=input("Enter new address:")
    b="update Customer_details set ADDRESS="
    f=b+"'"+new_address+"'"+" where USERNAME="+"'"+login_name+"'"+';'
    mycursor.execute(f)
    mydb.commit()
    print("Your Address has been changed successfully.")

def sec_delete():
    king.destroy()
    king.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    while True:
        a=random.randint(1000,9999)
        n=ToastNotifier()
        n.show_toast("Your OTP is:",str(a),duration=5)
        otp=int(input("Enter OTP:"))
        if otp==a:
            b="delete from Customer_details where USERNAME=" +"'"+login_name+"'"
            mycursor.execute(b)
            mydb.commit()
            print("You have unsubscribed successfully.")
            break
        else:
            print("Wrong OTP.Enter the OTP that you will be receiving now.")
def primary_delete():
    master.destroy()
    master.quit()
    global king 
    king=tkinter.Tk(className=' NAS GAS COMPANY')
    king.geometry('300x300')
    head=tkinter.Label(king,text='Do you want to delete your account?',font=('Times',15,'bold'))
    B_yes=tkinter.Button(king,text='YES',font='Times',bg='black',fg='white',activebackground='cyan',command=sec_delete)
    B_no=tkinter.Button(king,text='NO',font='Times',bg='black',fg='white',activebackground='cyan',command=after_login)        
    head.pack()
    B_yes.pack()
    B_no.pack()
    head.place(anchor=NW)
    B_yes.place(x=100,y=100)
    B_no.place(x=200,y=100)
    
def service():
    master.destroy()
    master.quit()
    a,b,c=9789361552,7908821202,6055721003
    print("A service engineer will arrive shortly at your location.")
    print("Contact:",a,"\\",b,"\\",c)

from tkinter import *
from tkinter.ttk import *
def bill():
    boss.destroy()
    boss.quit()
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    s="select * from Customer_details where USERNAME="+"'"+login_name+"'"
    mycursor.execute(s)
    det=mycursor.fetchall()
    r=datetime.date.today()
    q=str(r)
    n="NAME:  "+det[0][0]
    a="ADDRESS:  "+det[0][3]
    p="PHONE NUMBER:  "+det[0][1]
    e="EMAIL ID:  "+det[0][2]
    d="BOOKING DATE(YYYY-MM-DD):  "+q
    cus="CUSTOMER CARE NO: 9789361552 / 7908821202 / 6055721003"
    if int(det[0][8])<12:
        c="QUOTA:  "+str(14.2*(int(det[0][8])))+"Kg of Quota 170.4 Kg"
        t="TOTAL AMOUNT:  "+"650"
        pdf = FPDF() 
        pdf.add_page()
        pdf.set_font("Times", size = 25)  
        pdf.cell(190, 20, txt = "NAS GAS COMPANY",ln = 1, align = 'C')
        pdf.set_font("Times", size = 25)  
        pdf.cell(190, 20, txt = "E-BILL",ln = 2, align = 'C') 
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = n,ln = 5, align = 'L')
        pdf.cell(200, 10, txt = a,ln = 8, align = 'L')
        pdf.cell(200, 10, txt = c, ln = 14, align = 'L')
        pdf.cell(200, 10, txt = p, ln = 21, align = 'L')
        pdf.cell(200, 10, txt = e, ln = 28, align = 'L')
        pdf.cell(200, 10, txt = d, ln = 36, align = 'L')
        pdf.cell(200, 10, txt = t, ln = 44, align = 'L')
        pdf.set_font("Arial", size = 20)  
        pdf.cell(190, 20, txt = "Thank You!!",ln =50 , align = 'C')
        pdf.set_font("Times", size = 10)
        pdf.cell(200, 20, txt = cus, ln = 52, align = 'R')
        h="BILL_"+str(det[0][9])+".pdf"
        pdf.output(h)
    else:
        c="QUOTA:  "+str(14.2*(int(det[0][8])))+"Kg of Quota 170.4 Kg"
        t="TOTAL AMOUNT:  "+"700"
        pdf = FPDF() 
        pdf.add_page()  
        pdf.set_font("Times", size = 25)  
        pdf.cell(175, 20, txt = "E-BILL",ln = 1, align = 'C') 
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = n,ln = 5, align = 'L')
        pdf.cell(200, 10, txt = a,ln = 8, align = 'L')
        pdf.cell(200, 10, txt = c, ln = 14, align = 'L')
        pdf.cell(200, 10, txt = p, ln = 21, align = 'L')
        pdf.cell(200, 10, txt = e, ln = 28, align = 'L')
        pdf.cell(200, 10, txt = d, ln = 36, align = 'L')
        pdf.cell(200, 10, txt = t, ln = 44, align = 'L')
        pdf.set_font("Arial", size = 20)  
        pdf.cell(190, 20, txt = "Thank You!!",ln =50 , align = 'C')
        pdf.set_font("Times", size = 10)
        pdf.cell(200, 20, txt = cus, ln = 52, align = 'R')
        h="BILL_"+str(det[0][9])+".pdf"
        pdf.output(h)


def loading():
    global boss
    global load
    boss=Tk(className=' NAS GAS COMPANY')
    boss.geometry('500x75')
    load=Progressbar(boss,orient=HORIZONTAL,length=400,mode='determinate')
    bar()
def bar():
    load.pack()
    load['value']=40
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=80
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=120
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=160
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=200
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=240
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=280
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=320
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=360
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    load['value']=400
    boss.update_idletasks()
    time.sleep(2)
    load.pack()
    bill()
    

def sec_book():
    master.destroy()
    master.quit()
    t=datetime.date.today()
    s=str(t)
    li=list(s)
    y=int(li[0]+li[1]+li[2]+li[3])
    m=int(li[5]+li[6])
    d=int(li[8]+li[9])
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    r="select DOB from Customer_details where USERNAME="+"'"+login_name+"'"+";"
    mycursor.execute(r)
    v=mycursor.fetchall()
    while True:
        a=random.randint(1000,9999)
        n=ToastNotifier()
        n.show_toast("Your OTP is:",str(a),duration=5)
        otp=int(input("Enter the OTP to confirm your booking:"))
        if otp==a:
            if v==[(None,)]:
                b="update Customer_details set DOB="+"'"+str(t)+"'"+' where USERNAME='+"'"+login_name+"'"+";"
                mycursor.execute(b)
                c="update Customer_details set COUNT=COUNT+1 where USERNAME="+"'"+login_name+"'"+";"
                mycursor.execute(c)
                mydb.commit()
                loading()
                print("Your cylinder has been booked successfully[A copy of the bill has been saved where the python has been originally saved in the form of a PDF].")
                break
            else:
                w=v[0][0]
                h=list(str(w))
                h_y=int(h[0]+h[1]+h[2]+h[3])
                h_m=int(h[5]+h[6])
                h_d=int(h[8]+h[9])
                if y-h_y==0 and m-h_m==0 and d-h_d<15:
                    print("You cannot book a cylinder now.")
                    break
                else:
                    b="update Customer_details set DOB="+"'"+str(t)+"'"+' where USERNAME='+"'"+login_name+"'"+";"
                    mycursor.execute(b)
                    c="update Customer_details set COUNT=COUNT+1 where USERNAME="+"'"+login_name+"'"+";"
                    mycursor.execute(c)
                    mydb.commit()
                    loading()
                    print("Your cylinder has been successfully booked[A copy of the bill has been saved where the python has been originally saved in the form of a PDF].")
                    break
        else:
            print("Wrong OTP.Enter the OTP that you will be receiving now.")    

def rate_sec():
    minister.destroy()
    minister.quit()
    global tree
    tree=tkinter.Tk(className=' NAS GAS COMPANY')
    tree.geometry("500x500")
    feed_var=tkinter.StringVar()
    feed_label = tkinter.Label(tree, text='PLEASE LEAVE A FEEDBACK...',font=('Times',15,'bold'))
    feed = tkinter.Entry(tree,textvariable = feed_var,font=('calibre',10,'normal'))
    B_ok=tkinter.Button(tree, text ="OK",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_ter)
    feed_label.place(anchor= NW )
    feed.place(x=50,y=100,height=200,width=400)
    B_ok.place(x=440,y=450,height=30, width=55)
    
def rate_ter():
    print("Thank you for your feedback")
    tree.destroy()
    tree.quit()
    
def rate():
    master.destroy()
    master.quit()
    global minister
    minister=tkinter.Tk(className=' NAS GAS COMPANY')
    minister.geometry("500x500")
    B_one = tkinter.Button(minister, text ="☆",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_sec)
    B_two = tkinter.Button(minister, text ="☆☆",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_sec)
    B_three = tkinter.Button(minister, text ="☆☆☆",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_sec)
    B_four = tkinter.Button(minister, text ="☆☆☆☆",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_sec)
    B_five = tkinter.Button(minister, text ="☆☆☆☆☆",font='Times',bg='black',fg='white',activebackground='cyan',command=rate_sec)
    B_one.pack()
    B_two.pack()
    B_three.pack()
    B_four.pack()
    B_five.pack()
    B_one.place(anchor=CENTER,x=250,y=55, height=40, width=200)
    B_two.place(anchor=CENTER,x=250,y=125,height=40, width=200)
    B_three.place(anchor=CENTER,x=250,y=195,height=40, width=200)
    B_four.place(anchor=CENTER,x=250,y=265,height=40, width=200)
    B_five.place(anchor=CENTER,x=250,y=335,height=40, width=200)
    minister.mainloop()
    
def after_login():
    global master
    master = tkinter.Tk(className=' NAS GAS COMPANY')
    master.geometry("500x500")
    im=PIL.Image.open(r"C:\Users\nitee\Downloads\1.jpg")
    out=im.resize((500,500))
    render=ImageTk.PhotoImage(out)
    img= Label(master,image=render)
    img.place(x=0,y=0)
    B_details = tkinter.Button(master, text ="ABOUT YOU",font='Times',bg='black',fg='white',activebackground='cyan',command=details)
    B_book = tkinter.Button(master, text ="BOOK YOUR CYLINDER",font='Times',bg='black',fg='white',activebackground='cyan',command=sec_book)
    B_c_address = tkinter.Button(master, text ="CHANGE ADDRESS",font='Times',bg='black',fg='white',activebackground='cyan',command=change_address)
    B_delete = tkinter.Button(master, text ="SURRENDER YOUR SUBSCRIPTION",font='Times',bg='black',fg='white',activebackground='cyan',command=primary_delete)
    B_service = tkinter.Button(master, text ="SERVICE",font='Times',bg='black',fg='white',activebackground='cyan',command=service)
    B_rate = tkinter.Button(master,text ="RATE OUR SERVICE",font='Times',bg='black',fg='white',activebackground='cyan',command=rate)
    B_details.pack()
    B_book.pack()
    B_c_address.pack()
    B_delete.pack()
    B_service.pack()
    B_rate.pack()
    img.pack()
    B_details.place(anchor=CENTER,x=250,y=55, height=40, width=270)
    B_book.place(anchor=CENTER,x=250,y=125,height=40, width=270)
    B_c_address.place(anchor=CENTER,x=250,y=195,height=40, width=270)
    B_delete.place(anchor=CENTER,x=250,y=265,height=40, width=270)
    B_service.place(anchor=CENTER,x=250,y=335,height=40, width=270)
    B_rate.place(anchor=CENTER,x=250,y=405,height=40, width=270)
    master.mainloop()

def check_login():
    mydb=mysql.connector.connect(host='localhost',user='Niteesh',passwd='28102003',port='3306',database='project')
    mycursor=mydb.cursor()
    global login_name
    global login_password
    login_name=name_entry.get()
    login_password=passw_var.get()
    mycursor.execute("select USERNAME,PASSWORD from Customer_details;")
    li_u_p=mycursor.fetchall()
    for i in range(len(li_u_p)):
        if login_name not in li_u_p[i]:
            continue    
        else:
            a=li_u_p[i].index(login_name)
            b=i
            if li_u_p[b][1]==login_password:
                print("You have been logged in successfully.")
                root.destroy()
                root.quit()
                after_login()
            else:
                print("Invalid username or Password.")
                name_var.set("") 
                passw_var.set("")
    
log_reg()

    




