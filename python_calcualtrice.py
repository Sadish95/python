import tkinter as tk


calcul=""

def ajout_calcul(symbol):
    global calcul
    calcul+=str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)

def eval_calcul():
    global calcul
    try:    
         calcul=str(eval(calcul))
         text_resultat.delete(1.0,"end")
         text_resultat.insert(1.0,calcul)

    
    except:
        effacer_ecran()
        text_resultat.insert(1.0, "Erreur")

def effacer_ecran():
    global calcul
    calcul=""
    text_resultat.delete(1.0,"end ")

ecran=tk.Tk()
ecran.geometry("300x275")

text_resultat=tk.Text(ecran, height=2, width=16, font=('arial',24))
text_resultat.grid(columnspan=5)

btn_1=tk.Button(ecran,text="1",command=lambda:ajout_calcul(1),width=5, font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(ecran,text="2",command=lambda:ajout_calcul(2),width=5, font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(ecran,text="3",command=lambda:ajout_calcul(3),width=5, font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(ecran,text="4",command=lambda:ajout_calcul(4),width=5, font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(ecran,text="5",command=lambda:ajout_calcul(5),width=5, font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(ecran,text="6",command=lambda:ajout_calcul(6),width=5, font=('Arial',14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(ecran,text="7",command=lambda:ajout_calcul(7),width=5, font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(ecran,text="8",command=lambda:ajout_calcul(8),width=5, font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(ecran,text="9",command=lambda:ajout_calcul(9),width=5, font=('Arial',14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(ecran,text="0",command=lambda:ajout_calcul(0),width=5, font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_open=tk.Button(ecran,text="-",command=lambda:ajout_calcul("-"),width=5, font=('Arial',14))
btn_open.grid(row=5,column=1)

btn_close=tk.Button(ecran,text="/",command=lambda:ajout_calcul("/"),width=5, font=('Arial',14))
btn_close.grid(row=5,column=3)

btn_som=tk.Button(ecran,text="+",command=lambda:ajout_calcul("+"),width=5, font=('Arial',14))
btn_som.grid(row=2,column=5)

btn_mult=tk.Button(ecran,text="x",command=lambda:ajout_calcul("*"),width=5, font=('Arial',14))
btn_mult.grid(row=3,column=5)

btn_egal=tk.Button(ecran,text="=",command=eval_calcul,width=5, font=('Arial',14))
btn_egal.grid(row=4,column=5)

btn_effacer=tk.Button(ecran,text="/",command=effacer_ecran,width=5, font=('Arial',14))
btn_effacer.grid(row=5,column=5)

ecran.mainloop()