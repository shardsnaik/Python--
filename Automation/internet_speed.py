from tkinter import *
import speedtest
sp = Tk()

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downld = str(round(sp.download()/(10**6), 3)) + "  Mbps"
    upld = str(round(sp.upload()/(10**6), 3)) + "  Mbps"
    lab_dwn.config(text=downld)
    lab_upld.config(text=upld)


sp.title(" Internet Speed Tester")
sp.geometry('500x400')
sp.config(bg='green')

lab= Label(sp, text='Internet speed test', font=('Time New Roman' ,20, 'bold'), bg='green')
lab.place(x=40, y=40, height=50, width=380)

# Downlaod speed and data 
lab= Label(sp, text='Download speed', font=('Time New Roman' ,20, 'bold'), bg='green')
lab.place(x=80, y=110,height=50, width=380)

lab_dwn= Label(sp, text='00', font=('Time New Roman' ,20, 'bold'), bg='green')
lab_dwn.place(x=40, y=170,height=50, width=380)


# Upload Speed and data
lab= Label(sp, text='Uplaod speed', font=('Time New Roman' ,20, 'bold'), bg='green')
lab.place(x=40, y=240,height=50, width=380)

lab_upld= Label(sp, text='00', font=('Time New Roman' ,20, 'bold'), bg='green')
lab_upld.place(x=40, y=300, height=50, width=380)


button = Button(sp, text = 'Check Speed', font=('Time New Roman' ,20, 'bold'), relief=RAISED, bg='Red', command=speedcheck)
button.place(x=40, y=350, height=50, width=390)



sp.mainloop() 
