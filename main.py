import tkinter
from tkinter import *

screen = Tk()
screen.title("BMI Calculator")
screen.geometry("400x300")
screen.config(pady=40)

#Age + Gender + Height + Weight Label
def screen_label():
    label1 = Label(screen, text="ages: 2-120", width=15, height=2).grid(row=0, column=3),
    label2 = Label(screen, text="Age", width=15, height=2).grid(row=0),
    label3 = Label(screen, text="Gender", width=20, height=2).grid(row=1),
    label4 = Label(screen, text="Height", width=20, height=2).grid(row=2),
    label5 = Label(screen, text="Weight", width=20, height=2).grid(row=3),

#Male + Female Checkbutton
def screen_Checkbutton():
    var1 = IntVar()
    var2 = IntVar()
    Checkbutton(screen, text="Male", variable=var1).place(x=150, y=40)
    Checkbutton(screen, text=" Female", variable=var2).place(x=220, y=40)



def calculate_start():
    height = e_height.get()
    weight= e_weight.get()
    if height == "" or weight == "":
        result_label.config(text="Please enter a number")
    else:
        try:
            # Hata olabileceğini düşündüğünüz kod bloğu
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = bmi_class(bmi)
            result_label.config(text = result_string)
        except:
            # Hatanın türüne göre uygun bir işlem yapılır
            result_label.config(text="Enter a valid number!")
def calculate_clear():
    e_age.delete(0, END),
    e_height.delete(0, END),
    e_weight.delete(0, END)

def age_if(new_value):
    if new_value.isdigit() and 2 <= int(new_value) <= 120:
        return True
    else:
        return False

validation = screen.register(age_if)

#Entry
e_age = Entry(screen, width=22,validate="key", validatecommand=(validation , "%P") )
e_height = Entry(screen, width=22)
e_weight = Entry(screen, width=22)

e_age.grid(row=0, column=1)
e_height.grid(row=2, column=1)
e_weight.grid(row=3, column=1)


#Calculate Start + Clear Button
start_button = Button(screen, text="Calculate", bg="green", fg="white", width=15, height=2, command=calculate_start).place(x=130, y=150)
clear_button = Button(screen, text="Clear", bg="grey", fg="white", width=5, height=2, command=calculate_clear).place(x=260, y=150)
result_label = tkinter.Label()
result_label.place(x=120, y=210)

def bmi_class(bmi):
    result_string = f"Your BMI: {round(bmi,2)}. You are "
    if bmi < 16:
        result_string += "Severe Thinness"
    if 16 < bmi <= 17:
        result_string += "Moderate Thinness"
    if 17 < bmi <= 18.5:
        result_string += "Mild Thinness"
    if 18.5 < bmi <= 25:
        result_string += "Normal"
    if 25 < bmi <= 30:
        result_string += "Overweight"
    if 30 < bmi <= 35:
        result_string += "Obese Class I"
    if 35 < bmi <= 40:
        result_string += "Obese Class II"
    if bmi > 40:
        result_string += "Obese Class III"

    return result_string

screen_Checkbutton()
screen_label()
screen.mainloop()