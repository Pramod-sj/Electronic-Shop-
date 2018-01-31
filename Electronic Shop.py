#copy the electronic_databse file and paste it to c:/wamp64/bin/mysql/mysqlx.x.x/data/
from tkinter import *           #for gui
#please install mysql connect to use this module
import mysql.connector          #for database
import re
import time
import smtplib                  #sendind mail
from datetime import date       #license checking
t=time.localtime()
d=date(t.tm_year,t.tm_mon,t.tm_mday)
ed=date(2018,1,4)
remain=ed-d
conn=mysql.connector.connect(user="root",password="",database="Electronic_shop")
#remove below commenting if you want database functionality and customize according to your need
#for further need ask me...Surely help you 
#try to have same table in your database...or you will get some errors.
#conn=mysql.connector.connect(user="enter user",password="enter password",database="enter your database name")
cursor=conn.cursor()
window=Tk()
window.title('Electronic Shop')
#All Frames
f1=Frame(window)                    #frame for login
fb=Frame(window)                    #contains a canvas and frame(f2) in it
f2=Frame(fb,height=400,width=700)   #frame for start window
f3=Frame(window,height=400,width=700)
f4=Frame(window,height=400,width=700)
f5=Frame(window,height=400,width=700)
f6=Frame(window,height=400,width=700)
f7=Frame(window,height=400,width=700)
f8=Frame(window)        #GUI for customer data entry
f9=Frame(window)        #GUI for Order data entry
f10=Frame(window)       #GUI for Item data entry
f11=Frame(window)       #GUI for Payment data entry
#Logout Top menu bar
def logout():
    fb.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f8.pack_forget()
    f9.pack_forget()
    f10.pack_forget()
    f11.pack_forget()
    e1.delete(0,'end')
    e2.delete(0,'end')
    if(x.get()==1):
        y.set("")
        g.set("")
        gmail.destroy()
        send.destroy()
        bu=Button(f1,text="Forget\nPassword",command=forgetPassword)
        bu.grid(row=8,column=2,sticky='w')
    disable()
    f1.pack()
#Start Top menu bar call
def Start():
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()
    f10.pack_forget()
    f11.pack_forget()
    f2.pack()
    fb.pack()
def q():
    window.destroy()
#disable
def disable():
    menubar.entryconfig("Start", state="disabled")
    menubar.entryconfig("Table", state="disabled")
    menubar.entryconfig("Logout", state="disabled")
    menubar.entryconfig("Help", state="disabled")
    menubar.entryconfig("Feedback", state="disabled")
#Login Button Click Call
def login():
    pass_word=p.get()
    user_name=u.get()
    if( user_name==username and pass_word==password ):
        messagebox.showinfo("welcome","Welcome Pramod...!")
        canvas.pack()
        f2.pack()
        fb.pack()
        f1.pack_forget()
        if(remain.days<1):
            fb.pack_forget()
            f2.pack_forget()
            f1.pack()
            messagebox.showinfo(":|","License Expired")
            return None
        #enable menu
        menubar.entryconfig("Start", state="normal")
        menubar.entryconfig("Table", state="normal")
        menubar.entryconfig("Logout", state="normal")
        menubar.entryconfig("Help", state="normal")
        menubar.entryconfig("Feedback", state="normal")
        #end of enable menu

    else:
        messagebox.showinfo("Goodbye","Incorrect username or password")
#Top menu help
def about():
    messagebox.showinfo("about me","This Software is created by Pramod SJ")
def help():
    messagebox.showinfo("help index","For help please visit: www.elecsoft.com")
def License():  
    messagebox.showinfo("Licence","Working Licence "+str(remain.days)+" days are remaining.")
#TOp menu feedback form
def Feedback():
    def sendMessage():
        receiver='Receiver email id'
        sender='sender email id'
        feed=t.get(0.0,END)
        message=feed
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("sender email id","sender password")
            server.sendmail(sender, receiver, message)
            server.close()
            messagebox.showinfo(":)","Thank You.......!")
            window1.destroy()
        except:
            messagebox.showinfo(":(","No proper Connection or Email id is incorrect")
            return None
        
    window1=Tk()
    window1.title("Feedback Form")
    t=Text(window1)
    t.pack()
    Button(window1,text="Send",command=message).pack()
    window1.mainloop()
