from tkinter import *

# Makes tkinter equal to window so you can just write window instead of Tk.
window = Tk()
# Makes the title of the window Calculator.
window.title("Calculator")
# Makes the window have a minsize so it can not go smaller.
window.minsize(width=380, height=555)
# Makes the window have a maxsize so it can not go bigger.
window.maxsize(width=380, height=555)
# Makes the equation equal a string variable.
equation = StringVar()
# Makes screen equal to entry that has window and a parameter that equals equation in it
screen = Entry(window, textvariable=equation)
# Makes the screen into a grid format.
screen.grid(columnspan=4, ipadx=95)
# Goes in the method for window then goes into a parameter to make the background light blue.
window.configure(background="light blue")

# Makes it that the expression is equal to empty/nothing so nothing appears 
# in the calculator when it is opened.
expression = ""
 
# Makes it so the expression gets turned into a expression with a 
# a any parameter thats been turned into a string and 
# then make the equation set to the expression.
def click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
# Makes the total equal the a evaluated expression thats been 
# turned into a string and makes it so the equation is set to total 
# that is the expression.
def equal():
    global expression
    total = str(eval(expression))
    equation.set(total)

# Makes the expression equal empty/nothing and then it sets the 
# equation to the expression that is empty.
def clear():
    global expression
    expression = ""
    equation.set("")

# Makes the expression equal to a floated expression then 
# makes inches equal a rounded floated expression thats divided by 2.54 
# then makes the equation set to that expression
def in_to_cm():
    global expression
    expression = float(expression)
    inches = round(float(expression / 2.54))
    equation.set(inches)

# Makes the expression equal to a floated expression then 
# makes centermeters equal a rounded floated expression thats multipled by 2.54 
# then makes the equation set to that expression
def cm_to_in():
    global expression
    expression = float(expression)
    centermeters = round(float(expression * 2.54))
    equation.set(centermeters)

# Button for clear the uses (command=clear) to use the def clear
button_c = Button(text="C", height=4, width=4, command=clear, font=("Arial", 17, "bold"))
button_c.place(x=0, y=60)

# Button for clear the uses (command=cm_to_in) to use the def cm_to_in
button_in = Button(text="In", height=4, width=4, command=cm_to_in, font=("Arial", 17, "bold"))
button_in.place(x=100, y=60)

# Button for clear the uses (command=in_to_cm) to use the def in_to_cm
button_cm = Button(text="Cm", height=4, width=4, command=in_to_cm, font=("Arial", 17, "bold"))
button_cm.place(x=200, y=60)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka +
button_plus = Button(text="+", height=4, width=4, command=lambda: click("+"), font=("Arial", 17, "bold"))
button_plus.place(x=300, y=60)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 7
button_7 = Button(text="7", height=4, width=4, command=lambda: click(7), font=("Arial", 17, "bold"))
button_7.place(x=0, y=160)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 8
button_8 = Button(text="8", height=4, width=4, command=lambda: click(8), font=("Arial", 17, "bold"))
button_8.place(x=100, y=160)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 9
button_9 = Button(text="9", height=4, width=4, command=lambda: click(9), font=("Arial", 17, "bold"))
button_9.place(x=200, y=160)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka -
button_minus = Button(text="-", height=4, width=4, command=lambda: click("-"), font=("Arial", 17, "bold"))
button_minus.place(x=300, y=160)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 4
button_4 = Button(text="4", height=4, width=4, command=lambda: click(4), font=("Arial", 17, "bold"))
button_4.place(x=0, y=260)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 5
button_5 = Button(text="5", height=4, width=4, command=lambda: click(5), font=("Arial", 17, "bold"))
button_5.place(x=100, y=260)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 6
button_6 = Button(text="6", height=4, width=4, command=lambda: click(6), font=("Arial", 17, "bold"))
button_6.place(x=200, y=260)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka *
button_times = Button(text="*", height=4, width=4, command=lambda: click("*"), font=("Arial", 17, "bold"))
button_times.place(x=300, y=260)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 1
button_1 = Button(text="1", height=4, width=4, command=lambda: click(1), font=("Arial", 17, "bold"))
button_1.place(x=0, y=360)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 2
button_2 = Button(text="2", height=4, width=4, command=lambda: click(2), font=("Arial", 17, "bold"))
button_2.place(x=100, y=360)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 3
button_3 = Button(text="3", height=4, width=4, command=lambda: click(3), font=("Arial", 17, "bold"))
button_3.place(x=200, y=360)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka /
button_divided = Button(text="/", height=4, width=4, command=lambda: click("/"), font=("Arial", 17, "bold"))
button_divided.place(x=300, y=360)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka 0
button_0 = Button(text="0", height=4, width=4, command=lambda: click(0), font=("Arial", 17, "bold"))
button_0.place(x=0, y=460)

# Button that uses (command=lambda) that can evaluate and returns only one expression aka .
button_dot = Button(text=".", height=4, width=4, command=lambda: click("."), font=("Arial", 17, "bold"))
button_dot.place(x=100, y=460)

# Button for clear the uses (command=equal) to use the def equal
button_equals = Button(text="=", height=4, width=14, command=equal, font=("Arial", 17, "bold"))
button_equals.place(x=200, y=460)

window.mainloop()