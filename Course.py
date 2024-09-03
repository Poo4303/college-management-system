#============Importing Library================

#pip install tkinter
from tkinter import*

#import ttk from tkinter
from tkinter import ttk

#pip install pymysql
import pymysql

#import messagebox from tkinter
from tkinter import messagebox

#===========Defining Course Class============
class Course:

    #==========Define default constructor==========
    def __init__(self,root):
        self.root=root
        self.root.title("Courses Profile")
        self.root.geometry("1200x600+0+0")
        self.root.config(bg="black")

#===========All Variables======================

        self.course_var = StringVar()

        self.duration_var = StringVar()

        self.teacher_var = StringVar()

        self.fee_var = StringVar()

        #==================title on root window===================
        title=Label(self.root,text="Courses Detail",bd=10,relief=GROOVE,font=("calibri",30,"bold"),bg="black",fg="orange")
        title.pack(side=TOP,fill=X)

        #==============Manage Frame====================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=10,y=80,width=450,height=513)

        #===========Title Label==========
        m_title=Label(Manage_Frame,text="Manage Course",bg="black",fg="orange",font=("calibri",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #===========Roll No. Label==========
        lbl_course=Label(Manage_Frame,text="Course Name",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_course.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        #============Roll no. Entry Field =========
        txt_Course=Entry(Manage_Frame,textvariable=self.course_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Course.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #===========Name Label==========
        lbl_dur=Label(Manage_Frame,text="Duration",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_dur.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        #============Name Entry Field =========
        txt_Dur=Entry(Manage_Frame,textvariable=self.duration_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Dur.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #============Email Label=========
        lbl_teach=Label(Manage_Frame,text="Teacher",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_teach.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        #============Email Entry Field =========
        txt_Teach=Entry(Manage_Frame,textvariable=self.teacher_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Teach.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #============Email Label=========
        lbl_fee=Label(Manage_Frame,text="Fee",bg="black",fg="orange",font=("calibri",20,"bold"))
        lbl_fee.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        #============Email Entry Field =========
        txt_Fee=Entry(Manage_Frame,textvariable=self.fee_var,font=("calibri",15,"bold"),bd=5,relief=GROOVE)
        txt_Fee.grid(row=4,column=1,pady=10,padx=20,sticky="w")

#==============================Buttons========================================= 

        #=====Add Button==============
        addbtn = Button(Manage_Frame,text="Add",bg='khaki',fg="black",bd=7,command=self.add_student,font=("times new roman",20,"bold")).place(x=70,y=360,width=110,height=40)
       
        #=========Update Button=======
        updatebtn = Button(Manage_Frame,text="Update",bg='khaki',fg="black",bd=7,command=self.update_data,font=("times new roman",20,"bold")).place(x=255,y=360,width=110,height=40)
        
        #========Clear Button=========
        clearbtn = Button(Manage_Frame,text="Clear",bg='khaki',fg="black",bd=7,command=self.clear,font=("times new roman",20,"bold")).place(x=159,y=430,width=110,height=40)
       
        #==============Detail Frame====================   
    
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=470,y=80,width=800,height=580)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="orange")
        Table_Frame.place(x=13,y=8,width=700,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.Student_table=ttk.Treeview(Table_Frame,columns=("course","duration","teacher","fee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command= self.Student_table.xview)
        scroll_y.config(command= self.Student_table.yview)

        #============Headings for Student Table===========
        self.Student_table.heading("course",text="Course")

        self.Student_table.heading("duration",text="Duration")

        self.Student_table.heading("teacher",text="Teacher")

        self.Student_table.heading("fee",text="Fee")


        self.Student_table['show']='headings'
        self.Student_table.column("course",width=80)

        self.Student_table.column("duration",width=100)

        self.Student_table.column("teacher",width=100)

        self.Student_table.column("fee",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        #=====Call fetch data function========
        self.fetch_data()

#=============Create add_student function=========

#============Connectivity with Database=========

#====================Validation on Required Fields======================
    def add_student(self):
        if self.course_var.get()=="" or self.duration_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        elif self.teacher_var.get()=="" or self.fee_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")

        else:
                con=pymysql.connect(host="localhost", user="root", password="", database = "stud")    
                cur=con.cursor()
                cur.execute("insert into course values(%s,%s,%s,%s)",(self.course_var.get(),

                                                                      self.duration_var.get(),

                                                                      self.teacher_var.get(),

                                                                      self.fee_var.get(), 
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
        cur.execute("select * from course")
        rows=cur.fetchall()

        if len(rows)!=0:
                
                self.Student_table.delete(*self.Student_table.get_children())

                for row in rows:
                        self.Student_table.insert('',END,values=row)

                con.commit()
        con.close()

#=============Create clear function=========
    def clear(self):

        self.course_var.set("")

        self.duration_var.set("")

        self.teacher_var.set("")

        self.fee_var.set("")

#=============Create get_ cursor=========
    def get_cursor(self,ev):

        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.course_var.set(row[0])

        self.duration_var.set(row[1])

        self.teacher_var.set(row[2])

        self.fee_var.set(row[3])

#=============Create update_data function=========
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database = "stud")    
        cur=con.cursor()
        cur.execute("update course set duration=%s, teacher=%s, fee=%s where course=%s",
                                                                (self.duration_var.get(),

                                                                self.teacher_var.get(),

                                                                self.fee_var.get(),

                                                                self.course_var.get() 
                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record Update Successfully")



root=Tk()
ob=Course(root)
root.mainloop()