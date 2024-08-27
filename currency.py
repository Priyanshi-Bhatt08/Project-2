""" Title : Currency Converter
    Date : 05/04/2024
    Subject : Python """

import tkinter as tk
from tkinter import *
import tkinter.messagebox        # message box is imported to display pop box with specified title and message.
from tkinter import PhotoImage

root=tk.Tk()                     #It helps to display the root window and manages all componenets (name of window) 
root.title("Currency Conversion")

# Image section 
image_path=PhotoImage(file="currency.jpg")
bg_image=tkinter.Label(root,image=image_path)
bg_image.place(relheight=1.5,relwidth=1)

root.configure(bg = '#e6e5e5')    #customize appearance of widgets
root.geometry("600x600")          # width*height

headlabel = tk.Label(root,font=('lato black', 19,'bold'), text = '         Python Project    :    Currency Converter  ', bg= 'lightblue',fg='black') 
# root is written for label is to be placed in root
headlabel.grid(row=1, column=0,sticky=W)

variable1 = tk.StringVar(root)  #StringVar is used to hold string values.StringVar object that can be used to manage string data.StringVar have getter and setter method.
variable2 = tk.StringVar(root) 

variable1.set("currency") 
variable2.set("currency") 

CurrencyCode_list= ["INR","USD","CAD","CNY","DKK","EUR"]
# 1 USD = 83.47 Rupees
# 1 CAD = 61.47 Rupees
# 1 CNY(Chinese Yaun) = 11.54 Rupees
# 1 DKK(Danish Krone) = 12.11 Rupees
# 1 EUR = 90.35 Rupees

# method for conversion
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates  #forex_python is a free foreign exchange rates and currency conversion
    c= CurrencyRates()
    
    from_cur= variable1.get();
    to_cur=variable2.get()
    
    if(Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error!!  AMOUNT NOT ENTERED")
        
    elif(from_cur=="currency" or to_cur=="currency"):
        tkinter.messagebox.showinfo("Error!!  CURRENCY NOT SELECTED")
        
    else:
        new_amt= c.convert(from_cur,to_cur,float(Amount1_field.get()))
        Amount2_field.insert(0,str(new_amt))

# method to clear amount
def clear_all():
    Amount1_field.delete(0,tk.END)
    Amount2_field.delete(0,tk.END)

Label_1 =Label(root, font=('lato black', 27,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black") #foreground
Label_1.grid(row=1, column=0,sticky=W) #W-West or left center

label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  Amount :  ",bg="#e6e5e5", fg="black")
label1.grid(row=2,column=0,sticky=W)                 


label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  From Currency  :  ",bg="#e6e5e5", fg="black")
label1.grid(row=3,column=0,sticky=W)     


label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  To Currency  :  ",bg="#e6e5e5", fg="black")
label1.grid(row=4,column=0,sticky=W)     


label1= tk.Label(root,font=('lato black',15,'bold'),text="         Converted Amount :",bg="#e6e5e5", fg="black")
label1.grid(row=8,column=0,padx=2,sticky=W)   

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=5, column=0,sticky=W)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=7, column=0,sticky=W)


FromCurrency_option= tk.OptionMenu(root,variable1,*CurrencyCode_list) 
ToCurrency_option= tk.OptionMenu(root,variable2,*CurrencyCode_list)

FromCurrency_option.grid(row=3,column=0,ipadx=45,sticky=E)  
ToCurrency_option.grid(row=4,column=0,ipadx=45,sticky=E)    

Amount1_field= tk.Entry(root)     
Amount1_field.grid(row=2,column=0,sticky=E) # E-east or right center

Amount2_field= tk.Entry(root)
Amount2_field.grid(row=8,column=0,sticky=E)   


Label_9= Button(root,font=("arial",15,"bold"),text="  Convert  ",padx=2,pady=2,bg="#e6e5e5", fg="black",command= RealTimeCurrencyConversion)
Label_9.grid(row=6,column=0)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="", bg="#e6e5e5",fg ="black")
Label_1.grid(row=9, column=0,sticky=W)


Label_9= Button(root,font=("arial",15,"bold"),text="  Clear All ",bg="white", fg="green",command= clear_all)
Label_9.grid(row=10,column=0)

# Mainloop
root.mainloop()   #an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed. 