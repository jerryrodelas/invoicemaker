from tkinter import*
import tkinter.messagebox
import random
import time
import datetime
HEIGHT = 300
WIDTH = 800

root = Tk()



Tops = Frame(root, height = HEIGHT, width = WIDTH,bg='black')
Tops.pack()

f1 = Frame(root,bg='black',bd=5)
f1.pack()

root.title("Generate Quotation")
root.config(background='black')


#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Verdana',20,'bold'),text="Sedgcom Pty Ltd",fg="yellow",bg="black")
lblInfo.grid(row=0,column=1)

lblInfo=Label(Tops,font=('Verdana',10,'bold'),text=localtime,fg="#43e80c",bd=10,bg="black")
lblInfo.grid(row=0,column=2)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    try:
       if (Cable.get()==""):
           CoCable=0
       else:
           CoCable=float(Cable.get())

       if (Conduit.get()==""):
           CoConduit=0
       else:
           CoConduit=float(Conduit.get())

       if (Camera.get()==""):
          CoCamera=0
       else:
           CoCamera=float(Camera.get())

       if (DVR_NVR.get()==""):
          CoDVR_NVR=0
       else:
           CoDVR_NVR=float(DVR_NVR.get())

       if (Connectors.get()==""):
           CoConnectors=0
       else:
           CoConnectors=float(Connectors.get())

       if (Labour_hours.get()==""):
           CoD=0
       else:
           CoD=float(Labour_hours.get())

                   
       CostofCable =CoCable * 1.50
       CostofLabour_hours=CoD * 60
       CostofConduit = CoConduit* 20
       CostofCamera = CoCamera * 180
       CostDVR_NVR = CoDVR_NVR* 380
       CostConnectors=CoConnectors * 2.50

       CostofInstall= "AUD", str('%.2f' % (CostofCable+CostofLabour_hours+CostofConduit+CostofCamera+CostDVR_NVR+CostConnectors))

       PayTax=((CostofCable+CostofLabour_hours+CostofConduit+CostofCamera+CostDVR_NVR+CostConnectors) * 0.1)

       InstallCost=(CostofCable+CostofLabour_hours+CostofConduit+CostofCamera+CostDVR_NVR+CostConnectors)
 
       MaterialCost= ((CostofCable+CostofConduit+CostofCamera+CostDVR_NVR+CostConnectors))

       Service = "AUD", str ('%.2f' % MaterialCost)

       OverAllCost ="AUD", str ('%.2f' % (PayTax+InstallCost))

       PaidTax= "AUD", str ('%.2f' % PayTax)

       Service_Charge.set(Service)
       Cost.set(CostofInstall)
       Tax.set(PaidTax)
       Total.set(OverAllCost)

    except:
          tkinter.messagebox.askretrycancel("Incorrect quantity!","Press RESET button to clear fields.")
    return


def qExit():
    exit = tkinter.messagebox.askyesno("Generate Quotation","Do you want to exit?")
    if exit > 0:
        root.destroy()
        return

def Reset():
    rand.set("") 
    Cable.set("")
    Conduit.set("")
    Camera.set("")
    # SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Labour_hours.set("")
    Tax.set("")
    Cost.set("")
    DVR_NVR.set("")
    Connectors.set("")
    
#===============================================================================================
rand = StringVar()
Cable=StringVar()
Conduit=StringVar()
Camera=StringVar()

Total=StringVar()
Service_Charge=StringVar()
Labour_hours=StringVar()
Tax=StringVar()
Cost=StringVar()
DVR_NVR=StringVar()
Connectors=StringVar()



lblReference= Label(f1, font=('verdana', 12, 'bold'),text="Reference#",bd=10,anchor="w",fg="#43e80c",bg="black")
lblReference.grid(row=0, column=0)
txtReference=Label(f1, font=('verdana',12,'bold'),textvariable=rand,bd=10,bg="black",justify='left',fg="#43e80c")
txtReference.grid(row=0,column=1)

lblCable= Label(f1, font=('verdana', 12, 'bold'),text="Cable per metre",fg="#43e80c",bd=10,anchor='w',bg="black")
lblCable.grid(row=1, column=0)
txtCable=Entry(f1,font=('verdana',12,'bold'),textvariable=Cable,bd=10,width=13,bg="light green",justify='right')
txtCable.grid(row=1,column=1)