#All DATABASE MANAGEMENT STUFF
def insert():
    if(val.get()==0):
        m_name=name.get()
        m_number=number.get()
        m_addr=addr.get()
        m_gen=gen.get()
        if(m_gen==1):
            m_gen='M'
        elif(m_gen==2):
            m_gen='F'
        m_posid=posid.get()
        if(not m_name or not m_number or not m_addr or not m_gen or not m_posid or option=='select'):
            messagebox.showinfo(":(","Please fill all fields")
            return None
            
        if not(re.match("^[a-zA-Z\s']+$",m_name)):
            messagebox.showinfo(":(","Name cannot have number or special character")
            return None
        if(len(m_number)==10):
            if re.match('^[789]\d{9}',m_number):
                query="select * from customer where cust_phone="+m_number

                cursor.execute(query)
                
                if(cursor.fetchone()!=None):
                    messagebox.showinfo(":(","Phone number already exist")
                    return None
                 
            else:
                messagebox.showinfo(":(","Phone number is invalid")
                return None
        else:
            messagebox.showinfo(":(","Phone number is invalid")
            return None
        
        if(re.match(r'^\d$',m_addr)):
            messagebox.showinfo(":(","Adress Can't be a number")
            return None
        if not(re.match(r'^[0-9]{6,6}$',m_posid)):
            messagebox.showinfo(":(","Please enter a valid Postal code")
            return None
        query='insert into customer (cust_name,cust_phone,cust_gender,cust_address,cust_city,postal_code) values("%s",%d,"%c","%s","%s",%d)'%(m_name,int(m_number),m_gen,m_addr,option,int(m_posid));
        cursor.execute(query)
        messagebox.showinfo(":)","Data is Successfully added")
        id.set("")
        name.set("")
        addr.set("")
        number.set("")
        posid.set("")
        r1.deselect()
        r2.deselect()
        selected.set('Select City')
        #cust_fetch()
        customer()
    elif (val.get()==2):
        d=cust_det.split(":")
        if(o_custid.get()=="Select Customer" or q_sel.get()=='Select quantity'  or category.get()=='Select Category' or cat.get()=="Select Product"):
            messagebox.showinfo(":(","Please fill all fields")
            return None
        cust_id=cust_det.split(":")
        query="select cust_id from customer where cust_id=%d"%(int(cust_id[0]))
        cursor.execute(query)
        check=cursor.fetchone()
        if(check==None):
            messagebox.showinfo(":(","Customer Doesn't exists")
            return None
    
        query="select unit_price,stock from item where item_name='%s'"%(product_name)
        cursor.execute(query)
        content=cursor.fetchone()
        prod_price=content[0]
        cur_stock=content[1]-int(quantity)
        if(content[1]<int(quantity)):
            messagebox.showinfo(":(","Quantity Exceed Only "+str(content[1])+" unit are remaining...!")
            return None     
        up_query="update item set stock=%d where item_name='%s'"%(cur_stock,product_name)
        cursor.execute(up_query)
        t_price=int(quantity)*int(prod_price)
        query='insert into order_details(product_name,quantity,price,total_price,cust_id,purchase_date,category,status) values("%s",%d,%d,%d,%d,sysdate(),"%s","Not Paid")'%(product_name,int(quantity),float(prod_price),float(t_price),int(float(d[0])),option)
        cursor.execute(query)
        messagebox.showinfo(":)","Data is Successfully added")
        o_custid.set("Select Customer")
        category.set('Select Category')
        cat.set("Select Product")
        q_sel.set("Select quantity")
        #ord_fetch()
        ord()
    elif (val.get()==3):
        i_name=item_name.get()
        i_price=unit_price.get()
        s=stock.get()
        print(i_name)
        if (not i_name or not i_price or s=="" or category.get()=="Select Category"):
            messagebox.showinfo(":(","incomplete field")
            return None
        if not(re.match("^[a-zA-Z\s\d]+$",i_name)):
            messagebox.showinfo(":(","Name cannot have number or special character")
            return None
        if not(re.match("\d",i_price)):
            if int(i_price)<1:
                messagebox.showinfo(":(","price must be a +ve number")
                return None
            else:
                messagebox.showinfo(":(","price must be a number not character")
                return None
        if (int(s)<1):
            messagebox.showinfo(":(","Stock or Price cant be 0 or -ve")
            return None
        query="insert into item(item_name,stock,unit_price,item_category) values('%s',%d,%d,'%s')"%(i_name,int(s),int(i_price),option)
        cursor.execute(query)
        messagebox.showinfo(":)","Data is Successfully added")
        category.set("Select Category")
        item_name.set("")
        unit_price.set("")
        stock.set("")
        #item_fetch()
        item()
    elif (val.get()==4):
        if(payee.get()=='Select payee' or order.get()=="Select prod" or method.get()=="Select method"):
            messagebox.showinfo(":|","Empty Field")
            return None
        query="insert into payment(payee,total_amount,payment_method,ord_id) values('%s',%d,'%s',%d)"%(data[1],int(float(data2[2])),payment_type,int(data2[0]))
        cursor.execute(query)
        query="update order_details set status='Paid' where ord_id=%d"%(int(data2[0]))
        cursor.execute(query)
        messagebox.showinfo(":)","Data is Successfully added")
        payee.set("Select payee")
        order.set("Select prod")
        method.set("Select method")
        def refresh():
            f11.pack_forget()
            payment()
        b=Button(f11,text="refresh me",command=refresh,bd="3px")
        b.grid(row=10,column=0,columnspan=2)
def update():
    if(cur_sel.get()=='Select customer'):
        messagebox.showinfo(":(","Please select a customer id")
        return None
    if(cur_sel.get()=="Select item"):
        messagebox.showinfo(":(","Please select a item id")
        return None
    content=cur_selection.split(":")
    m_id=content[0]
    if(val.get()==0):
        cursor.execute("select cust_id from customer")
        c_id=cursor.fetchall()
        i=0
        bol=False
        if(number.get()=='' and addr.get()=="" and gen.get()==0 and posid.get()==""):
            messagebox.showinfo("Error","Please Enter Data\n You can only update number,gender,address and postal code....!")
            return None
        while(len(c_id)>i):
            if(int(m_id)==c_id[i][0]):
                #update statement for phone_number
                m_number=number.get()
                if(m_number):
                    if(len(m_number)==10):
                        if re.match('^[789]\d{9}',m_number):
                            print("correct")
                        else:
                            messagebox.showinfo("Error","Phone number is invalid")
                            return None
                    else:
                        messagebox.showinfo("Error","Phone number is invalid")
                        return None
                    query='update customer set cust_phone="%d" where cust_id=%d'%(int(m_number),int(m_id))
                    cursor.execute(query)
                        
                #update gender
                m_gen=gen.get()
                if(m_gen==1):
                    m_gen='M'
                elif(m_gen==2):
                    m_gen='F'
                if(m_gen):
                        query='update customer set cust_gender="%s" where cust_id=%d'%(m_gen,int(m_id))
                        cursor.execute(query)
                #update statement for address
                m_addr=addr.get()
                if(m_addr):
                    if(re.match(r'^\d$',m_addr)):
                        messagebox.showinfo(":(","Adress Can't be a number")
                        return None
                    else:
                        query='update customer set cust_address="%s" where cust_id=%d'%(m_addr,int(m_id))
                        cursor.execute(query)
                m_postal=posid.get()
                if(m_postal):
                    if not(re.match("^[0-9]{6,6}$",m_postal)):
                        messagebox.showinfo(":(","Please enter a valid Postal code")
                        return None
                    else:
                        query='update customer set postal_code="%d" where cust_id=%d'%(int(m_postal),int(m_id))
                        cursor.execute(query)
                messagebox.showinfo(":)","Successfully UPpated the new values")
                bol=True
            i+=1
        if not bol:
            messagebox.showinfo(":(","No data found")
            return None
        addr.set("")
        number.set("")
        posid.set("")
        r1.deselect()
        r2.deselect()
        cur_sel.set("Select customer")
    elif(val.get()==3):
        m_q=stock.get()
        cursor.execute("select stock from item where id=%d"%(int(m_id)))
        temp=cursor.fetchone()
        print(temp)
        if(temp==None):
            messagebox.showinfo(":(","No item Exist")
            return None
        if(not m_q):
            messagebox.showinfo(":|","You can only update Stock value")
            return None
        m_q=temp[0]+int(m_q)
        query='update item set stock=%d where id=%d'%(int(m_q),int(m_id))
        cursor.execute(query)
        print(query)
        messagebox.showinfo(":)","Stock value is successfully updated")
        stock.set("")
        cur_sel.set("Select item")
    
