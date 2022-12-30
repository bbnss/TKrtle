import tkinter
import turtle
import tkinter.messagebox
import time

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 600)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=11, columnspan=11)
draw = turtle.RawTurtle(canvas)
draw.shape("turtle")


def uno():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.left(90)
    draw.fd(200)
    draw.left(135)
    draw.fd(80)

def due():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.left(180)
    draw.fd(80)
    draw.right(135)
    draw.fd(100)
    draw.circle(40, 220)

def tre():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.circle(50, 180)
    draw.right(180)
    draw.circle(50,180)

def quattro():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.left(180)
    draw.fd(100)
    draw.right(135)
    draw.fd(100)
    draw.right(135)
    draw.fd(130)

def cinque():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.circle(50, 180)
    draw.right(90)
    draw.fd(50)
    draw.right(90)
    draw.fd(40)

def sei():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.circle(50)
    draw.right(180)
    draw.circle(-90, 150)

def sette():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.left(80)
    draw.fd(140)
    draw.left(100)
    draw.fd(70)

def otto():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.circle(50, 180)
    draw.circle(50, 180)
    draw.circle(-50, 180)
    draw.circle(-50, 180)
    
def nove():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.left(65)
    draw.fd(120)
    draw.circle(50)

def zero():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(30)
    draw.circle(90)    
    
    
def fiore():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.goto(0, 0)
    draw.reset()
    draw.color('red', 'yellow')
    draw.begin_fill()
    for x in range(0,36):
        draw.forward(200)
        draw.left(170)
    
    draw.end_fill()
    draw.penup()
    draw.fd(130)
    draw.pendown()
    draw.pensize(30)
    draw.color("green")
    draw.circle(-150, 180)

def sole():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.penup()
    draw.goto(0, -100)
    draw.pendown()
    draw.color("yellow")
    draw.begin_fill()
    draw.circle(100)
    draw.end_fill()
    draw.ht()
    
    for i in range(36):
        draw.penup()
        draw.goto(0, 0)
        draw.setheading(i * 10)
        draw.forward(100)
        draw.pendown()
        draw.forward(50)

def casa():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(20)
    draw.begin_fill()
    draw.color("brown")
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)

    draw.end_fill()
    
    draw.begin_fill()
    draw.color("black")
    draw.left(45)
    draw.forward(70)
    draw.right(90)
    draw.forward(70)
    draw.right(135)
    draw.forward(100)
    draw.right(90)
    draw.end_fill()
    draw.ht()

def stella():
    draw.penup()
    draw.goto(0, 0)
    draw.reset()
    draw.pendown()
    draw.pensize(20)
    draw.begin_fill()
    draw.color("yellow")
    for i in range(0, 5):
        draw.fd(200)
        draw.right(144)
    draw.end_fill()
    
    

        


    

def Button_click ():
    #tkinter.messagebox.showinfo("Bene!", " Iniziamo!!")
    uno()
    time.sleep(0.5)
    due()
    time.sleep(0.5)
    tre()
    time.sleep(0.5)
    quattro()
    time.sleep(0.5)
    cinque()
    time.sleep(0.5)
    sei()
    time.sleep(0.5)
    sette()
    time.sleep(0.5)
    otto()
    time.sleep(0.5)
    nove()
    time.sleep(0.5)
    zero()
    time.sleep(0.5)
    
def Button_click2 ():
    #tkinter.messagebox.showinfo("Bene!", " Iniziamo!! ")
    fiore()
    time.sleep(1)
    sole()
    time.sleep(1)
    casa()
    time.sleep(1)
    stella()
    time.sleep(1)


#Tasti Numeri
    
Play_Button = tkinter.Button(master = window, text ="Play! NUMERI", command = Button_click)
Play_Button.config(bg="red",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Play_Button = tkinter.Button(master = window, text ="Play! DISEGNI", command = Button_click2)
Play_Button.config(bg="blue",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=12, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Disegna il numero Uno", command = uno)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

Board_Button2 = tkinter.Button(master = window, text ="Disegna il numero Due", command = due)
Board_Button2.config(bg="cyan",fg="black")
Board_Button2.grid(padx=2, pady=2, row=2, column=11, sticky='nsew')

Board_Button3 = tkinter.Button(master = window, text ="Disegna il numero Tre", command = tre)
Board_Button3.config(bg="cyan",fg="black")
Board_Button3.grid(padx=2, pady=2, row=3, column=11, sticky='nsew')

Board_Button4 = tkinter.Button(master = window, text ="Disegna il numero Quattro", command = quattro)
Board_Button4.config(bg="cyan",fg="black")
Board_Button4.grid(padx=2, pady=2, row=4, column=11, sticky='nsew')

Board_Button5 = tkinter.Button(master = window, text ="Disegna il numero Cinque", command = cinque)
Board_Button5.config(bg="cyan",fg="black")
Board_Button5.grid(padx=2, pady=2, row=5, column=11, sticky='nsew')

Board_Button6 = tkinter.Button(master = window, text ="Disegna il numero Sei", command = sei)
Board_Button6.config(bg="cyan",fg="black")
Board_Button6.grid(padx=2, pady=2, row=6, column=11, sticky='nsew')

Board_Button7 = tkinter.Button(master = window, text ="Disegna il numero Sette", command = sette)
Board_Button7.config(bg="cyan",fg="black")
Board_Button7.grid(padx=2, pady=2, row=7, column=11, sticky='nsew')

Board_Button8 = tkinter.Button(master = window, text ="Disegna il numero Otto", command = otto)
Board_Button8.config(bg="cyan",fg="black")
Board_Button8.grid(padx=2, pady=2, row=8, column=11, sticky='nsew')

Board_Button9 = tkinter.Button(master = window, text ="Disegna il numero Nove", command = nove)
Board_Button9.config(bg="cyan",fg="black")
Board_Button9.grid(padx=2, pady=2, row=9, column=11, sticky='nsew')

Board_Button0 = tkinter.Button(master = window, text ="Disegna il numero Zero", command = zero)
Board_Button0.config(bg="cyan",fg="black")
Board_Button0.grid(padx=2, pady=2, row=10, column=11, sticky='nsew')

#Tasti Disegni

Board_Button11 = tkinter.Button(master = window, text ="Disegna un Fiore", command = fiore)
Board_Button11.config(bg="cyan",fg="black")
Board_Button11.grid(padx=2, pady=2, row=1, column=12, sticky='nsew')

Board_Button12 = tkinter.Button(master = window, text ="Disegna il Sole", command = sole)
Board_Button12.config(bg="cyan",fg="black")
Board_Button12.grid(padx=2, pady=2, row=2, column=12, sticky='nsew')

Board_Button13 = tkinter.Button(master = window, text ="Disegna una Casa", command = casa)
Board_Button13.config(bg="cyan",fg="black")
Board_Button13.grid(padx=2, pady=2, row=3, column=12, sticky='nsew')

Board_Button14 = tkinter.Button(master = window, text ="Disegna una Stella", command = stella)
Board_Button14.config(bg="cyan",fg="black")
Board_Button14.grid(padx=2, pady=2, row=4, column=12, sticky='nsew')


window.mainloop()
