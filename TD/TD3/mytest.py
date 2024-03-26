from tkinter import*
import tkinter as ttk
from turtle import*

# creation d'un fenetre
window = Tk()

# nommer l'interface
window.title("Interface graphique")

# limiter la taille de la fenetre
window.geometry("500x400")
window.configure(bg="white")
 
# creation d'un frame 
frame0 = ttk.Frame(window)
frame0.grid()

# création d'un canvas bg

#canvas = Canvas(frame0)
#canvas.grid()

#def create_cercle(x1,x2,y1,y2):



def modification():
    Lescouleurs = Variable
    Lescouleurs = ['white', 'red','yellow', "green",'lightpink', 'lightblue']
# Label 1, du nom de l'utilisateur
label1 = Label(frame0, text="Name : ", font="cursive")
label1.grid(row=0,column=0)
# Entry 1, pour écrire le nom de l'utilisateur
user =  Entry(frame0, text="Your Name", border= "5px")
user.grid(row=0, column=1)

# Label 2, du mot de passe 
label2 = Label(frame0, text="Password : ", font="cursive")
label2.grid(row=1,column=0)

# Entry 1, pour écrire le mot de passe de l'utilisateur
password =  Entry(frame0, text="Your password", border = "5px" )
password.grid(row=1, column=1)

# Un lien pour réins
c1 = Label(frame0, text="Forgot password ?", fg="blue")
c1.grid(row= 2, column=1)

# Première button pour valider
btn = Button(frame0,text = "Valider")
btn.grid(row=3, column= 1)

# Deuxième button pour annuler
btn = Button(frame0,text = "Annuler")
btn.grid(row = 3, column=2)

window.mainloop()