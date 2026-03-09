from tkinter import *
import calendar

def calendar_see():
    window=Tk()
    window.title("Complete Year Calendar")
    window.geometry("1000x1000")
    window.config(background="light pink")

    get_year=int(year_entry.get())
    window_content=calendar.calendar(get_year)

    year_cal=Label(window,text=window_content,font=("Time New Roman","30","bold"))
    year_cal.grid(row=5,column=1,padx=20)

    window.mainloop()

root=Tk()
root.title("Calendar")
root.geometry("500x500")
root.config(background="gray")

name_label=Label(root,text="Calendar",font=("Time New Roman","40","bold"),bg="gray")
name_label.grid(row=1,column=1)

year_label=Label(root,text="Enter the Year",font=("Time New Roman","20","bold"),bg="gray")
year_label.grid(row=2,column=1)

year_entry=Entry(root,font=("Time New Roman","30","bold"),bg="gray")
year_entry.grid(row=3,column=1)

button_label=Button(root,text="Show Calendar",font=("Time New Roman","20","bold"),command=calendar_see)
button_label.grid(row=4,column=1)

root.mainloop()
