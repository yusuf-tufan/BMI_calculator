from tkinter import *
from PIL import ImageTk, Image

window=Tk()
window.title("BMI Calculator")
window.configure(bg='#ffffca')
window.minsize(width=1400,height=1080)

#image
img = Image.open("BMI index1.jpg")
resized=img.resize((550,400),Image.Resampling.LANCZOS)
itk=ImageTk.PhotoImage(resized)
lbl=Label(window,image=itk)
lbl.image=itk
lbl.place(x=130,y=30)

def bmi_calcualte():

    user_kg=scale_kg.get()
    user_cm=scale_cm.get()

    #control Error
    try:
        user_kg=int(user_kg)
        user_cm=int(user_cm)
    except:
        lb = Label(window, text='Enter True Informations...')
        lb.config(width=50, height=5, bg='red', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)
        return

    bmi1=user_kg / ((user_cm/100) * (user_cm/100))

    #situations
    if 0<bmi1 <= 18.4:
        lb = Label(window, text=f'Underweight\nYour BMI : {'%.2f' % bmi1}\nLOW')
        lb.config(width=50,height=5, bg='light blue', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

    elif 18.5<=bmi1<=24.9:
        lb = Label(window, text=f'Normal\nYour BMI : {'%.2f' % bmi1}\nIDEAL')
        lb.config(width=50,height=5, bg='limegreen', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

    elif 24.91<= bmi1<=29.9:
        lb = Label(window, text=f'Overweight\nYour BMI : {'%.2f' % bmi1}\nHİGH')
        lb.config(width=50,height=5, bg='yellow', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

    elif 30.01<=bmi1<=39.9:
        lb = Label(window, text=f'Obese\nYour BMI : {'%.2f' % bmi1}\nVERY HİGH')
        lb.config(width=50,height=5, bg='dark orange', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

    elif 120>bmi1 >=40.0:
        lb = Label(window, text=f'Morebidly Obese\nYour BMI : {'%.2f' % bmi1}\nEXTREMELY HİGH')
        lb.config(width=50,height=5, bg='red', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

    else:
        lb = Label(window, text='Enter Right Informations!')
        lb.config(width=50,height=5, bg='red', fg='black', font=('Arial', 11, 'bold', 'italic'))
        lb.place(x=700, y=250)

#kg text
kg_label=Label(text='Enter In Your Weight(kg):',bg='light green',fg='black',font=("Arial",11,'italic'))
kg_label.place(x=700,y=100)

#cm text
cm_label=Label(text='Enter In Your Height(cm):',bg='light green',fg='black',font=("Arial",11,'italic'))
cm_label.place(x=700,y=150)


enter_size=StringVar()
#enter kg
scale_kg=Entry(width=10,textvariable=enter_size)
scale_kg.config(bg='light green',font=('Arial',11,'bold','italic'))
scale_kg.focus()
scale_kg.place(x=885,y=101)

enter_len=StringVar()
#enter cm
scale_cm=Entry(width=10,textvariable=enter_len)
scale_cm.config(bg='light green',font=('Arial',11,'bold','italic'))
scale_cm.place(x=885,y=151)

#control enteries limit
def character_limit(enter_size):
    if len(enter_size.get())>3:
        enter_size.set('')
enter_size.trace('w',lambda *args: character_limit(enter_size))

def character_size(enter_len):
    if len(enter_len.get())>3:
        enter_len.set('')
enter_len.trace('w',lambda *args: character_size(enter_len))


#button
calculator_button=Button(text='Calculate BMI',bg='orange',font=('Arial',11,'italic'),command=bmi_calcualte)
calculator_button.config(width=30)
calculator_button.place(x=700,y=190)


window.mainloop()