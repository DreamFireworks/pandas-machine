import sys
from tkinter import *
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as tkFont
import openpyxl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

window = Tk()
window.geometry("780x400")
window.title("Pandas Machine By Serhan Eraslan")
window.resizable(width=False,
                 height=False)

### UPPER HALF

# OpenFile
filename = ""
def openfile():
    global filename
    filename = filedialog.askopenfilename()


openbutton = Button(window, 
                    text = "Open", 
                    command = openfile,
                    justify="center",
                    bg="#efefef")
                    
openbutton.place(x=0,
                 y=5,
                 width=100,
                 height=40)

# Import Selection (CSV,XLS,XLSX)
radio = IntVar()
selected=""
def selection():
    global selected
    selectx = radio.get()
    if selectx==1:
        selected="csv"
    else:
        selected="excel"

csvbut= Radiobutton(window,
                    text="csv",
                    variable=radio,
                    value=1,
                    command=selection,
                    justify="center",
                    bg="#efefef",
                    activeforeground="#ff0000")
csvbut.place(x=100,
             y=0,
             width=90,
             height=30)

xlsbut= Radiobutton(window,
                    text="excel",
                    variable=radio,
                    value=2,
                    command=selection,
                    justify="center",
                    bg="#efefef",
                    activeforeground="#ff0000")
xlsbut.place(x=105,
             y=20,
             width=90,
             height=30)
             
             
# Import
data1=[]
def readselect():
    try:
        if selected=="excel":
            excell=pd.read_excel(filename,engine='openpyxl')
            #excell=pd.DataFrame(excell)
            messagebox.showinfo("Done!","Excel File imported!")
            global data1
            data1 = excell
            print(data1.head(5))
#            colnames.config(text=np.array(csv.columns))
#            csvhead.config(text=csv.head())
            column_names.config(text=np.array(data1.columns))
            preview.config(text=data1.head(5))

        else:
            csvv=pd.read_csv(filename)
            messagebox.showinfo("Done!", "CSV File imported!")
            global data
            data1=csvv
            print(data1.head(5))
#            colnames.config(text=np.array(csv.columns))
#            csvhead.config(text=csv.head())
            column_names.config(text=np.array(data1.columns))
            preview.config(text=data1.head(5))
        print("Data imported")
    except FileNotFoundError:
        messagebox.showinfo("Error!", "File not found")
    except:
        messagebox.showinfo("Error!", "Something went wrong!")
        
importbutton = Button(window, 
                      text="Import",
                      command=readselect,
                      justify="center",
                      bg="#efefef")
importbutton.place(x=180,
                   y=5,
                   width=75,
                   height=40)

# Save

def saver():
    pass

save=Button(window,
            text="Save As",
            command=saver,
            justify="center",
            bg="#efefef")
save.place(x=260,
           y=5,
           width=75,
           height=40)

# Colum1 Entry
col_one=Entry(window,
              justify="center",
              bg="#dedede")
col_one.insert(0, 'Column1(X)')
col_one.place(x=340,
              y=5,
              width=100,
              height=40)

# Colum2 Entry
col_two=Entry(window,
              justify="center",
              bg="#dedede")
col_two.insert(0, 'Column2(Y)')
col_two.place(x=445,
              y=5,
              width=100,
              height=40)

# Row Entry
row1=Entry(window,
           justify="center",
           bg="#dedede")
row1.insert(0, 'Row')
row1.place(x=550,
           y=5,
           width=100,
           height=40)

# Number Entry
num1=Entry(window,
           justify="center",
           bg="#dedede")
num1.insert(0, 'Number')
num1.place(x=655,
           y=5,
           width=100,
           height=40)

# Exit

def exitt():
    messagebox.showinfo("Bye!","Thanks for Using Pandas Machine, See ya!")
    window.destroy()

exitbutton= Button(window,
                   text="X",
                   justify="center",
                   command=exitt,
                   bg="#ff3366")
