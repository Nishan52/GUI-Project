from tkinter import *
from tkinter import messagebox as msgBox
import datetime
import re
from tkinter import filedialog
from stegano import lsb







#creating window
from tkinter.ttk import Notebook

from stegano.exifHeader import exifHeader

root=Tk()
#edit window
root.title("En-Deccryption")
root.geometry("500x500")
root.resizable(0,0)
root.config(background="grey")
root.iconbitmap("icon_icm_2.ico")


notebook=Notebook(root)
#creating tab
tab1=Frame(notebook)
tab2=Frame(notebook)
#adding tabs
notebook.add(tab1,text="Encryption")
notebook.add(tab2,text="Decryption")
notebook.pack(fill="both",expand="yes")

def SelectImage(path):
    filename=filedialog.askopenfilename()
    if re.search('\.jpg$', filename) or re.search('\.png$', filename):

        path.set(filename)

    else:
        msgBox.showinfo("Invalid Format","Select .jpg or .png Format")

def SaveAs(path):
    message_time = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    new_name='Secret_pic'+message_time+'.jpg'
    return new_name

def Save(messageRead,SaveAs):
    x=message1.get()
    y=SaveAs
    exifHeader.hide(path.get(), y, secret_message=x)
    msgBox.showinfo("saved", "image has been saved with name " + y)
    path.set("")
    messageRead.set("")

def close():
    root.destroy()


#creating button for selecting image in encryption tab

path=StringVar()
but1=Button(tab1,text=' Select Image', font=("Varanda",20),background='blue',command=lambda :SelectImage(path))
but1.place(relx=0.32,rely=0.15,height=40,width=195)

label1=Label(tab1,text="Your image path here:",font=("",15))
label1.place(relx=0.25,rely=0.25,height=40,width=250)

# creating text box to enter your mewssage
message= Entry(tab1, font=("varanda", 10), textvariable=path, bg='powder blue', justify='center', width=13)
message.place(relx=0.17,rely=0.33,height=40,width=300)


label1=Label(tab1,text="Your message here:",font=("",15))
label1.place(relx=0.25,rely=0.42,height=40,width=250)

messageRead=StringVar()
message1= Entry(tab1, font=("varanda", 20), textvariable=messageRead, bg='powder blue', justify='center', width=13)
message1.place(relx=0.17,rely=0.51,height=40,width=300)


but2=Button(tab1,text='Save As', font=("Varanda",20),command=lambda :SaveAs(path))
but2.place(relx=0.17,rely=0.62,height=40,width=120)

but3=Button(tab1,text='Encrypt', font=("Varanda",20),command=lambda :Save(messageRead,SaveAs(path)))
but3.place(relx=0.5,rely=0.62,height=40,width=120)



but3=Button(tab1,text='Exit', font=("Varanda",20),background='red',command=lambda:close())
but3.place(relx=0.34,rely=0.82,height=30,width=120)

#creating button for saving an encrypted image

#now working on decryption tab



def unbox(path):
    hiddentext=exifHeader.reveal(path.get())
    msgBox.showinfo("Unboxing", "Messasge  " + hiddentext.decode('UTF-8'))



but4=Button(tab2,text='select Image', font=("Varanda",20),background='brown',command=lambda :SelectImage(path1))
but4.place(relx=0.27,rely=0.1,height=40,width=200)

label3=Label(tab2,text='Your Image address:',font=("",14))
label3.place(relx=0.17,rely=0.25,height=35,width=290)

path1=StringVar()

message3= Entry(tab2, font=("varanda", 10), textvariable=path1, bg='powder blue', justify='center', width=13)
message3.place(relx=0.17,rely=0.33,height=40,width=300)



#creating button for saving an encrypted image
but5=Button(tab2,text='Decrypt', font=("Varanda",20),background='green',command=lambda: unbox(path1))
but5.place(relx=0.27,rely=0.5,height=40,width=200)

but6=Button(tab2,text='Exit', font=("Varanda",20),background='red',command=lambda:close())
but6.place(relx=0.34,rely=0.82,height=30,width=120)


mainloop()