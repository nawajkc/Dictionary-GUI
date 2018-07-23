import json
import difflib
#from difflib import SequenceMatcher as sm
from difflib import get_close_matches as g

data=json.load(open("data.json"))

keys=[]
for i, j in data.items():
    keys.append(i)
#easier, pythonic way, is to call data.keys()
def meaning(w):

    if w in data:
        for i, j in enumerate(data[w]):
            print(i,j)
    elif w.upper() in data:
        for i, j in enumerate(data[w.upper()]):
            print(i,j)
    elif w.title() in data:
        for i, j in enumerate(data[w.title()]):
            print(i,j)
    else:
        list=g(w,keys,n=1,cutoff=0.8)
        if len(list) == 0:
            print("Sorry, no word found.")
        else:
            real=list[0]
            print ("Is your word",real,"?")
            x = input("Yes or No?")
            if x == "Yes":
                for i, j in enumerate(data[real]):
                    print(i,j)
            elif x == "yes":
                for i, j in enumerate(data[real]):
                    print(i,j)
            else:
                print("Well, we done here")



    start_dict()


def start_dict():
    ask=input("Press Y if you want to use the dictionary. Otherwise, press N.")
    if ask == "Y":
        word=input("Enter your word here:")
        word=word.lower()
        meaning(word)
    else:
        exit

start_dict()