def delete():
    if(cur_sel.get()=='Select customer'):
        messagebox.showinfo(":(","Please select a customer id")
        return None
    if(cur_sel.get()=="Select order" ):
        messagebox.showinfo(":(","Please select a order id")
        return None
    if(cur_sel.get()=="Select item"):
        messagebox.showinfo(":(","Please select a item id")
        return None
    content=cur_selection.split(":")
    m_id=content[0]
    if(val.get()==0):
        cursor.execute("select cust_id from customer")
        c_id=cursor.fetchall()
        query="select cust_id from customer where cust_id=%d"%(int(m_id))
        cursor.execute(query)
        if(cursor.fetchone()==None):
            messagebox.showinfo(":(","No data found")
            return None
        query='delete from customer where cust_id=%d'%(int(m_id))
        cursor.execute(query)
        cur_sel.set("Select customer")
        cust_fetch()
    elif(val.get()==2):
        query="select ord_id from order_details where ord_id=%d"%(int(m_id))
        cursor.execute(query)
        if(cursor.fetchone()==None):
            messagebox.showinfo(":(","No data found")
            return None
        query='delete from order_details where ord_id=%d'%(int(m_id))
        cursor.execute(query)
        cur_sel.set("Select order")
        ord_fetch()
    elif(val.get())==3:
        
        query="select id from item where id=%d"%(int(m_id))
        cursor.execute(query)
        if(cursor.fetchone()==None):
            messagebox.showinfo(":(","No data found")
            return None
        query='delete from item where id=%d'%(int(m_id))
        cursor.execute(query)
        cur_sel.set("Select customer")
        item_fetch()
    messagebox.showinfo(":)","data deleted successfully")
    
#####################END OF DBMS STUFF

###############GUI FOR CUSTOMER
def cust_fetch():
    query="select cust_id,cust_name from customer order by cust_id"
    cursor.execute(query)
    content=cursor.fetchall()
    print()
    i=0
    cust_list=[]
    while(len(content)>i):
        cust_deat=str(content[i][0])+" : "+content[i][1]
        cust_list.append(cust_deat)
        i+=1
    def on_change(value):
        global cur_selection
        cur_selection=cur_sel.get()
    global cur_sel
    cur_sel=StringVar(value="Select customer")
    cust_op = OptionMenu(f8, cur_sel, *(cust_list), command=on_change)
    cust_op.grid(row=13,column=1,sticky=W)
    cust_op.configure(width=20)
def customer():
    val.set(0)
    fb.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f9.pack_forget()
    f10.pack_forget()
    f11.pack_forget()
    f8.pack()
    l=Label(f8,text="     Customer Entry     ",font="Times 60 bold")
    l.grid(row=0,column=0,columnspan=2)
    global id,name,addr,gen,number,posid,r1,r2,selected
    id=StringVar()
    name=StringVar()
    number=StringVar()
    addr=StringVar()
    gen=IntVar()
    posid=StringVar()
    t4=Label(f8,text="Name:",font="Verdana 10 bold")
    t4.grid(row=1,column=0,sticky=E)
    e4=Entry(f8,textvariable=name,width=20,bd='3px')
    e4.grid(row=1,column=1,sticky=W)
    t6=Label(f8,text="Gender:",font="Verdana 10 bold")
    t6.grid(row=2,column=0,sticky=E)
    r1=Radiobutton(f8,text="Male",variable=gen,value=1)
    r1.grid(row=2,column=1,sticky=W)
    r2=Radiobutton(f8,text="Female",variable=gen,value=2)
    r2.grid(row=3,column=1,sticky=W)
    t5=Label(f8,text="Phone no:",font="Verdana 10 bold")
    t5.grid(row=4,column=0,sticky=E)
    e5=Entry(f8,textvariable=number,width=20,bd='3px')
    e5.grid(row=4,column=1,sticky=W)
    t5=Label(f8,text="Address:",font="Verdana 10 bold")
    t5.grid(row=5,column=0,sticky=E)
    e6=Entry(f8,textvariable=addr,width=30,bd='3px')
    e6.grid(row=5,column=1,sticky=W)
    t5=Label(f8,text="City:",font="Verdana 10 bold")
    t5.grid(row=6,column=0,sticky=E)
    def on_change_selection(value):
        global option
        option=selected.get()
    options = ["Mumbai","Delhi","Kolkata","Pune","Dehradun","Jaipur","Chennai","Bengluru","Ahmedabad","Surat"]
    selected = StringVar(value="Select City")
    op = OptionMenu(f8, selected, *(options), command=on_change_selection)
    op.grid(row=6,column=1,sticky=W)
    op.configure(width=20)
    t5=Label(f8,text="Postal code:",font="Verdana 10 bold")
    t5.grid(row=7,column=0,sticky=E)
    e7=Entry(f8,textvariable=posid,bd="3px")
    e7.grid(row=7,column=1,sticky=W)
    #buttons
    t=Label(f8,text="")
    t.grid(row=8,column=0)
    b2=Button(f8,text="Add Data",command=insert,width=10,font="Times 11 bold",bd="3px")
    b2.grid(row=9,column=0,columnspan=2)
    #########################################
    t=Label(f8,text="----------------------------------------------------------------------------------------------")
    t.grid(row=10,column=0,columnspan=2)
    t=Label(f8,text="")
    t.grid(row=11,column=0)
    t7=Label(f8,text="Update and Delete Section",font="Times 15 bold")
    t7.grid(row=12,column=0,columnspan=2)
    ########################
    t6=Label(f8,text="Id:",font="Verdana 10 bold")
    t6.grid(row=13,column=0,sticky=E)
    cust_fetch()
    t6=Label(f8,text="")
    t6.grid(row=14,column=2)
    b3=Button(f8,text="Update",command=update,width=10,font="Times 11 bold")
    b3.grid(row=15,column=0,columnspan=2)
    t6=Label(f8,text="")
    t6.grid(row=16,column=2)
    b4=Button(f8,text="delete",command=delete,width=10,font="Times 11 bold")
    b4.grid(row=17,column=0,columnspan=2)
    t6=Label(f8,text="")
    t6.grid(row=18,column=2)
