from tkinter import Entry, Button, Listbox, Scrollbar, END, Tk, X, Y, BOTH, RIGHT, BOTTOM, HORIZONTAL, VERTICAL, GROOVE
from tkinter.messagebox import showerror
from threading import Thread
from urllib.request import urlopen
import json
from urllib.error import URLError    

height = 700
width = 500

def search():
    try:
        if len(searchbox.get()) > 0 and searchbox.get() != "Search":
            apiUrl = "https://myrestproject.000webhostapp.com/dictionary.php?limit=0-1000&query={}".format(searchbox.get())
            with urlopen(apiUrl) as words:
                data = json.loads(words.read().decode())
                AnsList.delete(0, END)
                for dictionary in data:
                    if dictionary["word"].lower() == searchbox.get().lower():
                        AnsList.insert("end", dictionary["word"]+" :")
                        AnsList.insert("end", dictionary["definition"])
                        AnsList.insert("end", "")
    except Exception:
        showerror("Error", "Some Thing Went Wrong! Please Try Again")

root = Tk()
root.title("Dictionary")
root.geometry("{}x{}".format(width, height))
root.resizable(False, False)

searchbox = Entry(root)
searchbox.insert(0, "Search")
searchbox.pack(fill=X, ipady=5)
searchbutton = Button(root, text="Click To Search", relief=GROOVE)
searchbutton.pack(fill=X, ipady=5, pady=(3,0))
searchbutton.config(command=search)

DictList = Listbox(root)
DictList.pack(fill=BOTH, expand=True)
DictScrollx = Scrollbar(DictList, orient=HORIZONTAL)
DictScrollx.config(command=DictList.xview)
DictScrollx.pack(fill=X, side=BOTTOM)
DictScrolly = Scrollbar(DictList, orient=VERTICAL)
DictScrolly.config(command=DictList.yview)
DictScrolly.pack(fill=Y, side=RIGHT)
DictList.config(yscrollcommand=DictScrolly.set)
DictList.config(xscrollcommand=DictScrollx.set)

AnsList = Listbox(root)
AnsList.pack(fill=BOTH, expand=True)
AnsScrollx = Scrollbar(AnsList, orient=HORIZONTAL)
AnsScrollx.config(command=AnsList.xview)
AnsScrollx.pack(fill=X, side=BOTTOM)
AnsScrolly = Scrollbar(AnsList, orient=VERTICAL)
AnsScrolly.config(command=AnsList.yview)
AnsScrolly.pack(fill=Y, side=RIGHT)
AnsList.config(yscrollcommand=AnsScrolly.set)
AnsList.config(xscrollcommand=AnsScrollx.set)

root.withdraw()
root.update_idletasks()
xloc = (root.winfo_screenwidth() - width) / 2
yloc = (root.winfo_screenheight() - height) / 2
root.geometry("+%d+%d" % (xloc, yloc))
root.deiconify()

class Api(Thread):
    apiUrl = "https://myrestproject.000webhostapp.com/dictionary.php?limit=0-1000"
    def run(self):
        try:
            with urlopen(self.apiUrl) as words:
                data = json.loads(words.read().decode())
                for dictionary in data:
                    DictList.insert("end", dictionary["word"]+" :")
                    DictList.insert("end", dictionary["definition"])
                    DictList.insert("end", "")
        except URLError:
            showerror("Error", "No Internet Connection")

api = Api()
api.start()
root.mainloop()    