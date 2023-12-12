from tkinter import *
import random

root=Tk()
root.geometry("750x300")
root.title("password generator")
  
label1=Label(root,text=" PASSWORD GENERATOR ",font="Helvetica 20 bold",background="skyblue",justify=LEFT).grid(row=0,column=1)
name_label=Label(root,text="Enter Your Name: ",font="Helvetica 13 bold").grid(row=1,column=0)
len_label=Label(root,text="Enter The Length Of Password: ",font="Helvetica 13 bold").grid(row=3,column=0)
ans_label=Label(root,text="Generated Password Is: ",font="Helvetica 13 bold").grid(row=6,column=0)

          
len_value=IntVar()
len_value.set(" ")
name_value=StringVar()
name_entry=Entry(root,textvariable=name_value,font="Helvetica 13 bold").grid(row=1,column=1)
len_entry=Entry(root,textvariable=len_value,font="Helvetica 13 bold").grid(row=3,column=1)
   
def operation():
    global password
    small="abcdefghijklmnopqrstuvwxyz"
    big="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters="!@#$%&_*.:"
    digits="0123456789"
    number=small+big+characters+digits

    password="".join(random.sample(number,len_value.get()))
    print(f"The Generated Password Is : {password}")
    gen_label=Label(root,text=password,font="Helvetica 13 bold").grid(row=6,column=1)
           
def reset():
    global password
    print("hello")
    len_value.set(" ")
    name_value.set(" ") 
    gen_label=Label(root,text="                                                                                       ").grid(row=6,column=1)
           
button=Button(root,text="GENERATE PASSWORD",command=operation,font="Helvetica 13 bold").grid(row=4,column=1)
rest_button=Button(root,text="RESET",command=reset,font="Helvetica 13 bold").grid(row=7,column=1)

root.mainloop()

