from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("400x400")
window.configure(background="powder blue")
c=1

def show(b):
    l4.configure(text='')

    global c
    c+=1
    if(c%2==0):
        l5 = Label(window, text='Player 2 Turn : ', font=('arial', 10, 'bold'), fg='blue', bg='powder blue')
        l5.place(x=50, y=290)
        if(b["text"]==''):
            b["text"]='X'

    else:
        l5 = Label(window, text='Player 1 Turn : ', font=('arial', 10, 'bold'), fg='blue', bg='powder blue')
        l5.place(x=50, y=290)
        if(b["text"]==''):
            b["text"]='0'


    if(b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X' or b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X' or b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X' or b1["text"]=='X' and b5["text"]=='X' and b9["text"]=='X' or b3["text"]=='X' and b5["text"]=='X' and b7["text"]=='X' or b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X' or b2["text"]=='X' and b5["text"]=='X' and b8["text"]=='X' or b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X'):

        l4.configure(text='Player 1 is winner')

        messagebox.showinfo('Alert','Player 1 is winner')
        rr = messagebox.askretrycancel('Alert', 'For play again hit Retry button')
        l4.configure(text='')


        if(rr==True):
            b1.configure(text='')
            b2.configure(text='')
            b3.configure(text='')
            b4.configure(text='')
            b5.configure(text='')
            b6.configure(text='')
            b7.configure(text='')
            b8.configure(text='')
            b9.configure(text='')

    elif(b1["text"]=='0' and b2["text"]=='0' and b3["text"]=='0' or b4["text"]=='0' and b5["text"]=='0' and b6["text"]=='0' or b7["text"]=='0' and b8["text"]=='0' and b9["text"]=='0' or b1["text"]=='0' and b5["text"]=='0' and b9["text"]=='0' or b3["text"]=='0' and b5["text"]=='0' and b7["text"]=='0' or b1["text"]=='0' and b4["text"]=='0' and b7["text"]=='0' or b2["text"]=='0' and b5["text"]=='0' and b8["text"]=='0' or b3["text"]=='0' and b6["text"]=='0' and b9["text"]=='0'):

        l4.configure(text='Player 2 is winner')

        messagebox.showinfo('Alert', 'Player 2 is winner')
        rr = messagebox.askretrycancel('Alert', 'For play again hit Retry button')
        l4.configure(text='')


        if (rr == True):
            b1.configure(text='')
            b2.configure(text='')
            b3.configure(text='')
            b4.configure(text='')
            b5.configure(text='')
            b6.configure(text='')
            b7.configure(text='')
            b8.configure(text='')
            b9.configure(text='')
            l5.configure(text='Player 1 Turn :')


#***************************************************player turn*****************************************

l1=Label(window,text=" TICK CROSS GAME ",font=('arial',20,'bold'),bg="powder blue",fg="white")
l1.place(x=50,y=10)
l2=Label(window,text="Player 1 [X]",font=('arial',10,'bold'),bg="powder blue")
l2.place(x=45,y=45)
l3=Label(window,text="Player 2 [0]",font=('arial',10,'bold'),bg="powder blue")
l3.place(x=45,y=70)

#***********************************************************button***********************************
b1=Button(window,text='',height=3,width=5,command=lambda:show(b1))
b1.place(x=45,y=100)
b2=Button(window,text='',height=3,width=5,command=lambda:show(b2))
b2.place(x=95,y=100)
b3=Button(window,text='',height=3,width=5,command=lambda:show(b3))
b3.place(x=145,y=100)
b4=Button(window,text='',height=3,width=5,command=lambda:show(b4))
b4.place(x=45,y=160)
b5=Button(window,text='',height=3,width=5,command=lambda:show(b5))
b5.place(x=95,y=160)
b6=Button(window,text='',height=3,width=5,command=lambda:show(b6))
b6.place(x=145,y=160)
b7=Button(window,text='',height=3,width=5,command=lambda:show(b7))
b7.place(x=45,y=220)
b8=Button(window,text='',height=3,width=5,command=lambda:show(b8))
b8.place(x=95,y=220)
b9=Button(window,text='',height=3,width=5,command=lambda:show(b9))
b9.place(x=145,y=220)

l4=Label(window,text='START GAME',font=('arial',15,'bold'),fg='blue',bg='powder blue')
l4.place(x=50,y=320)
l5=Label(window,text='Player 1 Turn : ',font=('arial',10,'bold'),fg='blue',bg='powder blue')
l5.place(x=50,y=290)

window.mainloop()
