from tkinter import *
import datetime

# -------------------- Functions ---------------------

def date_time():
    now = datetime.datetime.now()

    hr = now.strftime("%I")
    mi = now.strftime("%M")
    se = now.strftime("%S")
    am = now.strftime("%p")

    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    day = now.strftime("%a")

    label_hr.config(text=hr)
    label_min.config(text=mi)
    label_sec.config(text=se)
    label_scale.config(text=am)

    label_date.config(text=date)
    label_mon.config(text=month)
    label_year.config(text=year)
    label_day.config(text=day)

    label_hr.after(1000, date_time)  # ✅ FIXED


dig = Tk()
dig.title("***Digital Clock***")
dig.geometry("1000x500")
dig.config(bg="#1e1b4b")

# -------- Time Labels --------
label_text=Label(dig,text="“Built with Python & Tkinter”",font=("Time New Roman","20","bold"),bg="#1e1b4b")
label_text.place(x=300,y=5,height=40,width=400)

label_hr = Label(dig, text="00", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_hr.place(x=120, y=40, height=110, width=100)
Label(dig, text="Hour", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=120, y=170, height=40, width=100)

label_min = Label(dig, text="00", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_min.place(x=340, y=40, height=110, width=100)
Label(dig, text="Min", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=340, y=170, height=40, width=100)

label_sec = Label(dig, text="00", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_sec.place(x=560, y=40, height=110, width=100)
Label(dig, text="Sec", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=560, y=170, height=40, width=100)

label_scale = Label(dig, text="AM", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_scale.place(x=780, y=40, height=110, width=100)
Label(dig, text="AM/PM", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=780, y=170, height=40, width=100)

# -------- Date Labels --------

label_date = Label(dig, text="00", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_date.place(x=120, y=300, height=100, width=100)
Label(dig, text="Date", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=120, y=420, height=50, width=100)

label_mon = Label(dig, text="00", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_mon.place(x=340, y=300, height=100, width=100)
Label(dig, text="Month", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=340, y=420, height=50, width=100)

label_year = Label(dig, text="00", font=("Times New Roman", 50, "bold"), bg="#312e81")
label_year.place(x=560, y=300, height=100, width=100)
Label(dig, text="Year", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=560, y=420, height=50, width=100)

label_day = Label(dig, text="Mon", font=("Times New Roman", 60, "bold"), bg="#312e81")
label_day.place(x=780, y=300, height=100, width=100)
Label(dig, text="Day", font=("Times New Roman", 30, "bold"), bg="#312e81").place(x=780, y=420, height=50, width=100)

date_time()
dig.mainloop()