lblConduit= Label(f1, font=('verdana', 12, 'bold'),text="Conduit/Ducting",fg="#43e80c",bd=10,anchor='w',bg="black")
lblConduit.grid(row=2, column=0)
txtConduit=Entry(f1, font=('verdana',12,'bold'),textvariable=Conduit,bd=10,width=13,bg="light green",justify='right')
txtConduit.grid(row=2,column=1)


lblCamera= Label(f1, font=('verdana', 12, 'bold'),text="Camera",fg="#43e80c",bd=10,anchor='w',bg="black")
lblCamera.grid(row=3, column=0)
txtCamera=Entry(f1, font=('verdana',12,'bold'),textvariable=Camera,bd=10,width=13,bg="light green",justify='right')
txtCamera.grid(row=3,column=1)

lblDVR_NVR= Label(f1, font=('verdana', 12, 'bold'),text="DVR/NVR",fg="#43e80c",bd=10,anchor='w',bg="black")
lblDVR_NVR.grid(row=4, column=0)
txtDVR_NVR=Entry(f1, font=('verdana',12,'bold'),textvariable=DVR_NVR,bd=10,width=13,bg="light green",justify='right')
txtDVR_NVR.grid(row=4,column=1)

lblConnectors= Label(f1, font=('verdana', 12, 'bold'),text="Connectors/Fixtures",fg="#43e80c",bd=10,anchor='w',bg="black")
lblConnectors.grid(row=5, column=0)
txtConnectors=Entry(f1, font=('verdana',12,'bold'),textvariable=Connectors,bd=10,width=13,bg="light green",justify='right')
txtConnectors.grid(row=5,column=1)

#============================================================================================================
#
#========================================================================================

lblLabour_hours= Label(f1, font=('verdana', 12, 'bold'),text="Labour hours",fg="#43e80c",bd=10,anchor='w',bg="black")
lblLabour_hours.grid(row=6, column=0)
txtLabour_hours=Entry(f1, font=('verdana',12,'bold'),textvariable=Labour_hours,bd=10,width=13,bg="light green",justify='right')
txtLabour_hours.grid(row=6,column=1)

lblCost= Label(f1, font=('verdana', 12, 'bold'),text="Installation Cost",fg="#43e80c",bd=10,anchor='w',bg="black")
lblCost.grid(row=1, column=2)
# txtCost=Entry(f1, font=('verdana',12,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost=Label(f1, font=('verdana',12,'bold'),textvariable=Cost,bd=10,bg="black",fg="#43e80c",anchor="w")
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('verdana', 12, 'bold'),text="Cost of Material",fg="#43e80c",bd=10,anchor='w',bg="black")
lblService.grid(row=2, column=2)
# txtService=Entry(f1, font=('verdana',12,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService=Label(f1, font=('verdana',12,'bold'),textvariable=Service_Charge,bd=10,bg="black",fg="#43e80c",anchor="w")
txtService.grid(row=2,column=3)


lblGST= Label(f1, font=('verdana', 12, 'bold'),text="GST",fg="#43e80c",bd=10,anchor='w',bg="black")
lblGST.grid(row=3, column=2)
txtGST=Label(f1, font=('verdana',12,'bold'),textvariable=Tax,bd=10,bg="black",fg="#43e80c",justify='right')
txtGST.grid(row=3,column=3)

# lblSubTotal= Label(f1, font=('verdana', 12, 'bold'),text="Sub Total",fg="#43e80c",bd=10,anchor='w',bg="black")
# lblSubTotal.grid(row=4, column=2)
# txtSubTotal=Label(f1, font=('verdana',12,'bold'),textvariable=SubTotal,bd=10,bg="black",fg="#43e80c",justify='right')
# txtSubTotal.grid(row=4,column=3)

lblInstallCost= Label(f1, font=('verdana', 12, 'bold'),text="Total Cost",fg="#43e80c",bd=10,anchor='w',bg="black")
lblInstallCost.grid(row=4, column=2)
txtInstallCost=Label(f1, font=('verdana',12,'bold'),textvariable=Total,bd=10,bg="black",fg="#43e80c",justify='right')
txtInstallCost.grid(row=4,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=5,pady=5,bd=8,font=('verdana',12,'bold'),width=8,text="Total",bg="black",fg="#43e80c",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=5,pady=5,bd=8,font=('verdana',12,'bold'),width=8,text="Reset",bg="black",fg="#43e80c",command=Reset).grid(row=7,column=1)

btnExit=Button(f1,padx=5,pady=5,bd=8,font=('verdana',12,'bold'),width=8,text="Exit",bg="black",fg="#43e80c",command=qExit).grid(row=7,column=2)


root.mainloop()