ft = tkFont.Font(family='Times',size=14)
exitbutton.place(x=757,
                 y=5,
                 width="20",
                 height="18")
# clear

def clearr():
    col_one.delete(0, 100)
    col_one.insert(0, 'Column1')
    col_two.delete(0, 100)
    col_two.insert(0, 'Column2')
    row1.delete(0, 100)
    row1.insert(0, 'Row')
    num1.delete(0, 100)
    num1.insert(0, 'Number')
    readselect()

clearbutton= Button(window,
                    text="C",
                    justify="center",
                    command=clearr,
                    bg="#efefef")
                    
clearbutton.place(x=757,
                 y=25,
                 width="20",
                 height="20")
# Column Names
column_names=Label(window,
                   text="Column Names will shown here",
                   justify="center",
                   bg="#eeefff",
                   relief="groove")
column_names.place(x=0,
                   y=50,
                   width=335,
                   height=40)

# Result

result= Label(window,
              text="Result will shown here", 
              justify="center",
              bg="#eeefff",
              relief="groove")
result.place(x=0,
             y=100,
             width=335,
             height=100)


# Data Preview
preview= Label(window,
               text="Data's First 5 obs will shown here",
               justify="center",
               bg="#eeefff",
               relief="groove")
preview.place(x=340,
              y=50,
              width=440,
              height=150)

# LOWER HALF
def passs():
    pass


# LEFTSIDE BUTTONS

# Mean

