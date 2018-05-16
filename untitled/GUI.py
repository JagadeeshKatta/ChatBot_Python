import os
import json
import tkinter
import random
import subprocess
from tkinter import *
import tkinter.scrolledtext as st


close_ui=["exit","close","quit","bye"]
#Method call happens upon hitting submit button from UI window during input text given by the user
def send_message():
    if len(scrolltxt.get("1.0", "end"))>1:
        chat.config(state=NORMAL)
        chat.insert(END, user + str(scrolltxt.get("1.0", "end")).replace("\n","")+"\n\n\t\t")
        messg = str(scrolltxt.get("1.0", "end")).replace("\n", "")
        chat.tag_add("newtag","1.0","end")
        chat.tag_configure("newtag", font='Helvetica 8 bold', foreground="#483d8b")
        chat.see(END)
        scrolltxt.delete("1.0", "end")
        chat.config(state=DISABLED)
        response(messg)
#Method call happens upon hitting enter during input text given by the user
def on_enter(event):
    if len(scrolltxt.get("1.0", "end")) > 1:
        chat.config(state=NORMAL)
        chat.insert(END, user + str(scrolltxt.get("1.0", "end")).replace("\n","")+"\n\n\t\t")
        messg = str(scrolltxt.get("1.0", "end")).replace("\n","").lower()
        chat.tag_add("newtag","1.0","end")
        chat.tag_configure("newtag", font='Helvetica 8 bold', foreground="#483d8b")
        chat.see(END)
        scrolltxt.delete("1.0", "end")
        chat.config(state=DISABLED)
        response(messg)

#Response giving by Bot to chatbox based on user input
def response(messag):
    global close_ui,top
    if messag in close_ui:
        top.quit()
    else:
        response_msg = check_msg(messag)
        chat.config(state=NORMAL)
        chat.insert(INSERT, bot+response_msg+"\n\n")
        chat.see(END)
        chat.config(state=DISABLED)

#Comparison whether input data exist in the given Json file or not
def check_msg(messg):
    filename="train_data"
    filename1 = "New_Data"
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
    if messg in datastore:
        if isinstance(datastore[messg], list):
            return random.choice(datastore[messg])
        else:
            if ".exe" in datastore[messg]:
                os.system("start "+datastore[messg])
                return "Task Completed!"
            else:
                return datastore[messg]
    else:
        if filename1:
            with open(filename1, 'w') as f:
                f.write(messg)
        return "Sorry! Not Trained on this but thanks for the new input!"


#Creating tkinter instance
top = tkinter.Tk()
top.title('Chat Bot')
#main window dimentions
top.geometry('300x350')
#Making main window to not resizable
top.resizable(False, False)
#pre-defined character names
user = "You : "
bot  = "Bot : "

#Canvas which showing Bog Image on top left most corner
canvas = tkinter.Canvas(width = 40, height = 35, bg = 'grey',bd="1")
canvas.place(x="",y="")
gif1 = tkinter.PhotoImage(file = "img/drib_blink_bot.gif")
canvas.create_image(20,20,image = gif1)
#ScrollBar or TextInput bar for user to enter inpu
scrollbar = Scrollbar(top)
scrollbar.place( x="274",y="45",height=250, width=15)
#Text box in the middle of chat screen
chat=tkinter.Text(top,height=15,width=30,yscrollcommand = scrollbar.set,background="#ffe4e1")
chat.config(state=DISABLED)
chat.place(x="30",y="45")
scrollbar.config( command = chat.yview )
#Wishing label on top just beside bot image
var = StringVar()
msg = tkinter.Message(top, textvariable=var, relief=RAISED,justify="left",width="200",bg="#8fbc8f",bd="3",font='Helvetica 8 bold')
var.set("...Hey!  How can I help you?")
msg.place(x="50",y="5")
#User Label name and configuration
label = tkinter.Label(top, text=user,fg="green",font='Helvetica 8 bold')
label.place(x="20", y="300")
#scrollText to enter data or input from user
scrolltxt = st.ScrolledText(wrap='word',font='Helvetica 8 bold')
scrolltxt.focus()
scrolltxt.bind('<Return>',on_enter)
scrolltxt.place(x="50", y="297", height=25, width=200)
#submit button to submit entered data to chat view
button = tkinter.Button(top, text="Submit", bg="orange",command=send_message,font='Helvetica 8 bold')
button.place(x="245", y="298")
#running main loop(UI execution starts from here)
top.mainloop()