#GUI for Order
def ord_fetch():
    query="select ord_id,product_name from order_details order by ord_id"
    cursor.execute(query)
    content=cursor.fetchall()
    print()
    i=0
    ord_list=[]
    while(len(content)>i):
        cust_deat=str(content[i][0])+" : "+content[i][1]
        ord_list.append(cust_deat)
        i+=1
    def on_change(value):
        global cur_selection
        cur_selection=cur_sel.get()
    global cur_sel
    cur_sel=StringVar(value="Select order")
    cust_op = OptionMenu(f9, cur_sel, *(ord_list), command=on_change)
    cust_op.grid(row=13,column=1,sticky=W)
    cust_op.configure(width=20)
def ord():
    val.set(2)
    fb.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f10.pack_forget()
    f11.pack_forget()
    f9.pack()
    global quantity
    global category
    global product_name
    global o_custid
    product_name=StringVar()
    p_price=StringVar()
    quantity=StringVar()
    
    l=Label(f9,text="     Order Entry     ",font="Times 60 bold")
    l.grid(row=0,column=0,columnspan=2,sticky=W)
    Label(f9,text="").grid(row=1,column=0)
    t6=Label(f9,text="Category:",font="Verdana 12 bold")
    t6.grid(row=2,column=0,sticky=E)
    t5=Label(f9,text="product_name:",font="Verdana 12 bold")
    t5.grid(row=3,column=0,sticky=E)
    t6=Label(f9,text="quantity:",font="Verdana 12 bold")
    t6.grid(row=4,column=0,sticky=E)
    t6=Label(f9,text="cust id:",font="Verdana 12 bold")
    t6.grid(row=5,column=0,sticky=E)
    o_custid=StringVar(value="Select Customer")
    cursor.execute("select cust_id,cust_name from customer")
    content=cursor.fetchall()
    i=0
    customer=[]
    global q_sel
    q_sel=StringVar(value="Select quantity") 
    q=[1,2,3,4,5,6,7,8,9,10]
    def quantity_sel(value):
        global quantity
        quantity=q_sel.get()
    
    q_selection= OptionMenu(f9, q_sel, *(q), command=quantity_sel)
    q_selection.grid(row=4,column=1,sticky=W)
    q_selection.configure(width=20)
    while(len(content)>i):
        data=str(content[i][0])+" : "+content[i][1]
        customer.append(data)
        i+=1
    def cust_selection(value):
        global cust_det
        cust_det=o_custid.get()
    c_selection= OptionMenu(f9, o_custid, *(customer), command=cust_selection)
    c_selection.grid(row=5,column=1,sticky=W)
    c_selection.configure(width=20)
    global cat
    cat=StringVar(value="Select Product")  #default value of option menu
    def on_change_selection(value):
        global option
        option=category.get()
        print(option)
        op=[]
        query="Select item_name,stock from item where item_category='%s'"%(option)
        print(query)
        cursor.execute(query)
        item=cursor.fetchone()
        while(item!=None):
            op.append(item[0])
            item=cursor.fetchone()
        quantity=content[1]
        def on_selection(value):
            global product_name
            product_name=cat.get()
        #selected = tk.StringVar()
        #selected.set("one")
        op1= OptionMenu(f9, cat, *(op), command=on_selection)
        op1.grid(row=3,column=1,sticky=W)
        op1.configure(width=20)
    itemfetch="select distinct(item_category) from item"
    cursor.execute(itemfetch)
    item_cat=cursor.fetchone()
    options=[]
    while(item_cat!=None):
        options.append(item_cat[0])
        item_cat=cursor.fetchone()
    #options = ["Audio Devices","Mobile accessories","Computer stuff","Home Appliances","Mobile Devices"]
    global category
    category= StringVar(value="Select Category")
    #selected = tk.StringVar()
    #selected.set("one")
    op = OptionMenu(f9, category, *(options), command=on_change_selection)
    op.grid(row=2,column=1,sticky=W)
    op.configure(width=20)
    t6=Label(f9,text="")
    t6.grid(row=6,column=0)
    #buttons

    b3=Button(f9,text="Add Data",command=insert,width=10,font="Times 11 bold")
    b3.grid(row=8,column=0,columnspan=2)
    t6=Label(f9,text="")
    t6.grid(row=9,column=0)
    t7=Label(f9,text="---------------------------------------------",font="Verdana 10 bold")
    t7.grid(row=10,column=0,columnspan=2)
    t7=Label(f9,text="Delete Section",font="Times 15 bold")
    t7.grid(row=11,column=0,columnspan=2)
    t6=Label(f9,text="")
    t6.grid(row=12,column=0)
    global id
    id=StringVar()
    t6=Label(f9,text="id:",font="Verdana 12 bold")
    t6.grid(row=13,column=0,sticky=E)
    ord_fetch()
    t6=Label(f9,text="")
    t6.grid(row=14,column=0)
    b5=Button(f9,text="delete",command=delete,width=10,bd="3px",font="Times 11 bold")
    b5.grid(row=15,column=0,columnspan=2)
    t6=Label(f9,text="")
    t6.grid(row=16,column=0)
    
