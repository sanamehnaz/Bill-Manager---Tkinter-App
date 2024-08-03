from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Bill Management App")
root.resizable(False, False)

def Reset():
    entry_idly.delete(0,END)
    entry_vada.delete(0,END)
    entry_dosa.delete(0,END)
    entry_puri.delete(0,END)
    entry_pongal.delete(0,END)
    entry_upma.delete(0,END)
    entry_ragiAmbali.delete(0,END)

def Total():
    try:a1=int(idly.get())
    except:a1=0

    try:a2=int(vada.get())
    except:a2=0

    try:a3=int(dosa.get())
    except:a3=0

    try:a4=int(puri.get())
    except:a4=0

    try:a5=int(pongal.get())
    except:a5=0

    try:a6=int(upma.get())
    except:a6=0

    try:a7=int(ragiAmbali.get())
    except:a7=0
    c1 = 20*a1
    c2 = 10*a2
    c3 = 20*a3
    c4 = 30*a4
    c5 = 25*a5
    c6 = 20*a6
    c7 = 20*a7

    lbl_total = Label(f2,font=("garamond",20,"bold"),text="Total", width=16,fg="lightyellow", bg="black")
    lbl_total.place(x=0,y=50)

    entry_total = Entry(f2,font=("garamond",20,"bold"),textvariable=total_bill,bd=6,width=15,bg="lightblue")
    entry_total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.",str("%.2f" %totalcost)
    total_bill.set(string_bill)
    

Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("garamond", 33), width="300", height="2").pack()
frame = Frame(root, bg="lightpink", highlightbackground="black", highlightthickness=1, width=300, height=370)
frame.place(x=10, y=118)
Label(frame,text="MENU", font=("garamond",40,"bold"), fg="black", bg="lightpink").place(x=50,y=0)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Idly......Rs.20/-", fg="black", bg="lightpink").place(x=10,y=80)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Vada......Rs.10/-", fg="black", bg="lightpink").place(x=10,y=110)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Dosa......Rs.20/-", fg="black", bg="lightpink").place(x=10,y=140)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Puri......Rs.30/-", fg="black", bg="lightpink").place(x=10,y=170)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Pongal......Rs.25/-", fg="black", bg="lightpink").place(x=10,y=200)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Upma......Rs.20/-", fg="black", bg="lightpink").place(x=10,y=230)
Label(frame,font=("Aquarium Font", 15, "bold"), text="Ragi Ambali......Rs.20/-", fg="black", bg="lightpink").place(x=10,y=260)

f2 = Frame(root, bg="lightyellow",highlightbackground="black",highlightthickness="1", width=300,height=370)
f2.place(x=690,y=118)

bill = Label(f2, text="Total Amount To Pay", font=("garamond",20,"bold"),bg="lightyellow")
bill.place(x=9,y=9)

f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()
idly = StringVar()
vada = StringVar()
dosa = StringVar()
puri = StringVar()
pongal = StringVar()
upma = StringVar()
ragiAmbali = StringVar()
total_bill =StringVar()

lbl_idly = Label(f1, font=("garamond",20,"bold"),text="Idly", width=12, fg="black")
lbl_vada = Label(f1, font=("garamond",20,"bold"),text="Vada", width=12, fg="black")
lbl_dosa = Label(f1, font=("garamond",20,"bold"),text="Dosa", width=12, fg="black")
lbl_puri = Label(f1, font=("garamond",20,"bold"),text="Puri", width=12, fg="black")
lbl_pongal = Label(f1, font=("garamond",20,"bold"),text="Pongal", width=12, fg="black")
lbl_upma = Label(f1, font=("garamond",20,"bold"),text="Upma", width=12, fg="black")
lbl_ragiAmbali = Label(f1, font=("garamond",20,"bold"),text="Ragi Ambali", width=12, fg="black")
lbl_idly.grid(row=1, column=0)
lbl_vada.grid(row=2, column=0)
lbl_dosa.grid(row=3, column=0)
lbl_puri.grid(row=4, column=0)
lbl_pongal.grid(row=5, column=0)
lbl_upma.grid(row=6, column=0)
lbl_ragiAmbali.grid(row=7, column=0)

entry_idly = Entry(f1,font=("garamond", 20, "bold"), textvariable=idly, bd=6, width=8, bg="lightpink")
entry_vada = Entry(f1,font=("garamond", 20, "bold"), textvariable=vada, bd=6, width=8, bg="lightpink")
entry_dosa = Entry(f1,font=("garamond", 20, "bold"), textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_puri = Entry(f1,font=("garamond", 20, "bold"), textvariable=puri, bd=6, width=8, bg="lightpink")
entry_pongal = Entry(f1,font=("garamond", 20, "bold"), textvariable=pongal, bd=6, width=8, bg="lightpink")
entry_upma = Entry(f1,font=("garamond", 20, "bold"), textvariable=upma, bd=6, width=8, bg="lightpink")
entry_ragiAmbali = Entry(f1,font=("garamond", 20, "bold"), textvariable=ragiAmbali, bd=6, width=8, bg="lightpink")
entry_idly.grid(row=1, column=1)
entry_vada.grid(row=2, column=1)
entry_dosa.grid(row=3, column=1)
entry_puri.grid(row=4, column=1)
entry_pongal.grid(row=5, column=1)
entry_upma.grid(row=6, column=1)
entry_ragiAmbali.grid(row=7, column=1)

btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("garamond",16,"bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8,column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue",font=("garamond",16,"bold"), width=10,text="Total", command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()