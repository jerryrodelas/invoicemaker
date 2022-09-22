import time
import datetime
from tkinter import *
import tkinter.messagebox

from reportlab.pdfgen import canvas


root=Tk()
root.title("Invoice Generator")
root.geometry('1200x1000+0+0')
root.configure(background="#040608")


Tops=Frame(root,width=600,height=800,bd=8,bg="#040608")
Tops.pack()

f1=Frame(root,width=100,height=100,bd=8,bg="#040608")
f1.pack()
f2=Frame(root,width=300,height=700,bd=8,bg="#040608")
f2.pack(side=TOP)

fla=Frame(f1,width=200,height=200,bd=8,bg="#040608")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="#040608")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('verdana',12,'bold'),bg="#040608",text="Sedgcom Pty Ltd - Invoice Management",bd=10,fg="#e6df20")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Invoice Management","Do you want to exit the system?")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Email.set("")
  ShipDet.set("")
  LabourCost.set("")
  SubTotal.set("")
  WorkDesc.set("")
  TotalCost.set("")
  BOM.set("")
  GST.set("")
  MobileNo.set("")
  txtShowInvoice.delete("1.0",END)

def enterinfo():
  txtShowInvoice.delete("1.0",END)
  txtShowInvoice.insert(END,"Sedgcom Pty Ltd - Invoice\n\n")
  txtShowInvoice.insert(END,"Date :\t"+DateOfOrder.get()+"        Customer:"+Name.get()+"\n\n")
  txtShowInvoice.insert(END,"Email :\t"+Email.get()+"                                 Mobile Number:"+MobileNo.get()+"\n\n")
  txtShowInvoice.insert(END,"Work Description :\t"+WorkDesc.get()+"\n\n")
  txtShowInvoice.insert(END,"Labour Cost :\t"+LabourCost.get()+"             GST:"+GST.get()+"\n\n")
  txtShowInvoice.insert(END,"Bill of Materials :\t"+BOM.get()+"              SubTotal :"+SubTotal.get()+"               Total :\t"+TotalCost.get()+"\n\n")
  # txtShowInvoice.insert(END,"Total :\t"+TotalCost.get()+"\n\n")

def ShowTotalCost():
  txtShowInvoice.delete("1.0",END)

  try:
      cost_of_labour=float(LabourCost.get())
      bill_of_goods=float(BOM.get())
      subcost=cost_of_labour+bill_of_goods
      cost_no_gst="A$ "+ str('%.2f'%(subcost))
      SubTotal.set(cost_no_gst)

      gst=subcost*0.10
      paytax="A$ "+ str('%.2f'%(gst))
      GST.set(paytax)

      cost_with_gst=subcost+gst
      overall_cost="A$ "+ str('%.2f'%(cost_with_gst))
      TotalCost.set(overall_cost)
  except:
      tkinter.messagebox.askretrycancel("Amount Required!","Enter/Change the values of the cost of labour/materials.")
  return

def SavePDF(): # imports pdf report on the default folder where this file is located
     pdf_file = 'Invoice.pdf'

     can = canvas.Canvas(pdf_file)
     can.setFont("Courier", 24)
     can.drawString(60, 800, "Sedgcom Pty Ltd  -  Invoice")
     can.setFont("Courier", 16)
     can.drawString(60,770,DateOfOrder.get())
     can.drawString(60, 700,Email.get())
     can.drawString(60,670,ShipDet.get())
     can.drawString(60,640,"Labour Cost: A$ "+LabourCost.get())
     can.drawString(60,610,"Total without GST: "+SubTotal.get())
     can.drawString(60,580,"Work Description: "+WorkDesc.get())
     can.drawString(60,550,"GST due: "+GST.get())
     can.drawString(60,520,"Total without GST: "+TotalCost.get())

     can.showPage()
     can.save()



#=============================== Variables ========================================================
Name=StringVar()
Email=StringVar()
LabourCost=StringVar()
BOM=StringVar()
SubTotal=StringVar()
WorkDesc=StringVar()
TotalCost=StringVar()
GST=StringVar()
ShipDet=StringVar()
MobileNo=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d %b %Y"))
# ("%d/%m/%Y") output is formatted as 12/07/2018
#("%d %b, %Y") output is formatted as 12 Jun, 2018
#================================ Label Widget =================================================

