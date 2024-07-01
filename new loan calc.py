from tkinter import *

def calculate_emi():
    info1=float(e1.get())
    info2=float(e2.get())
    info3=int(e3.get())
    roi=(info2/1200)  #roi in month
    no_of_month=info3*12 
    emi=(info1*roi*((1+roi)**no_of_month))/(((1+roi)**no_of_month)-1)
    l5.config(text=emi)

    interest_component=(emi*no_of_month)-info1
    l7.config(text=interest_component)

    total_amount_paid=info1+interest_component
    l9.config(text=total_amount_paid)

    no_of_emi=int(total_amount_paid/no_of_month)
    l11.config(text=no_of_emi)
        
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

b1=Button(root, text="Calculate EMI", command=calculate_emi)
b1.pack()

l4=Label(root, text= "Monthly EMI")
l4.pack()

l5=Label(root, text= "")
l5.pack()
l6=Label(root, text= "Total interest to be paid")
l6.pack()
l7=Label(root, text= "")
l7.pack()
l8=Label(root, text= "Total amount to be paid")
l8.pack()
l9=Label(root, text= "")
l9.pack()

l10=Label(root, text="Number of emi")
l10.pack()


l11=Label(root,text="")
l11.pack()


root.mainloop()