def meanb():
    try:
        global data1
        res=data1[col_one.get()].mean()
        result.config(text="Mean of {} Column is {}".format(col_one.get(),res))
        print("Mean: ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
mean_button = Button(window, 
                     text="Mean",
                     command=meanb,
                     justify="center",
                     bg="#efefef")
mean_button.place(x=0,
              y=205,
              width=75,
              height=40)
              
# Median

def medianb():
    try:
        global data1
        res= data1[col_one.get()].median()
        result.config(text="Median of {} Column is {}".format(col_one.get(),res))
        print("Median calculated: ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")

median_button = Button(window, 
                      text="Median",
                      command=medianb,
                      justify="center",
                      bg="#efefef")
median_button.place(x=0,
              y=250,
              width=75,
              height=40)

# Mode

def modeb():
    try:
        global data1
        res=list(data1[col_one.get()].mode())
        result.config(text="Mode of {} Column = {}".format(col_one.get(),res))
        print("Mode: ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")

mode_button = Button(window, 
                      text="Mode",
                      command=modeb,
                      justify="center",
                      bg="#efefef")
mode_button.place(x=0,
              y=295,
              width=75,
              height=40)
              
# observations

def obsb():
    try:
        global data1
        res = len(data1.index)
        result.config(text="Total Observation(s): {}".format(res))
        print("Observations: ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
obs_button = Button(window, 
                      text="Obs",
                      command=obsb,
                      justify="center",
                      bg="#efefef")
obs_button.place(x=0,
              y=340,
              width=75,
              height=40)

# Min 
 
def minb():
    try:
        global data1
        res=data1[col_one.get()].min()
        result.config(text="Min. of {} Column is {}".format(col_one.get(),res))
        print("Min. : ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")

min_button = Button(window, 
                      text="Min",
                      command=minb,
                      justify="center",
                      bg="#efefef")
min_button.place(x=85,
              y=205,
              width=75,
              height=40)
              
# Max

def maxb():
    try:
        global data1
        res=data1[col_one.get()].max()
        result.config(text="Max. of {} Column is {}".format(col_one.get(),res))
        print("Max. : ",res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
max_button = Button(window, 
                      text="Max",
                      command=maxb,
                      justify="center",
                      bg="#efefef")
max_button.place(x=85,
             y=250,
             width=75,
             height=40)


# Shape

def shapeb():
    try:
        global data1
        res=data1.shape
        result.config(text="(Row, Column) = " + str(res))
        print("Shape: ", res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")

shape_button = Button(window, 
                      text="Shape",
                      command=shapeb,
                      justify="center",
                      bg="#efefef")
shape_button.place(x=85,
              y=295,
              width=75,
              height=40)

# Describe

def descb():
    try:
        global data1
        res=data1.describe()
        preview.config(text=res)
        result.config(text="Descriptive Statistics")
        print("Description: \n ", res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
describe_button = Button(window, 
                      text="Describe",
                      command=descb,
                      justify="center",
                      bg="#efefef")
describe_button.place(x=85,
              y=340,
              width=75, 
              height=40)


# Variance

def varb():
    try:
        global data1
        res = np.var(data1[col_one.get()])
        result.config(text="Variance of {} Column is {:.4f}".format(col_one.get(),res))
        print("Variance calculated: ", res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")

variance_button = Button(window, 
                      text="Variance",
                      command=varb,
                      justify="center",
                      bg="#efefef")
variance_button.place(x=170,
              y=205,
              width=75,
              height=40)
              
# Standard Deviation

def stdb():
    try:
        global data1
        res=float(np.std(data1[col_one.get()]))
        result.config(text="Std. Deviation of {} Column is {:.4f}".format(col_one.get(),res))
        print("Standard Deviation calculated: ", res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
stddev_button = Button(window, 
                      text="Std Deviation",
                      command=stdb,
                      justify="center",
                      bg="#efefef")
stddev_button.place(x=170,
               y=250,
               width=75,
               height=40)

# Missing Values

def missingval():
    try:
        global data1
        res = data1.isnull().sum()
        preview.config(text=res)
        result.config(text="Missing Values")
        print("Missing values: \n ", res)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
missing_button = Button(window, 
                      text="Missing Val.",
                      command=missingval,
                      justify="center",
                      bg="#efefef")
missing_button.place(x=170,
              y=295,
              width=75,
              height=40)
              
# Preview

def prevb():
    try:
        global data1
        preview.config(text=data1.head(5))
        result.config(text="Data Preview")
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
        
prev_button = Button(window, 
                      text="Preview",
                      command=prevb,
                      justify="center",
                      bg="#efefef")
prev_button.place(x=170,
              y=340,
              width=75,
              height=40)

# Button 13

def button13():
    pass
    """
    try:
    
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
    """

 
button13 = Button(window, 
                      text="Button13",
                      command=passs,
                      justify="center",
                      bg="#efefef")
button13.place(x=255,
              y=205,
              width=75,
              height=40)
              
# Button 14

def button14():
    pass
    """
    try:
    
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
    """

button14 = Button(window, 
                      text="Button14",
                      command=passs,
                      justify="center",
                      bg="#efefef")
button14.place(x=255,
             y=250,
             width=75,
             height=40)


# Button 15

def button15():
    pass
    """
    try:
    
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
    """

button15 = Button(window, 
                      text="Button15",
                      command=passs,
                      justify="center",
                      bg="#efefef")
button15.place(x=255,
              y=295,
              width=75,
              height=40)

# Button 16

def button16():
    pass
    """
    try:
    
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
    """


button16 = Button(window, 
                      text="Button16",
                      command=passs,
                      justify="center",
                      bg="#efefef")
button16.place(x=255,
              y=340,
              width=75, 
              height=40)


# RIGHTSIDE BUTTONS Graphics.

# Line
def linep():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        ax1.plot(data1[col_one.get()], color = 'g')
        line1 = FigureCanvasTkAgg(figure1, window) 
        line1.get_tk_widget().place(x=525,y=205,width=240,height=175)
        ax1.set_xlabel(data1[col_one.get()])
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")

    
    
line_plot = Button(window, 
                      text="Line",
                      command=linep,
                      justify="center",
                      bg="#efefef")
line_plot.place(x=345,
              y=205,
              width=75,
              height=40)
              
# Histogram

def histp():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        ax1.hist(data1[col_one.get()], color = 'g')
        scatter1 = FigureCanvasTkAgg(figure1, window) 
        scatter1.get_tk_widget().place(x=525,y=205,width=240,height=175) 
        ax1.set_xlabel(data1[col_one.get()])
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")


#bins=num1.get()
hist_plot = Button(window, 
                      text="Hist",
                      command=histp,
                      justify="center",
                      bg="#efefef")
hist_plot.place(x=345,
             y=250,
             width=75,
             height=40)


# Scatter
def scatterp():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        ax1.scatter(data1[col_one.get()],data1[col_two.get()], color = 'g')
        scatter1 = FigureCanvasTkAgg(figure1, window) 
        scatter1.get_tk_widget().place(x=525,y=205,width=240,height=175)
        ax1.set_xlabel(data1[col_one.get()])
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")

# Graph output
    #x=515,y=205,width=240,height=175
    
scatter_plot = Button(window, 
                      text="Scatter",
                      command=scatterp,
                      justify="center",
                      bg="#efefef")
scatter_plot.place(x=345,
              y=295,
              width=75,
              height=40)

# Regplot   

def regressionp():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        sns.regplot(data1[col_one.get()],data1[col_two.get()], color = 'g',ax=ax1)
        regpl = FigureCanvasTkAgg(figure1, window) 
        regpl.get_tk_widget().place(x=525,y=205,width=240,height=175)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")


regression_button = Button(window, 
                      text="Regression",
                      command=regressionp,
                      justify="center",
                      bg="#efefef")
regression_button.place(x=345,
              y=340,
              width=75, 
              height=40)

# BoxPlot

def boxplotb():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        sns.boxplot(data1[col_one.get()], color = 'g',ax=ax1)
        boxpl = FigureCanvasTkAgg(figure1, window) 
        boxpl.get_tk_widget().place(x=525,y=205,width=240,height=175)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")



boxplot_button = Button(window, 
                      text="Boxplot",
                      command=boxplotb,
                      justify="center",
                      bg="#efefef")
boxplot_button.place(x=430,
              y=205,
              width=75,
              height=40)
              
# SwarmPlot

def swarmp():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        sns.swarmplot(data1[col_one.get()],color='g',ax=ax1)
        swarmpl = FigureCanvasTkAgg(figure1, window) 
        swarmpl.get_tk_widget().place(x=525,y=205,width=240,height=175)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")

        
swarm_button = Button(window, 
                      text="Swarm Plot",
                      command=swarmp,
                      justify="center",
                      bg="#efefef")
swarm_button.place(x=430,
             y=250,
             width=75,
             height=40)


# kdeplot   

def kdepl():
    try:
        global data1
        figure1 = plt.Figure(figsize=(2,1), dpi=50)
        ax1 = figure1.add_subplot(111)
        sns.kdeplot(data1[col_one.get()],color='g',ax=ax1)
        swarmpl = FigureCanvasTkAgg(figure1, window) 
        swarmpl.get_tk_widget().place(x=525,y=205,width=240,height=175)
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")


kde_button = Button(window, 
                      text="KDE Plot",
                      command=kdepl,
                      justify="center",
                      bg="#efefef")
kde_button.place(x=430,
              y=295,
              width=75,
              height=40)

# Button 24

def button24():
    pass
    """
    try:
    
    except KeyError:
        messagebox.showinfo("Error!","Column name is not available")
    except TypeError:
        messagebox.showinfo("Error!","Type is not suitable for calculation, or data is not imported")
    except:
        messagebox.showinfo("Error!","Something went wrong!")
    """

button24 = Button(window, 
                      text="Button24",
                      command=passs,
                      justify="center",
                      bg="#efefef")
button24.place(x=430,
              y=340,
              width=75, 
              height=40)
              
window.mainloop()