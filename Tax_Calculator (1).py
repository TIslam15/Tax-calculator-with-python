from tkinter import *
window = Tk()
window.title("Tax Calculator")
window.geometry('800x500')

given = IntVar()


def selection():
    check_value = given.get()
    if check_value < 300000:
        error_text(1)
    elif clicked.get() == 'Select Here':
        error_text(2)
    else:

        if clicked.get() == 'Freedom Fighter':
            income = check_value - 475000
            calculation(income)
        elif clicked.get() == 'Women':
            income = check_value - 350000
            calculation(income)
        elif clicked.get() == 'Above 65 Years Old':
            income = check_value - 350000
            calculation(income)
        elif clicked.get() == 'Disabled':
            income = check_value - 450000
            calculation(income)
        elif clicked.get() == 'Parents of Disabled':
            income = check_value - 350000
            calculation(income)
        elif clicked.get() == 'Others':
            income = check_value - 300000
            calculation(income)


def calculation(income):
    if 0 < income <= 100000:
        tax = (income * 0.05)
        if tax <= 3000:
            error_text(3)
        else:
            error_text(tax)

    elif 100000 < income <= 400000:
        tax = 5000 + (income - 100000) * 0.1
        if tax <= 3000:
            error_text(3)
        else:
            error_text(tax)

    elif 400000 < income <= 700000:
        tax = 35000 + (income - 400000) * 0.15
        if tax <= 3000:
            error_text(3)
        else:
            error_text(tax)

    elif 700000 < income <= 1600000:
        tax = 95000 + (income - 700000) * 0.2
        if tax <= 3000:
            error_text(3)
        else:
            error_text(tax)
    else:
        tax = 95000 + (income - 1600000) * 0.25
        if tax <= 3000:
            error_text(3)
        else:
            error_text(tax)


def error_text(value):
    if value == 1:
        emptylabel1.config(text='\nERROR!!! Please Enter Valid Annual Income ', fg='red', font=('Arial', 18))
        emptylabel1.pack()
    elif value == 2:
        emptylabel2.config(text='\nERROR!!!  Please Select Your Category. ', fg='red', font=('Arial', 18))
        emptylabel2.pack()

    elif value == 3:
        emptylabel3.config(text='\nPayable Income tax BDT 3000  ', fg='red', font=('Arial', 18))
        emptylabel3.pack()
    else:
        emptylabel.config(text='\n \nYour Payable Income Tax is BDT ' + str(value), fg='black', font=('Arial', 18))
        emptylabel.pack()


l0 = Label(window, text='Welcome to TAX CALCULATOR \n', fg='red', font=('Arial', 18))
l0.pack()
l1 = Label(window, text='Select Your Category', font=('Arial', 18))
l1.pack()
category = [
    "Select Here",
    "Freedom Fighter",
    "Above 65 Years Old",
    "Disabled",
    "Parents of Disabled",
    "Women",
    "Others",
]
clicked = StringVar()
clicked.set(category[0])
menu = OptionMenu(window, clicked, *category)
menu.pack(pady=20)
l2 = Label(window, text='Enter Your Annual Income\n ', font=('Arial', 16))
l2.pack()
textbox1 = Entry(window, textvariable=given)
textbox1.pack()
l3 = Label(window, text='\n ', font=('Arial', 16))
l3.pack()
calculator = Button(window, command=selection, text="Calculate Income Tax", bg='blue', fg='white', font=('Arial', 16))
calculator.pack()
emptylabel = Label(window)
emptylabel1 = Label(window)
emptylabel2 = Label(window)
emptylabel3 = Label(window)
window.mainloop()
