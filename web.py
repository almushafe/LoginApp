from customtkinter import *
from PIL import Image

app = CTk()
app.title("Login")
app.config(bg="white")
app.geometry("900x500+300+100")
app.resizable(False,False)

bg_image =CTkImage(dark_image=Image.open("bg1.jpg"),size=(500,500))

bg_lab =CTkLabel(app,image=bg_image,text="")
bg_lab.grid(row=0 , column=0,padx=10)

frame1 =CTkFrame(app,width=300,height=350,bg_color="white",fg_color="#D9D9D9",corner_radius=20)
frame1.grid(row=0,column=1,padx=30)

lab1 = CTkLabel(frame1,text="Welcome Back! \nLogin to Account",text_color="Black",font=("",35,'bold'))
lab1.grid(row=0 , column=0 , sticky="nw",pady=30,padx=10)

username= CTkEntry(frame1, width=200 , height=45,fg_color='black',corner_radius=15,placeholder_text="Username",placeholder_text_color="white",font=("",16,'bold'),text_color='white')
username.grid(row=1,column=0,sticky="nwe",padx=30)


pasword = CTkEntry(frame1,width=200,height=45,fg_color='black',corner_radius=15,placeholder_text="Username",placeholder_text_color="white",font=("",16,'bold'),text_color='white')
pasword.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)

cr_acc= CTkLabel(frame1,text="Create Account!",text_color="black",cursor="hand2",font=("",15))
cr_acc.grid(row=3,column=0,sticky="w",padx=40,pady=20)

login_btn = CTkButton(frame1, text="Login",text_color="white",font=("",15,"bold"),height=40,width=60,fg_color="#0085FF",corner_radius=15,cursor="hand2")
login_btn.grid(row=3,column=0,sticky="ne",padx=35,pady=20)
app.mainloop()