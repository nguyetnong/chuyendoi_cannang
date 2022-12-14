from tkinter import*

def chuyen_doi_can_nang():
    kg_gram=float(entry_kg.get())
    ketqua_gram=kg_gram*1000
    kq_label_gram["text"]=ketqua_gram

    ketqua_pounds=kg_gram*2.20462
    kq_label_pounds["text"]=ketqua_pounds
    
    ketqua_ounce=kg_gram*35.274
    kq_label_ounce["text"]=ketqua_ounce
    
    


window=Tk()
window.title(" chuyen doi can nang ")
label_kg=Label(master=window,text="Enter the weight in Kg ")
label_kg.grid(row=0,column=0)
entry_kg=Entry(master=window)
entry_kg.grid(row=0,column=1)
Button_kg=Button(master=window,text="Convert",command=chuyen_doi_can_nang)
Button_kg.grid(row=0,column=2)

label_gram=Label(master=window,text="Gram")
label_gram.grid(row=1,column=0)
kq_label_gram=Label(master=window)
kq_label_gram.grid(row=2,column=0)
# kq_label_gram.delete(0,END)
# kq_label_gram.insert(END,)

label_pounds=Label(master=window,text="Pounds")
label_pounds.grid(row=1,column=1)
kq_label_pounds=Label(master=window)
kq_label_pounds.grid(row=2,column=1)


label_ounce=Label(master=window,text="Ounce")
label_ounce.grid(row=1,column=2)
kq_label_ounce=Label(master=window)
kq_label_ounce.grid(row=2,column=2)

window.mainloop()