##end of order data GUI
def item_fetch():
    query="select id,item_name from item order by id"
    cursor.execute(query)
    content=cursor.fetchall()
    print()
    i=0
    item_list=[]
    while(len(content)>i):
        item_deat=str(content[i][0])+" : "+content[i][1]
        item_list.append(item_deat)
        i+=1
    def on_change(value):
        global cur_selection
        cur_selection=cur_sel.get()
    global cur_sel
    cur_sel=StringVar(value="Select item")
    item_op = OptionMenu(f10, cur_sel, *(item_list), command=on_change)
    item_op.grid(row=12,column=1,sticky=W)
    item_op.configure(width=20)
def item():
    val.set(3)
    fb.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()
    f11.pack_forget()
    f10.pack()
    global category,item_name,unit_price,stock,id,e6
    unit_price=StringVar()
    item_name=StringVar()
    stock=StringVar()
    l=Label(f10,text="     Item Entry     ",font="Times 60 bold")
    l.grid(row=0,column=0,columnspan=2,sticky=W)
    t6=Label(f10,text="")
    t6.grid(row=1,column=0)
    itemfetch="select distinct(item_category) from item"
    cursor.execute(itemfetch)
    item_cat=cursor.fetchone()
    options=[]
    def on_change1(value):
        global on_change1
        global option
        option=category.get()
    while(item_cat!=None):
        options.append(item_cat[0])
        item_cat=cursor.fetchone()
    #options = ["Audio Devices","Mobile accessories","Computer stuff","Home Appliances","Mobile Devices"]
    category= StringVar(value="Select Category")
    #selected = tk.StringVar()
    #selected.set("one")
    t6=Label(f10,text="Item Category:",font="Verdana 10 bold") 
    t6.grid(row=2,column=0,sticky=E)
    category= StringVar(value="Select Category")
    op = OptionMenu(f10, category, *(options),command=on_change1)
    op.grid(row=2,column=1,sticky=W)
    op.configure(width=20)
    t5=Label(f10,text="Item_name:",font="Verdana 10 bold")
    t5.grid(row=3,column=0,sticky=E)
    e6=Entry(f10,textvariable=item_name,bd="3px")
    e6.grid(row=3,column=1,sticky=W)
    t6=Label(f10,text="Unit_price:",font="Verdana 10 bold")
    t6.grid(row=4,column=0,sticky=E)
    e6=Entry(f10,textvariable=unit_price,bd="3px")
    e6.grid(row=4,column=1,sticky=W)
    t6=Label(f10,text="Stock:",font="Verdana 10 bold")
    t6.grid(row=5,column=0,sticky=E)
    e6=Entry(f10,textvariable=stock,bd="3px")
    e6.grid(row=5,column=1,sticky=W)
    t6=Label(f10,text="")
    t6.grid(row=6,column=0)
    b5=Button(f10,text="Add Data",command=insert,width=10)
    b5.grid(row=7,column=0,columnspan=2)
    t6=Label(f10,text="")
    t6.grid(row=8,column=0)
    t6=Label(f10,text="--------------------------------------------------------------------------------",font="Veranda 10 bold")
    t6.grid(row=9,column=0,columnspan=2)
    t6=Label(f10,text="Update And Delete Section",font="Times 15 bold")
    t6.grid(row=10,column=0,columnspan=2)
    t6=Label(f10,text="")
    t6.grid(row=11,column=0)
    id=StringVar()
    t5=Label(f10,text="ID:",font="Verdana 10 bold")
    t5.grid(row=12,column=0,sticky=E)
    item_fetch()
    t6=Label(f10,text="")
    t6.grid(row=13,column=0)
    b5=Button(f10,text="delete",command=delete,width=10,bd="3px",font="Times 11 bold")
    b5.grid(row=14,column=0,columnspan=2)
    t6=Label(f10,text="")
    t6.grid(row=15,column=0)
    b4=Button(f10,text="Update",command=update,width=10,bd="3px",font="Times 11 bold")
    b4.grid(row=16,column=0,columnspan=2)
    t6=Label(f10,text="")
    t6.grid(row=17,column=0)
    
