from tkinter import*
import random

root=Tk()
root.title("Picnic Bag")
root.geometry("400x600")

bag_items=Label(root)
random_number=Label(root)

items=['bottle','biscuits','cube','notebook','chocolates','binoculars']

bag_items["text"] = str(items)

def random_item():
    random_list=random.sample(range(1,6),1)
    random_number["text"] = "Put item number" + str(random_list)

btn_1=Button(root,text="Click me!",command=random_item,anchor=CENTER)
btn_1.place(relx="0.5" , rely="0.5",anchor=CENTER)
bag_items.place(relx="0.5" , rely="0.3",anchor=CENTER)
random_number.place(relx="0.5", rely="0.4",anchor=CENTER)

root.mainloop()