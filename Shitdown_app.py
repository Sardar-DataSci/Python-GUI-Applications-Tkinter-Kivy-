from tkinter import *
import os

def restart():
     os.system("sudo shutdown -r now")
def restart_time():    
    os.system("sudo shutdown -r +0.33")
def logout():
    os.system("osascript -e 'tell application \"System Events\" to log out'")
def shutdown():
    os.system("sudo shutdown -h now")   

st=Tk()
st.title("Mac Power App by Pyhton")
st.geometry("500x500")
st.config(bg="Red")
r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),
                relief=RAISED,cursor="plus",command=restart())

r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",30,"bold"),
                 relief=RAISED,cursor="plus",command=restart_time())
rt_button.place(x=150,y=170,height=50,width=200)


logout_button=Button(st,text="Logout",font=("Time New Roman",30,"bold"),
                     relief=RAISED,cursor="plus",command=logout())
logout_button.place(x=150,y=270,height=50,width=200)

shutdown_button=Button(st,text="Shutdown",font=("Time New Roman",30,"bold"),
                       relief=RAISED,cursor="plus",command=shutdown())

shutdown_button.place(x=150,y=370,height=50,width=200)



st.mainloop()