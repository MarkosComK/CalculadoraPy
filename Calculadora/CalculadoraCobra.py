from tkinter import *

root = Tk()
root.geometry('480x746')
root.resizable(False, False)
root.title('Calculadora Cobra')

espressao = ''

def press(num):
    global espressao
    espressao = espressao + str(num)
    equacao.set(espressao)


def resultado():
    global espressao
    result = str(eval(espressao))
    equacao.set(result)


def limpar():
    global espressao
    espressao = ''
    equacao.set('')


equacao = StringVar()

#class Calculadora:
#telaFrame = Frame(root, height=140, width=480, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
#telaFrame.place(x=0, y=0)
telaInput = Entry(root, font = ('arial', 100, 'normal'), textvariable=equacao, width=7, bg="black", bd=0, justify=LEFT, fg='white')
telaInput.place(x=0, y=0)
#def __init__(self, master=None):
b1 = Button(text='7', bg='white')
b1.img = PhotoImage()
b1.config(height=145, width=120, image=b1.img, compound=CENTER, command=lambda: press(7))
b1.place(x=0, y=140)
b2 = Button(text='8', bg='white')
b2.config(height=145, width=120, image=b1.img, compound=CENTER, command=lambda: press(8))
b2.place(x=120, y=140)
b3 = Button(text='9', bg='white')
b3.config(height=145, width=120, image=b1.img, compound=CENTER, command=lambda: press(9))
b3.place(x=240, y=140)
b4 = Button(text='X', bg='white')
b4.config(height=145, width=120, image=b1.img, compound=CENTER, command=lambda: press('*'))
b4.place(x=360, y=140)
b5 = Button(text='4', bg='white')
b5.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(4))
b5.place(x=0, y=291)
b5 = Button(text='5', bg='white')
b5.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(5))
b5.place(x=120, y=291)
b6 = Button(text='6', bg='white')
b6.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(6))
b6.place(x=240, y=291)
b7 = Button(text='÷', bg='white')
b7.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press('/'))
b7.place(x=360, y=291)
b8 = Button(text='1', bg='white')
b8.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(1))
b8.place(x=0, y=442)
b9 = Button(text='2', bg='white')
b9.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(2))
b9.place(x=120, y=442)
b10 = Button(text='3', bg='white')
b10.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(3))
b10.place(x=240, y=442)
b11 = Button(text='-', bg='white')
b11.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press('-'))
b11.place(x=360, y=442)
b12 = Button(text='CE', bg='white')
b12.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: limpar())
b12.place(x=0, y=593)
b13 = Button(text='0', bg='white')
b13.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press(0))
b13.place(x=120, y=593)
b14 = Button(text='=', bg='white')
b14.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: resultado())
b14.place(x=240, y=593)
b15 = Button(text='+', bg='white')
b15.config(height=145, width=114, image=b1.img, compound=CENTER, command=lambda: press('+'))
b15.place(x=360, y=593)

#Calculadora(root)
root.mainloop()