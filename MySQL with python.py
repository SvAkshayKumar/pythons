from tkinter import *
import os
import random
import datetime
import mysql.connector
from PIL import Image, ImageTk
import turtle as tr


mycon = mysql.connector.connect(host='localhost', user='root', password='root', database='medicine')
mycur = mycon.cursor()
root = Tk()
root.title('Login')
root.geometry('925x500+200+100')
root.configure(bg="white")
root.resizable(False, False)

mycur.execute("""
    CREATE TABLE IF NOT EXISTS Stock (
        batch_no INT PRIMARY KEY,
        name VARCHAR(255),
        manuf VARCHAR(255),
        date_man DATE,
        date_exp DATE,
        quantity INT,
        sell INT,
        balance INT,
        cost_unit INT)
""")

mycur.execute("""CREATE TABLE IF NOT EXISTS Dispose (
    batch_no INT PRIMARY KEY,
    name VARCHAR(255),
    date_exp DATE,
    amount INT
)""")
image = Image.open(r"C:\Users\Akshay\OneDrive\Desktop\python\OIG.hrV6zlSSvVK19mle5.jpeg")#Image for the signin page
image = image.resize((350, 300))
img = ImageTk.PhotoImage(image)
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='SIGN IN', fg='black', bg='white', font=('Copperplate Gothic Bold', 30, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'username')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'password')


code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)



# Assuming you have a `signin` function for the "Sign In" button
def signin():
    username = user.get()
    password = code.get()

    if username == '12345' and password == '04':
        
        root.destroy()
        page2()
        
    else:
        screen = Toplevel(root)
        screen.title("Invalid")
        screen.geometry('463x250+430+230')
        screen.config(bg='white')
        Label(screen, text="Sorry, invalid username or password", bg='white', font=('Calisto MT', 14)).pack(expand=True)
        screen.after(750,screen.destroy)
        screen.mainloop()
Button(frame, width=40, pady=7, text='sign in', bg='green', fg='white', border=0, command=signin).place(x=35, y=204)
def welcome_page():
    tr.setup(width=1200, height=450)
    tr.speed(25)
    tr.pensize(12)
    tr.penup()#taking the pen to the left/initial point
    tr.left(180)
    tr.forward(300)
    tr.right(90)
    #Writing the letter W
    tr.forward(100)
    tr.right(180)
    tr.pendown()
    tr.forward(100)
    tr.left(135)
    tr.forward(55)
    tr.right(90)
    tr.forward(55)
    tr.left(135)
    tr.forward(100)
    #Rearranging the pen to the position
    tr.penup()
    tr.right(90)
    tr.forward(75)
    tr.left(90)
    tr.right(180)
    tr.pendown()
    #Writing the letter E
    tr.right(90)
    tr.forward(60)
    tr.left(90)
    tr.forward(50)
    tr.left(90)
    tr.forward(45)
    tr.left(180)
    tr.forward(45)
    tr.left(90)
    tr.forward(50)
    tr.left(90)
    tr.forward(60)
    #Rearranging the pen to the position
    tr.penup()
    tr.forward(15)
    tr.pendown()
    #Writing the letter L
    tr.forward(60)
    tr.left(180)
    tr.forward(60)
    tr.right(90)
    tr.forward(100)
    #Rearranging the pen to the position
    tr.right(90)
    tr.penup()
    tr.forward(120)
    tr.pendown()
    #Writing the letter C
    tr.circle(-55,-180)
    #Rearranging the pen to the position
    tr.penup()
    tr.right(180)
    tr.forward(65)
    tr.pendown()
    #Writing the letter O
    tr.circle(55,360)
    #Rearranging the pen to the position
    tr.penup()
    tr.forward(75)
    tr.left(90)
    tr.pendown()
    #Wrting the letter M
    tr.forward(100)
    tr.right(135)
    tr.forward(50)
    tr.left(90)
    tr.forward(50)
    tr.right(135)
    tr.forward(100)
    #Rearranging the pen to the position
    tr.penup()
    tr.right(180)
    tr.forward(100)
    tr.right(90)
    tr.forward(75)
    tr.left(90)
    tr.right(180)
    tr.pendown()
    #Writing the letter E
    tr.right(90)
    tr.forward(60)
    tr.left(90)
    tr.forward(50)
    tr.left(90)
    tr.forward(45)
    tr.left(180)
    tr.forward(45)
    tr.left(90)
    tr.forward(50)
    tr.left(90)
    tr.forward(60)
    tr.bye()
