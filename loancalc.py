from tkinter import *

def calculate_loan():
    info1=float(e1.get())
    info2=float(e2.get())
    info3=float(e3.get())
    roi=(info2/1200)  #roi in month
    no_of_month=info3*12 

    emi=(info1*roi*((1+roi)**no_of_month))/(((1+roi)**no_of_month)-1)
    l4.config(text=emi)
    

root=Tk()
root.title("Loan Calculator")
root.minsize(width=400,height=400)
root.geometry("500x500")

l1=Label(root,text="Enter principal amount ")
l1.pack()
e1=Entry(root, text="")
e1.pack()

l2=Label(root, text="Enter annual rate of interest(%)")
l2.pack()
e2=Entry(root, text="")
e2.pack()

l3=Label(root, text="Enter number of years ")
l3.pack()
e3=Entry(root, text="")
e3.pack()

b1=Button(root, text="Calculate EMI", command=calculate_loan)
b1.pack()

l4=Label(root, text= "")
l4.pack()

root.mainloop()