lblName=Label(fla,text="Customer Name",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=0,column=0)
lblEmail=Label(fla,text="Email Address",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=0,column=2)
lblShipDet=Label(fla,text="Shipping Details",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=1,column=0)
lblMobileNo=Label(fla,text="Mobile Number",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=1,column=2)
lblLabourCost=Label(fla,text="Labour Cost",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=2,column=0)
lblBOM=Label(fla,text="Bill Of Materials",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=2,column=2)
lblWorkDesc=Label(fla,text="Work Description",font=('verdana',10,'bold'),bd=20,anchor='w',fg="#05fa22",bg="#040608").grid(row=3,column=0)
lblGST=Label(fla,text="GST (excl.)",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=3,column=2)
lblSubTotal=Label(fla,text="Sub Total ",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=4,column=0)
lblTotalCost=Label(fla,text="Total Cost",font=('verdana',10,'bold'),bd=20,fg="#05fa22",bg="#040608").grid(row=4,column=2)

#=============================== Entry Widget =================================================

etxname=Entry(fla,textvariable=Name,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxname.grid(row=0,column=1)

etxEmail=Entry(fla,textvariable=Email,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxEmail.grid(row=0,column=3)

etxShipDet=Entry(fla,textvariable=ShipDet,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxShipDet.grid(row=1,column=1)

etxLabourCost=Entry(fla,textvariable=LabourCost,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxLabourCost.grid(row=2,column=1)

etxBOM=Entry(fla,textvariable=BOM,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxBOM.grid(row=2,column=3)

etxMobileNo=Entry(fla,textvariable=MobileNo,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxMobileNo.grid(row=1,column=3)

etxSubTotal=Label(fla,textvariable=SubTotal,font=('verdana',10,'bold'),bg='#040608',fg='white',bd=10,width=22,justify='left')
etxSubTotal.grid(row=4,column=1)

etxTotalCost=Label(fla,textvariable=TotalCost,font=('verdana',10,'bold'),bg='#040608',fg='white',bd=10,width=22,justify='left')
etxTotalCost.grid(row=4,column=3)

etxWorkDesc=Entry(fla,textvariable=WorkDesc,font=('verdana',10,'bold'),bd=10,width=22,justify='left')
etxWorkDesc.grid(row=3,column=1)

etxGST=Label(fla,textvariable=GST,font=('verdana',10,'bold'),bg='#040608',fg='white',bd=10,width=22,justify='left')
etxGST.grid(row=3,column=3)

#=============================== Text Widget ============================================================

ShowInvoice=Label(f2,textvariable=DateOfOrder,font=('verdana',10,'bold'),fg="#05fa22",bg="#040608").grid(row=0,column=5)
txtShowInvoice=Text(f2,height=30,width=70,bd=10,font=('verdana',10,'bold'),fg="#05fa22",bg="#040608")
txtShowInvoice.grid(row=1,column=5)

#=============================== buttons ===============================================================

btnShowTotalCost=Button(flb,text='Show Total Cost',padx=10,pady=10,bd=8,font=('verdana',10,'bold'),width=14,fg="#05fa22",bg="#040608",command=ShowTotalCost).grid(row=0,column=0)

btnReset=Button(flb,text='Reset',padx=10,pady=10,bd=8,font=('verdana',10,'bold'),width=14,command=reset,fg="#05fa22",bg="#040608").grid(row=0,column=1)

btnViewInvoice=Button(flb,text='View Invoice',padx=10,pady=10,bd=8,font=('verdana',10,'bold'),width=14,command=enterinfo,fg="#05fa22",bg="#040608").grid(row=0,column=2)

btnGeneratePDF=Button(flb,text='Generate PDF',padx=10,pady=10,bd=8,font=('verdana',10,'bold'),width=14,command=SavePDF,fg="#05fa22",bg="#040608").grid(row=0,column=3)

btnExit=Button(flb,text='Exit',padx=10,pady=10,bd=8,font=('verdana',10,'bold'),width=14,command=exit,fg="#05fa22",bg="#040608").grid(row=0,column=4)

root.mainloop()