################end of item block
def payment():
    val.set(4)
    fb.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()
    f10.pack_forget()
    f11.pack()
    global t_price,payee,method
    payee=StringVar()
    pay_method=StringVar()
    status=StringVar()
    t_price=IntVar()
    l=Label(f11,text="     Payment Entry     ",font="Times 60 bold")
    l.grid(row=0,column=0,columnspan=2,sticky=W)
    t6=Label(f11,text="")
    t6.grid(row=1,column=0)
    global order
    order= StringVar(value="Select Prod")  #All data about order
    def on_change(value):
        global payee_option
        payee_option=payee.get()
        global data  #for customer
        data=payee_option.split(":")    #1:pramodsj
        query="select o.total_price,o.product_name,o.ord_id from order_details o join customer c on c.cust_id=o.cust_id  where o.cust_id=%d and status='Not Paid'"%(int(data[0]))
        cursor.execute(query)
        content=cursor.fetchone()
        item1=[]
        j=0
        while(content!=None):
            d=str(content[2])+" : "+content[1]+" : "+str(content[0])#23:"Moto G3"
            item1.append(d)
            content=cursor.fetchone()
        def on_selection(value):
            global data2 #for order
            global order_detail
            order_detail=order.get()
            data2=order_detail.split(":")
            t_price.set(data2[2])
        #selected = tk.StringVar()
        #selected.set("one")
        op1= OptionMenu(f11,order, *(item1), command=on_selection)
        op1.grid(row=3,column=1,sticky=W)
        op1.configure(width=20)
    cursor.execute("select distinct(o.cust_id),c.cust_name from customer c join order_details o on c.cust_id=o.cust_id where status='Not Paid'")
    i_name=cursor.fetchall()
    options=[]
    i=0
    while(len(i_name)>i):
        id_name=str(i_name[i][0])+" : "+i_name[i][1]
        options.append(id_name)
        i+=1
    t5=Label(f11,text="Payee:",font="Veranda 10 bold")
    t5.grid(row=2,column=0,stick=E)
    t5=Label(f11,text="Ord_detail",font="Veranda 10 bold")
    t5.grid(row=3,column=0,stick=E)
    payee= StringVar(value="Select payee:")
    op = OptionMenu(f11, payee, *(options),command=on_change)
    op.grid(row=2,column=1,sticky=W)
    op.configure(width=20)
    t5=Label(f11,text="Payment type:",font="Veranda 10 bold")
    t5.grid(row=4,column=0,stick=E)
    def method_func(value):
        global payment_type
        payment_type=method.get()
       
    method_type=['Credit','Debit','Online Banking','Cash']
    method= StringVar(value="Select method")
    method_op = OptionMenu(f11, method, *(method_type),command=method_func)
    method_op.grid(row=4,column=1,sticky=W)
    method_op.configure(width=20)
    t6=Label(f11,text="Total_price:",font="Veranda 10 bold")
    t6.grid(row=5,column=0,stick=E)
    e6=Entry(f11,textvariable=t_price,bd="3px")
    e6.grid(row=5,column=1,sticky=W)
    t6=Label(f11,text="")
    t6.grid(row=7,column=0)
    
    b5=Button(f11,text="Add Data",command=insert,width=10,bd="3px",font="Times 11 bold")
    b5.grid(row=8,column=0,columnspan=2)
    t6=Label(f11,text="")
    t6.grid(row=9,column=0)
    

