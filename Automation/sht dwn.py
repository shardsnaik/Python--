from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 39')
def logout():
    os.system('shutdown -1')
def shutdown():
    os.system('shutdown /s /t 1')

st = Tk()
st.title('ShutDown App ')
st.geometry('500x500')
st.config(bg='gray')

rst_button = Button(st, text='Restart', font=('Time New Roman',20,'bold'), relief=RAISED,cursor='plus', command=restart)
rst_button.place(x=150,y=50,height=60, width=200)

rst_button = Button(st, text='Restart Time', font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus', command=restart_time)
rst_button.place(x=150,y=120,height=60, width=200)

lg_button = Button(st, text='Log-Out', font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus', command=logout)
lg_button.place(x=150,y=200,height=60, width=200)

lg_button = Button(st, text='ShutDown', font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus', command=shutdown)
lg_button.place(x=150,y=270,height=60, width=200)

st.mainloop()