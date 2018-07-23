'''
Building a relatively smart Dictionary in GUI form
@author:Nawaj
Note: the first half is back-end code for how the dictionary works, the
second half building a GUI using tkinter 
'''
import json
from difflib import get_close_matches as g

data=json.load(open("data.json"))
keys = data.keys()

def meaning():

    w = e1_value.get()

    if w in data:
        for i, j in enumerate(data[w]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.upper() in data:
        for i, j in enumerate(data[w.upper()]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.title() in data:
        for i, j in enumerate(data[w.title()]):
            t1.insert(END,str(i)+' '+j+'\n')
    else:
        list=g(w,keys,n=1,cutoff=0.8)
        if len(list) == 0:
            t1.insert(END,"Sorry, no word found!")
        else:
            real=list[0]
            answer=tkinter.messagebox.askquestion("Word Suggestion", "Is your word "+real+"?")
            
            if answer == "yes":
                for i, j in enumerate(data[real]):
                    t1.insert(END,str(i)+' '+j+'\n')
            #elif x == "yes":
                #for i, j in enumerate(data[real]):
                    #t1.insert(END,str(i)+' '+j+'\n')
            else:
                t1.insert(END,"Apologies, no word found. Please check your input word again.")


def meaning2():
    t1.delete(1.0,END)
    e1.delete(0,END)

    meaning

from tkinter import *
import tkinter.messagebox
root=Tk()

header=Label(root, text="A Relatively Smart Dictionary", bg="black", fg="white")
header.pack(fill=X)

label1=Label(root, text="Enter your word:")
label1.pack()

e1_value=StringVar()
e1=Entry(root, textvariable=e1_value)
e1.pack()

button=Button(root, text="Find meaning!", command=meaning, bg="lightgreen")
button.pack()

t1=Text(root)
t1.pack(fill=X)

label2=Label(root, text="Hit the button below to search another word!")
label2.pack()

button2=Button(root,text="Another word!", command=meaning2, bg="lightgreen")
button2.pack()


root.mainloop()
