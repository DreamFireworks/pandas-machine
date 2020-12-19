from tkinter import *
import numpy as np
import pandas as pd
from tkinter import messagebox

window = Tk()
window.geometry("450x300")
window.title("Pandas Machine!")
csv=[]

def readcsv():
    csvv=pd.read_csv(csvrd.get())
    messagebox.showinfo("Done!", "Imported csv Succesfully!")
    global csv
    csv=csvv
    print(csv.head())
    colnames.config(text=np.array(csv.columns))
    csvhead.config(text=csv.head())
    
def meancalc():
    global csv
    csvv = csv
    result=csvv[mean1.get()].mean()
    print(result)
    meanout.config(text="Mean of {} Column is {}, rounded: {}".format(mean1.get(),result,result.round(2)))
    
def vardev():
    global csv
    csvv= csv
    inpt=vardev1.get()
    variance=csvv[inpt].var()
    stdev=np.sqrt(variance)
    print(variance,stdev)
    vardevout.config(text="Variance of {} Column is {}, rounded: {} ,\n Standard Deviation of {} Column is {}, rounded: {}".format(inpt,variance,variance.round(2),inpt,stdev,stdev.round(2)))
    
csvrd= Entry(window)
read1= Button(window, text="Import!", command=readcsv)
colnames= Label(window,bg="white",text='Column Names')
csvhead= Label(window,bg="white",text='Data Preview')


mean1= Entry(window)
meanCalc= Button(window, text="Calculate Mean!", command=meancalc)
meanout= Label(window,bg='white', text='Result Of Mean')

vardev1= Entry(window)
vardevCalc=Button(window, text="Calculate Variance!", command=vardev)
vardevout=Label(window,bg='white', text='Result Of Variance')


label1= Label(window, text="File Name.csv:")
label2= Label(window, text="Operations")


op1= Label(window, text="Mean for column:")
op2= Label(window,text="Variance of column:")

csvrd.grid(row=0,column=1)
read1.grid(row=0,column=2)
colnames.grid(row=1,column=0,columnspan=4)
csvhead.grid(row=2,column=0,columnspan=4)


mean1.grid(row=4,column=1)
op1.grid(row=4,column=0)
meanCalc.grid(row=4,column=2)
meanout.grid(row=6,column=0,columnspan=4)


vardev1.grid(row=7,column=1)
op2.grid(row=7,column=0)
vardevCalc.grid(row=7,column=2)
vardevout.grid(row=8,column=0,columnspan=4)


label1.grid(row=0,column=0) #read csv
label2.grid(row=3,column=0,columnspan=2) # Operations

window.mainloop()