def page2():
    welcome_page()
    def background_store():#This function is used to take the input details of the imported medicine
        sql = "Insert into stock(batch_no,name,manuf,date_man,date_exp,quantity,sell,balance,cost_unit)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"#This is the SQL syntex
        print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
        acc = int(input('\nENTER THE BATCH NUMBER:'))
        nm = input('\nENTER THE NAME OF THE MEDICINE WITH POWER:')
        addr = input('\nENTER THE NAME OF THE MANUFACTURER:')
        dbs = input('\nENTER THE DATE OF MANUFACTURE(YYYY-MM-DD):')
        dacc = input('\nENTER THE DATE OF EXPIRY(YYYY-MM-DD):')
        quan = int(input('\nENTER THE QUANTITY OF THE IMPORTED MEDICINE:'))
        sell = 0
        balance = quan
        cost = int(input('\nENTER THE COST OF THE IMPORTED MEDICINE PER UNIT:'))
        value = (acc, nm, addr, dbs, dacc, quan, sell, balance, cost)
        try:
            mycur.execute(sql, value)
            print(nm, 'ADDED TO THE STOCK')
            mycon.commit()#Running the SQL command to add it to the table in mysql
        except:
            print('UNABLE TO ADD MEDICINE INCORRECT FORMAT OF DETAILS OR MEDICINE ALREADY EXIST!!!!!')

    def background_search_by_name():#This function helps the user to search the details of the medicine by entering its name 
        ph = input('\nENTER THE MEDICINE NAME TO SEARCH:')
        sql = "Select * from Stock where name=%s"#This is the SQL syntex
        value = (ph,)
        mycur.execute(sql, value)
        rec = mycur.fetchone()#This line gives the output from mysql and stores it in the variable rec
        if rec == None:
            print(ph, 'IS NOT AVAILABLE')
        else:
            print('BATCH NUMBER:\t', rec[0])
            print('MEDICINE NAME:\t', rec[1])
            print('MANUFACTURER:\t', rec[2])
            print('DATE OF MANUFACTURE:\t', rec[3])
            print('DATE OF EXPIRY:\t', rec[4])
            print('QUANTITY STORED:\t', rec[5])
            print('INITIAL COST:\t', rec[8])

    def background_search_by_manu():#This function helps the user to search the details of the medicine by entering its manufacturer name
        ph = input('\nENTER THE MANUFACTURER NAME TO SEARCH:')
        sql = "Select name from Stock where manuf=%s"#This is the SQL syntex
        value = (ph,)
        mycur.execute(sql, value)
        rec = mycur.fetchall()#This line gives the output from mysql and stores it in the variable rec
        if rec == None:
            print('NO SUCH MANUFACTURER NAMED AS ',ph)
        else:
            print('----------MEDICINES MANUFACTURED BY', ph, '--------------------')
            for nm in rec:
                print(nm[0])

    def background_cost_update():#This function helps us to update the price of the medicine if we have entered it wrong in the previous entry
        sql = "Update stock set cost_unit=%s where name=%s"#This is the SQL syntex
        ph = input('\nENTER THE MEDICINE NAME TO CHANGE COST:')
        addr = int(input('\nENTER THE NEW COST PER UNIT:'))
        value = (addr, ph)
        try:
            mycur.execute(sql, value)
            mycon.commit()
            print('NEW COST OF', ph, 'IS ', addr,'Rs')
        except:
            print('UNABLE TO CHANGE COST!!!!')

    def background_sell():#This function helps the user to sell the medicine and decreasing the quantity in the mysql stock table
        sql = "Update stock set sell=%s,balance=%s where name=%s"
        ph = input('\nENTER THE MEDICINE NAME TO SELL:')
        addr = int(input('\nENTER THE QUANTITY TO SELL:'))
        sql2 = 'select quantity from stock where name=%s'
        value2 = (ph,)
        mycur.execute(sql2, value2)
        rec = mycur.fetchone()
        if addr > rec[0]:
            print('INSUFFICIENT STOCK IN HAND!!!!!!')
            return
        else:
            balance = rec[0] - addr
            value = (addr, balance, ph)
            try:
                mycur.execute(sql, value)
                mycon.commit()
                print(addr, 'UNITS OF', ph, 'SOLD')
                print(balance, 'UNITS LEFT')
            except:
                print('UNABLE TO SELL MEDICINE!!!!')

    def background_available():#This function tells us about the quantities left out of the medicine name entered
        ph = input('\nENTER THE MEDICINE NAME TO SEARCH:')
        sql = "Select balance from Stock where name=%s"
        value = (ph,)
        mycur.execute(sql, value)
        rec = mycur.fetchone()
        if rec == None:
            print(ph, 'IS NOT AVAILABLE')
        else:
            print(rec[0], 'UNITS OF', ph, 'IS AVAILABLE')

    def background_dispose():#This function helps to find out the expired medicines
        sql = "Insert into dispose(batch_no,name,date_exp,amount)values(%s,%s,%s,%s)"
        nm = input('\nENTER THE MEDICINE NAME TO DISPOSE:')
        sql2 = "Select batch_no,name,date_exp,balance from stock where name=%s and date_exp<=%s"
        t_date = datetime.date.today()
        value2 = (nm, t_date)
        mycur.execute(sql2, value2)
        rec = mycur.fetchone()
        if rec == None:
            print(nm, 'IS NOT EXPIRED YET OR NOT AVAILABLE IN STOCK')
        else:
            print(nm, 'IS EXPIRED')
            c = int(input('\nPRESS 1 TO DISPOSE IT:'))
            if c == 1:#Entering 1 removes the medicine from the stock table and them adds that into teh dispose table which means that the medicine is expired
                b = rec[0]
                n = rec[1]
                d = rec[2]
                am = rec[3]
                value = (b, n, d, am)
                sql3 = 'Delete from stock where name=%s'
                value3 = (n,)
                try:
                    mycur.execute(sql, value)
                    mycon.commit()
                    print(n, 'SUCCESSFULLY DISPOSED')
                    mycur.execute(sql3, value3)
                    mycon.commit()
                except:
                    print('UNABLE TO DISPOSE MEDICINE')
            else:
                print('WARNING!!!!!', nm, 'MUST BE DISPOSED , ALREADY EXPIRED')
        return

    def background_search_dispose():#This function searches and displays details of disposed medicines (expired) by their name from the "Dispose" table in the MySQL database.
        ph = input('\nENTER THE DISPOSED MEDICINE NAME TO SEARCH:')
        sql = "Select * from Dispose where name=%s"
        value = (ph,)
        mycur.execute(sql, value)
        rec = mycur.fetchone()
        if rec == None:
            print(ph, 'IS NOT AVAILABLE')
        else:
            print('BATCH NUMBER:\t', rec[0])
            print('MEDICINE NAME:\t', rec[1])
            print('DATE OF EXPIRY:\t', rec[2])
            print('BALANCE AMOUNT:\t', rec[3])

    def background_close():#This function is used to close the program with successful execution
        #os.system('cls') ###NOT REQUIRED###
        print('\nTHANK YOU FOR USING THE APPLICATION')
        quit()

    
    #Function starting point  
    print('------------WELCOME TO MEDICINE STOCK CHECKING SYSTEM-------------\n\n')

    while True:
        #os.system('cls')  # Use 'clear' on Linux/macOS or 'cls' on Windows      #####NOT RESPONDING#####
        print('\nPRESS 1 TO ADD A NEW MEDICINE')
        print('PRESS 2 TO SEARCH A MEDICINE BY NAME')
        print('PRESS 3 TO SEARCH A MEDICINE BY MANUFACTURER')
        print('PRESS 4 TO UPDATE MEDICINE COST')
        print('PRESS 5 TO SELL MEDICINE')
        print('PRESS 6 TO CHECK AVAILABILITY')
        print('PRESS 7 TO DISPOSE EXPIRED MEDICINE')
        print('PRESS 8 TO SEARCH EXPIRED MEDICINE BY NAME')
        print('PRESS 9 TO CLOSE THE APPLICATION')

        choice = int(input('ENTER YOUR CHOICE : '))

        if choice == 1:
            background_store()
        elif choice == 2:
            background_search_by_name()
        elif choice == 3:
            background_search_by_manu()
        elif choice == 4:
            background_cost_update()
        elif choice == 5:
            background_sell()
        elif choice == 6:
            background_available()
        elif choice == 7:
            background_dispose()
        elif choice == 8:
            background_search_dispose()
        else:
            background_close()

'''label = Label(frame, text="don't have any account?", fg='black', bg='white',font=('Microsoft YaHei UI Light', 10))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='signup', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)'''#Not necessary for this page i guess

root.mainloop()