########################end of payment


        
##########fetching or displaying data#########
def goBack():
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    fb.pack()
def fetch():
    index=Lb1.curselection()
    if len(index)==0:
        messagebox.showinfo("Error","Please select database")
        return None
    fb.pack_forget()
    if index[0]==0:
        f3.pack()
        Label(f3,text="Cust_id").grid(row=0,column=0)
        Label(f3,text="Name").grid(row=0,column=1)
        Label(f3,text="Phone").grid(row=0,column=2)
        Label(f3,text="Gen").grid(row=0,column=3)
        Label(f3,text="Address").grid(row=0,column=4)
        Label(f3,text="City").grid(row=0,column=5)
        Label(f3,text="Postal code").grid(row=0,column=6)
        b1=Button(f3,text="Go Back",command=goBack,bd="3px")
        b1.grid(row=2,column=2,columnspan=6)
        Lb2=Listbox(f3,width=5,height=40)
        Lb2.grid(row=1,column=0)
        Lb3=Listbox(f3,width=20,height=40)
        Lb3.grid(row=1,column=1)
        Lb4=Listbox(f3,width=15,height=40)
        Lb4.grid(row=1,column=2)
        Lb5=Listbox(f3,width=5,height=40)
        Lb5.grid(row=1,column=3)
        Lb6=Listbox(f3,width=40,height=40)
        Lb6.grid(row=1,column=4)
        Lb7=Listbox(f3,width=10,height=40)
        Lb7.grid(row=1,column=5)
        Lb8=Listbox(f3,width=20,height=40)
        Lb8.grid(row=1,column=6)
        query="Select * from customer order by cust_id"
        cursor.execute(query)
        row=cursor.fetchall()
        a=1
        
        for i in row:
            Lb2.insert(a,i[0])
            Lb3.insert(a,i[1])
            Lb4.insert(a,i[2])
            Lb5.insert(a,i[3])
            Lb6.insert(a,i[4])
            Lb7.insert(a,i[5])
            Lb8.insert(a,i[6])
            a+=1
    elif index[0]==1:
        f4.pack()
        l1=Label(f4,text="Ord_id").grid(row=0,column=0)
        l2=Label(f4,text="product_Name").grid(row=0,column=1)
        l4=Label(f4,text="quantity").grid(row=0,column=2)
        l3=Label(f4,text="price").grid(row=0,column=3)
        l5=Label(f4,text="total_price").grid(row=0,column=4)
        l6=Label(f4,text="purchase_date").grid(row=0,column=5)
        b2=Button(f4,text="Go Back",command=goBack,bd="3px")
        b2.grid(row=2,column=2,columnspan=5)
        Lb2=Listbox(f4,width=5,height=40)
        Lb2.grid(row=1,column=0)
        Lb3=Listbox(f4,width=20,height=40)
        Lb3.grid(row=1,column=1)
        Lb4=Listbox(f4,width=9,height=40)
        Lb4.grid(row=1,column=2)
        Lb5=Listbox(f4,width=20,height=40)
        Lb5.grid(row=1,column=3)
        Lb6=Listbox(f4,width=20,height=40)
        Lb6.grid(row=1,column=4)
        Lb7=Listbox(f4,width=20,height=40)
        Lb7.grid(row=1,column=5)
        query="select * from order_details order by ord_id"
        cursor.execute(query)
        row=cursor.fetchall()
        a=1
        for i in row:
            Lb2.insert(a,i[0])
            Lb3.insert(a,i[1])
            Lb4.insert(a,i[2])
            Lb5.insert(a,i[3])
            Lb6.insert(a,i[4])
            Lb7.insert(a,i[6])
            a+=1
    elif index[0]==2:
        f5.pack()
        Label(f5,text="Item id").grid(row=0,column=0)
        Label(f5,text="Item Name").grid(row=0,column=1)
        Label(f5,text="Stock").grid(row=0,column=2)
        Label(f5,text="Unit price").grid(row=0,column=3)
        Label(f5,text="Item Category").grid(row=0,column=4)
        b2=Button(f5,text="Go Back",command=goBack,bd="3px")
        b2.grid(row=2,column=2,columnspan=4)
        Lb2=Listbox(f5,width=5,height=40)
        Lb2.grid(row=1,column=0)
        Lb3=Listbox(f5,width=20,height=40)
        Lb3.grid(row=1,column=1)
        Lb4=Listbox(f5,width=5,height=40)
        Lb4.grid(row=1,column=2)
        Lb5=Listbox(f5,width=20,height=40)
        Lb5.grid(row=1,column=3)
        Lb6=Listbox(f5,width=20,height=40)
        Lb6.grid(row=1,column=4)
        query="select * from item order by id"
        cursor.execute(query)
        row=cursor.fetchall()
        a=1
        for i in row:
            Lb2.insert(a,i[0])
            Lb3.insert(a,i[1])
            Lb4.insert(a,i[2])
            Lb5.insert(a,i[3])
            Lb6.insert(a,i[4])
            a+=1

    elif index[0]==3:
        f6.pack()
        Label(f6,text="Payment Id").grid(row=0,column=0)
        Label(f6,text="Payee").grid(row=0,column=1)
        Label(f6,text="Total amount").grid(row=0,column=2)
        Label(f6,text="Payment method").grid(row=0,column=3)
        Label(f6,text="Ord_id").grid(row=0,column=4)
        Label(f6,text="Prod_name").grid(row=0,column=5)
        b2=Button(f6,text="Go Back",command=goBack,bd="3px")
        b2.grid(row=2,column=2,columnspan=5)
        Lb2=Listbox(f6,width=10,height=40)
        Lb2.grid(row=1,column=0)
        Lb3=Listbox(f6,width=20,height=40)
        Lb3.grid(row=1,column=1)
        Lb4=Listbox(f6,width=10,height=40)
        Lb4.grid(row=1,column=2)
        Lb5=Listbox(f6,width=20,height=40)
        Lb5.grid(row=1,column=3)
        Lb6=Listbox(f6,width=20,height=40)
        Lb6.grid(row=1,column=4)
        Lb7=Listbox(f6,width=20,height=40)
        Lb7.grid(row=1,column=5)
        query="select p.payment_id,p.payee,p.total_amount,p.payment_method,o.ord_id,o.product_name from payment p join order_details o on o.ord_id=p.ord_id order by payment_id"
        cursor.execute(query)
        row=cursor.fetchall()
        a=1
        for i in row:
            Lb2.insert(a,i[0])
            Lb3.insert(a,i[1])
            Lb4.insert(a,i[2])
            Lb5.insert(a,i[3])
            Lb6.insert(a,i[4])
            Lb7.insert(a,i[5])
            a+=1

def joins():
    if(cur_sel.get()=='Select customer'):
        messagebox.showinfo(":(","Please Select Customer")
        return None
    sel=cur_selection.split(":")
    cursor.execute("select count(*) from customer c join order_details o on o.cust_id=c.cust_id where c.cust_id=%d"%(int(sel[0])))
    x=cursor.fetchall()
    s=IntVar()
    query='select c.Cust_id,c.cust_name,c.cust_phone,c.cust_city,o.ord_id,o.product_name,o.total_price,o.status from customer c join order_details o on o.cust_id=c.cust_id where o.cust_id=%d'%(int(sel[0]))
    cursor.execute(query)
    row=cursor.fetchall()
    
    if(row==[]):
        messagebox.showinfo(":|","NO item purchased yet")
        return None
    fb.pack_forget()
    f7.pack()
    global length,l_cust_name,l_cust_no,l_cust_id,Lb2,Lb3,Lb4;
    length=len(query)
    
    if(row==None):
        messagebox.showinfo(":|","NO item purchased yet")
        return None
    l_cust_name=StringVar()
    l_cust_id=IntVar()
    l_cust_no=IntVar()
    l_cust_id.set(row[0][0])
    l_cust_no.set(row[0][2])
    l_cust_name.set(row[0][1])
    Label(f7,text="Cust id:").grid(row=0,column=0)
    Label(f7,textvariable=l_cust_id).grid(row=0,column=1)
    Label(f7,text="Cust Name:").grid(row=1,column=0)
    Label(f7,textvariable=l_cust_name).grid(row=1,column=1)
    Label(f7,text="Cust Number:").grid(row=2,column=0)
    Label(f7,textvariable=l_cust_no).grid(row=2,column=1)
    s.set(str(x[0][0]))
    Label(f7,text="Item Buyed:").grid(row=3,column=0)
    Label(f7,textvariable=s).grid(row=3,column=1)
    Label(f7,text="Ord_id").grid(row=4,column=0)
    Label(f7,text="Product").grid(row=4,column=1)
    Label(f7,text="total_price").grid(row=4,column=2)
    Label(f7,text="Status").grid(row=4,column=3)
    b3=Button(f7,text="Go Back",command=goBack,bd='3px')
    b3.grid(row=7,column=2,columnspan=3)
    Lb2=Listbox(f7,width=10,height=30)
    Lb2.grid(row=5,column=0)
    Lb3=Listbox(f7,width=30,height=30)
    Lb3.grid(row=5,column=1)
    Lb4=Listbox(f7,width=10,height=30)
    Lb4.grid(row=5,column=2)
    Lb5=Listbox(f7,width=10,height=30)
    Lb5.grid(row=5,column=3)
    a=1
    for i in row:
        Lb2.insert(a,i[4])
        Lb3.insert(a,i[5])
        Lb4.insert(a,i[6])
        Lb5.insert(a,i[7])
        a+=1
    cur_sel.set("Select customer")

