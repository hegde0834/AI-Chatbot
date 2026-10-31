from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.configure(bg="white")

def ask():
    user_val = speech_to_text.speech_to_text()
    if not user_val:
        return
    bot_val = action.Action(user_val)
    reply_box.insert(END, "User ----> " + user_val + "\n")
    if bot_val is not None:
        reply_box.insert(END, "Bot <---- " + str(bot_val) + "\n")
    if bot_val == "ok bye":
        root.destroy()
def send():
    user_val = question_box.get("1.0", END).strip()
    if not user_val:
        return
    bot_val = action.Action(user_val)
    reply_box.insert(END, "User ----> " + user_val + "\n")
    if bot_val is not None:
        reply_box.insert(END, "Bot <---- " + str(bot_val) + "\n")
    question_box.delete("1.0", END)
    if bot_val == "ok bye":
        root.destroy()
def del_text():
    reply_box.delete("1.0", END)

frame = LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised",bg="#6F8FAF")
frame.place(x=95, y=20)

text_label = Label(frame,text="AI Assistant",font=("Comic Sans MS", 14, "bold"),bg="#356696",fg="white")
text_label.grid(row=0, column=0, pady=10)

img = Image.open(r"C:/Users/hegde/PycharmProjects/PythonProject8/AI.png")
img = img.resize((150, 150))

image = ImageTk.PhotoImage(img)
image_label = Label(frame,image=image,bg="#6F8FAF")
image_label.grid(row=1, column=0, pady=10)
image_label.image = image

reply_box = Text(root,font=("Courier", 10, "bold"),bg="#356696",fg="white",bd=3)
reply_box.place(x=95, y=300, width=370, height=100)

question_box = Text(root,font=("Courier", 10),bd=2)
question_box.place(x=95, y=430, width=370, height=50)

ask_btn = Button(root,text="ASK",font=("Arial", 10, "bold"),bg="#356696",fg="white",command=ask)
ask_btn.place(x=95, y=530, width=110, height=35)

delete_btn = Button(root,text="DELETE",font=("Arial", 10, "bold"),bg="#356696",fg="white",command=del_text)
delete_btn.place(x=220, y=530, width=110, height=35)

send_btn = Button(root,text="SEND",font=("Arial", 10, "bold"),bg="#356696",fg="white",command=send)
send_btn.place(x=345, y=530, width=110, height=35)

root.mainloop()