from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text='type', src='English', dest='kannada'):
    text1 = text
    src1 = src
    dest1 = dest
    tarns = Translator()
    trans1 = tarns.translate(text1, src=src1, dest=dest1)
    return trans1

def data():
    s = com_sor.get()
    d = com_test.get()
    masg = Sor_text.get(1.0, END)
    textgwt = change(text=masg, src=s, dest=d)
    des_text.delete(1.0, END)
    des_text.insert(END, textgwt)



root = Tk()
root.title("Translator")
root.geometry('600x900')
root.config(bg='Black')

lab_text = Label(root, text='Translator', font=('Time New Roman', 40, 'bold'))
lab_text.place(x=100, y= 40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root, text='Source Text', font=('Time New Roman', 20, 'bold'))
lab_text.place(x=100, y= 110, height=20, width=300)

Sor_text = Text(frame, font=('Time New Roman', 20, 'bold'), wrap=WORD)
Sor_text.place(x=100, y= 140, height=170, width=400)

list_txt = list(LANGUAGES.values())

com_sor = ttk.Combobox(frame, values=list_txt)
com_sor.place(x=40, y= 320, height=40, width=120)
com_sor.set('english')

butn_chang = Button(frame, text='Translaye', relief=RAISED, command=data)
butn_chang.place(x=200, y=320, height=40, width=120)


com_test = ttk.Combobox(frame, values=list_txt)
com_test.place(x=360, y= 320, height=40, width=120)
com_test.set('english')


des_text = Text(frame, font=('Time New Roman', 20, 'bold'), wrap=WORD)
des_text.place(x=100, y= 380, height=170, width=400)


root.mainloop()