#Forget password Button click call
def forgetPassword():
    bu.destroy()
    global send,gmail
    def sendMessage():
        receivers=gm.get()
        sender = 'Idher apna email'
        
        message = "Your password is 1234"
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login("idher apna gmail address","idher password daal")
            server.sendmail(sender, receivers, message)
            server.close()
            messagebox.showinfo(":)","Password sent!")
        except:
            messagebox.showinfo(":(","No proper Connection or Email id is incorrect")
            return None
    global y,g
    y=StringVar()
    x.set(1)
    label=Label(f1,textvariable=y,font="Verdana 11")
    y.set("Please Enter your Gmail address, we will send you the password")
    label.grid(row=8,column=1,columnspan=3)
    g=StringVar()
    g.set("Gmail id:")
    gm=StringVar()
    Label(f1,text="").grid(row=9,column=1)
    label2=Label(f1,textvariable=g)
    label2.grid(row=10,column=1,sticky="e")
    gmail=Entry(f1,width=30,textvariable=gm,bd="3px")
    gmail.grid(row=10,column=2,stick="w")
    Label(f1,text="").grid(row=11,column=1)
    send=Button(f1,text="Send",command=sendMessage,bd="3px")
    send.grid(row=12,column=2,stick="w")
    Label(f1,text="").grid(row=13,column=1)

#Top menubar
menubar = Menu(window)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Start",command=Start)
editmenu.add_separator()
editmenu.add_command(label="Exit",command=q)
menubar.add_cascade(label="Start", menu=editmenu)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Customer", command=customer)
filemenu.add_command(label="Order", command=ord)
filemenu.add_command(label="Item", command=item)
filemenu.add_command(label="Payment", command=payment)
menubar.add_cascade(label="Table", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
helpmenu.add_command(label="Licence", command=License)
helpmenu.add_separator()
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_cascade(label="Feedback", command=Feedback)
menubar.add_cascade(label="Logout", command=logout)
window.config(menu=menubar)
#end of menu


###

#Login Page GUI
u=StringVar()
p=StringVar()
username="pramodsj"
password='1234'
x=IntVar()
Label(f1,text="    Admin login    ",font="Times 70 bold").grid(row=0,column=1,columnspan=2)
Label(f1,text="").grid(row=1,column=1)
Label(f1,text="Username:",font="Times 15 bold").grid(row=2,column=1,sticky='e')
e1=Entry(f1,textvariable=u,width=30,bd="4px")
e1.grid(row=2,column=2,sticky='w')
Label(f1,text="").grid(row=3,column=1)
Label(f1,text="Password:",font="Times 15 bold").grid(row=4,column=1,sticky='e')
e2=Entry(f1,show="*",textvariable=p,width=30,bd="3px")
e2.grid(row=4,column=2,sticky='w')
Label(f1,text="").grid(row=5,column=1)
b=Button(f1,text="Login",command=login,width=10,bd="3px",activebackground="lavender").grid(row=6,column=2,sticky='w')
Label(f1,text="").grid(row=7,column=1)
bu=Button(f1,text="Forget\nPassword",command=forgetPassword,width=10,bd="4px")
bu.grid(row=8,column=2,sticky='w')
Label(f1,text="").grid(row=9,column=1)
disable()
f1.pack()
u.set("pramodsj")
p.set("1234")

#end of login page

#Start Page with image
val=IntVar()
canvas=Canvas(fb,height=350,width=1020)
photo=PhotoImage(file="elec.gif")
canvas.create_image(0, 0, image=photo,anchor="nw")
#canvas.create_text(canvas,text="ELECTRONICS SHOP",font="Verdana 40 bold",bg="grey").pack()
#canvas.create_rectangle(190, 0,800, 68,fill="grey");
#canvas.create_text(190,69, text="ELECTRONICS SHOP",anchor=SW, fill="black",font="Verdana 40 bold")
Label(f2,text="").pack()
Label(f2,text="Select the Database:",font="Times 15 bold").pack()
Lb1=Listbox(f2,width=50,height=4,selectmode=SINGLE,bd="3px")
Lb1.insert(END, "Customer")
Lb1.insert(END, "Order")
Lb1.insert(END, "Item")
Lb1.insert(END, "Payment")
Lb1.pack()
Label(f2).pack()
b5=Button(f2,text="Show All Data",bd="3px",command=fetch,font="Times 11 bold")
b5.pack()
Label(f2).pack()
Label(f2,text="View Customer full detail who buyed products using his/her Id:",font="Times 15 bold").pack()
Label(f2,text="").pack()
cursor.execute("select cust_id,cust_name from customer order by cust_id")
content=cursor.fetchall()
i=0
cust_list=[]
while(len(content)>i):
    cust_deat=str(content[i][0])+" : "+content[i][1]
    cust_list.append(cust_deat)
    i+=1
def on_change(value):
    global cur_selection
    cur_selection=cur_sel.get()
global cur_sel
cur_sel=StringVar(value="Select customer")
cust_op = OptionMenu(f2, cur_sel, *(cust_list), command=on_change)
cust_op.pack()
cust_op.configure(width=30)
Label(f2,text="").pack()
f21_b=Button(f2,text="Get Result",bd="4px",command=joins,font="Times 11 bold").pack()
Label(f2,text="").pack()


