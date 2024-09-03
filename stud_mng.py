#============Importing Library================

#pip install tkinter
from tkinter import*

#import ttk from tkinter
from tkinter import ttk

#pip install pymysql
import pymysql

#import messagebox from tkinter
from tkinter import messagebox

#===========Defining Student Class============
class Student:

    #==========Define default constructor==========
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1260x700+0+0")
        self.root.config(bg="black")

        #==================title on root window===================
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("calibri",30,"bold"),bg="black",fg="orange")
        title.pack(side=TOP,fill=X)

#===========All Variables======================

        self.roll_no_var = StringVar()

        self.name_var = StringVar()

        self.email_var = StringVar()

        self.gender_var = StringVar()

        self.contact_var = StringVar()

        self.dob_var = StringVar()

        self.search_by = StringVar()

        self.search_tx = StringVar()

#==============Manage Frame====================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=10,y=80,width=450,height=580)

        #===========Title Label==========
        m_title=Label(Manage_Frame,text="Manage Student",bg="black",fg="orange",font=("calibri",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #===========Roll No. Label==========
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        #============Roll no. Entry Field =========
        txt_Roll=Entry(Manage_Frame,textvariable=self.roll_no_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #===========Name Label==========
        lbl_name=Label(Manage_Frame,text="Name",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        #============Name Entry Field =========
        txt_Name=Entry(Manage_Frame,textvariable=self.name_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #============Email Label=========
        lbl_email=Label(Manage_Frame,text="Email",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        #============Email Entry Field =========
        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #============Gender Label=========
        lbl_gender=Label(Manage_Frame,text="Gender",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        #===========Combobox on gender fields========
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,width=19,font=("calibri",14,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #============Contact Label=========
        lbl_contact=Label(Manage_Frame,text="Contact",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        #============Contact. Entry Field =========
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #============DOB Label=========
        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        #============D.O.B Entry Field =========
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #============Address Label=========
        lbl_address=Label(Manage_Frame,text="Address",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        #============Text Field for Address============
        self.txt_address=Text(Manage_Frame,width=20,height=2,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#==============Button Frame====================

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="orange")
        btn_Frame.place(x=10,y=530,width=420)

        #=====Add Button===========
        addbtn = Button(btn_Frame,text="Add",width=10,command=self.add_student).grid(row=1,column=0,padx=10,pady=10)
       
        #=====Update Button========
        updatebtn = Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=1,column=1,padx=10,pady=10)
       
        #========Delete Button=====
        deletebtn = Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=1,column=2,padx=10,pady=10)
       
        #=========Clear Button=======
        clearbtn = Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=1,column=3,padx=10,pady=10)

#==============Detail Frame====================   
    
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=470,y=80,width=800,height=580)

        #============Search Label=========
        lbl_search=Label(Detail_Frame,text="Search",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        #============Combobox for search=========
        combo_search=ttk.Combobox(Detail_Frame,width=15,textvariable=self.search_by,font=("calibri",14,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        #============Search Entry Field =========
        txt_search=Entry(Detail_Frame,width=15,textvariable=self.search_tx,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        #=====Seaarch Button======
        searchbtn = Button(Detail_Frame,text="Search",bg="orange",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        
        #=====Show Button=========
        showbtn = Button(Detail_Frame,text="Show",bg="orange",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#==============Table Frame====================== 
       
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="orange")
        Table_Frame.place(x=10,y=60,width=765,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll no.","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command= self.Student_table.xview)
        scroll_y.config(command= self.Student_table.yview)

        #============Headings for Student Table===========
        self.Student_table.heading("roll no.",text="Roll No.")

        self.Student_table.heading("name",text="Name")

        self.Student_table.heading("email",text="Email")

        self.Student_table.heading("gender",text="Gender")

        self.Student_table.heading("contact",text="Contact")

        self.Student_table.heading("dob",text="D.O.B")

        self.Student_table.heading("address",text="Address")


        self.Student_table['show']='headings'
        self.Student_table.column("roll no.",width=50)

        self.Student_table.column("name",width=100)

        self.Student_table.column("email",width=100)

        self.Student_table.column("gender",width=100)

        self.Student_table.column("contact",width=100)

        self.Student_table.column("dob",width=100)

        self.Student_table.column("address",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #=====Call fetch data function========
        self.fetch_data()

#=============Create add_student function=========

#============Connectivity with Database=========

#====================Validation on Required Fields======================
    def add_student(self):
        if self.roll_no_var.get()=="" :
                messagebox.showerror("Error","All fields are required!!!")

        elif self.name_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        elif self.gender_var.get()=="" :
                messagebox.showerror("Error","All fields are required!!!")

        elif self.email_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        elif  self.dob_var.get()=="":
                messagebox.showerror("Error","All fields are required")

        else:
                con=pymysql.connect(host="localhost", user="root", password="", database = "stud")    
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),

                                                                                self.name_var.get(),

                                                                                self.email_var.get(),

                                                                                self.gender_var.get(),

                                                                                self.contact_var.get(),

                                                                                self.dob_var.get(),

                                                                                self.txt_address.get('1.0',END) 
                                                                                ))
                con.commit()
                self.fetch_data()
                self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been successfully inserted")

#=============Create fetch_data function=========

#============Connectivity with Database============
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stud")    
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()

        if len(rows)!=0:
                
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()

#=============Create clear function=========
    def clear(self):

        self.roll_no_var.set("")

        self.name_var.set("")

        self.email_var.set("")

        self.gender_var.set("")

        self.contact_var.set("")

        self.dob_var.set("")

        self.txt_address.delete('1.0',END)

#=============Create get_ cursor=========
    def get_cursor(self,ev):

        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.roll_no_var.set(row[0])

        self.name_var.set(row[1])

        self.email_var.set(row[2])

        self.gender_var.set(row[3])

        self.contact_var.set(row[4])

        self.dob_var.set(row[5])

        self.txt_address.delete("1.0",END)

        self.txt_address.insert(END,row[6])

#=============Create update_data function=========
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database = "stud")    
        cur=con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s  where roll_no=%s",
                                                                (self.name_var.get(),

                                                                self.email_var.get(),

                                                                self.gender_var.get(),

                                                                self.contact_var.get(),

                                                                self.dob_var.get(),

                                                                self.txt_address.get('1.0',END),

                                                                self.roll_no_var.get() 
                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record Update Successfully")

#=============Create delete_data function=========
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stud")    
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close() 
        messagebox.showinfo("Success","Record Delete Successfully")
        self.fetch_data()
        self.clear()

#========Create search_data function==========
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stud")    
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_tx.get())+"%'")
        rows = cur.fetchall()

        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())

                for row in rows:
                   self.Student_table.insert('',END,values=row)

                con.commit()
        con.close()
        
root=Tk()
ob=Student(root)
root.mainloop()