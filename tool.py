from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os


#//------- FUNCTIONS --------\\
def createBox(title,message,type): #Creates a message box
    match type:
        case "info":
            messagebox.showinfo(title,message)
        case "warn":
            messagebox.showwarning(title,message)
        case "error":
            messagebox.showerror(title,message)

def errorBox(code): #Error display
    match code:
        case 0:
            createBox("Credits","Made by Ian Leisure\nIntro to Software Development Class 2024\nVersion 1.0","info")
        case 1:
            createBox("BPM Conversion Error","Please enter a valid number.","info")
def exitButton(): # Exits program
    exit(0)


def helpMenu(): # Builds the second help menu
    HELP_WINDOW = Toplevel(WINDOW) #Generates New Window
    HELP_WINDOW.title("BPM Converter Help")
    HELP_WINDOW.iconphoto(False,WINDOW_ICON)
    def bpmMilliHelp():
        CONTENT_TITLE.config(text="BPM to Milliseconds")
        CONTENT_TEXT.config(text="1 Minute = 60,000 milliseconds \nDividing 60,000 milliseconds by the BPM (Beats per minute) grants us the \nlength of a quarter note in milliseconds.")
    def conversionHelp():
        CONTENT_TITLE.config(text="How to Use the Tool")
        CONTENT_TEXT.config(text="To use the tool, first input an integer (e.x. 120), and click the \"Convert\" button.\n Then, this program will output several values that correspond\nwith their respective note length.\n\nThis program does not work with decimals at this current time.")
    HELP_MENU = Menu(WINDOW)

    HELP_USAGE = Menu(HELP_MENU,tearoff=0)
    HELP_MENU.add_cascade(label="Usage",menu=HELP_USAGE)
    HELP_USAGE.add_command(label="Conversion",command=conversionHelp)

    HELP_CONVERT = Menu(HELP_MENU, tearoff = 0)
    HELP_MENU.add_cascade(label = "Conversion", menu = HELP_CONVERT)
    HELP_CONVERT.add_command(label = "BPM to Milliseconds", command = bpmMilliHelp) #Help on bpm to milli
    
    
    INFO_PANEL = LabelFrame(HELP_WINDOW,padx=10,pady=10,text = "Help")
    INFO_PANEL.pack(expand=1)

    CONTENT_TITLE = Label(INFO_PANEL,text="Help Menu")
    CONTENT_TITLE.pack(side="top")

    CONTENT_TEXT = Label(INFO_PANEL,text="Welcome to the Help Menu!")
    CONTENT_TEXT.pack(side="bottom")
    HELP_WINDOW.config(menu = HELP_MENU)#Adds menu to main window
    HELP_WINDOW.mainloop()


def convertBPMtoMilli(): # Conversion button from BPM to Milli
    m = 60000
    entryVal = BPM_ENTRY.get()
    if entryVal.isnumeric():
        bpm = float(entryVal)
        quartnote = int((m/bpm)*100)/100
        QUART_OUTPUT.config(text=str(quartnote)+" ms")
        EIGHT_OUTPUT.config(text=str(quartnote/2)+" ms")
        SIXTEEN_OUTPUT.config(text=str(quartnote/4)+" ms")
        THIRT_OUTPUT.config(text=str(quartnote/8)+" ms")
    else:
        errorBox(1)


def creditsConstruct(): # Function for credits button
    errorBox(0)

#//------- WIDGETS --------\\

WINDOW = Tk() #Main Window
WINDOW.title("BPM Conversion Tool") #Sets title
WINDOW.geometry("250x250")
WINDOW_ICON = ImageTk.PhotoImage(Image.open("ico.png"))
WINDOW.iconphoto(False,WINDOW_ICON)

#---Menu---

MENU = Menu(WINDOW)
HELP_BAR = Menu(MENU, tearoff = 0)
MENU.add_cascade(label = "Help", menu = HELP_BAR)
HELP_BAR.add_command(label = "Help", command = helpMenu) #Help button
HELP_BAR.add_command(label = "Credits",command = creditsConstruct) #Credits button 
HELP_BAR.add_separator()
HELP_BAR.add_command(label = "Exit", command = exitButton) #Exit button

#---Top Frame---

backgroundImg = ImageTk.PhotoImage(Image.open("background.png"))
BACKGROUND_LABEL = Label(WINDOW, image = backgroundImg)
BACKGROUND_LABEL.place(x=0,y=0,relwidth=1,relheight=1)
TOP_FRAME = LabelFrame(WINDOW,padx=10,pady=10,text="BPM to Milli")
TOP_FRAME.place(relx=0.5,rely=0.45,anchor=CENTER)

#---Text above the entry box

BPM_LABEL = Label(TOP_FRAME,text="BPM")
BPM_LABEL.grid(row=0,column=0)

#---Entry box

BPM_ENTRY = Entry(TOP_FRAME,border=1)
BPM_ENTRY.grid(row=1,column=0)

#---Conversion button

BPM_CONVERT = Button(TOP_FRAME,border=1,command=convertBPMtoMilli,text="Convert")
BPM_CONVERT.grid(row=1,column=1)

#--- Value frame

VALUES_FRAME = Frame(TOP_FRAME,border=1,padx=10,pady=10)
VALUES_FRAME.grid(row=2,column=0,columnspan=1,rowspan=3)

#--- Quarter note
QUART_LABEL = Label(VALUES_FRAME,text="1/4").grid(row=0,column=0)
QUART_OUTPUT = Label(VALUES_FRAME,text="N/A",border=1,background="white")
QUART_OUTPUT.grid(row=0,column=1)

#--- Eighth note
EIGHT_LABEL = Label(VALUES_FRAME,text="1/8").grid(row=1,column=0)
EIGHT_OUTPUT = Label(VALUES_FRAME,text="N/A",border=1,background="white")
EIGHT_OUTPUT.grid(row=1,column=1)

#--- Sixteenth note
SIXTEEN_LABEL = Label(VALUES_FRAME,text="1/16").grid(row=2,column=0)
SIXTEEN_OUTPUT = Label(VALUES_FRAME,text="N/A",border=1,background="white")
SIXTEEN_OUTPUT.grid(row=2,column=1)

#--- 32nd note
THIRT_LABEL = Label(VALUES_FRAME,text="1/32").grid(row=3,column=0)
THIRT_OUTPUT = Label(VALUES_FRAME,text="N/A",border=1,background="white")
THIRT_OUTPUT.grid(row=3,column=1)

WINDOW.config(menu = MENU)#Adds menu to main window

WINDOW.mainloop()
