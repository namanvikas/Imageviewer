from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk


root=Tk()
root.title("image viewer")
root.geometry("600x400")
root.configure(background="light blue")


house_img=ImageTk.PhotoImage(Image.open("house.jpg"))
car_img=ImageTk.PhotoImage(Image.open("car.jfif"))



label_planet_name=Label(root,text=" planet : ",bg="lightblue")
label1_planet_name=Label(root,font=("courier",18,"bold"),bg="lightblue")
label_planet_image=Label(root,bg="gold2",highlightthickness=5,borderwidth=2,relief=SOLID)
label_gravity_radius=Label(root,font=("castellar"),bg="lightblue")
label_planet_info=Label(root,font=("courier",10,"bold"),bg="lightblue",wraplength=500)

planet=["house","car"]
selectedwal=StringVar()
dropdown=ttk.Combobox(root,values=planet,textvariable=selectedwal)


def planet_info():
  im=Image.open(img_path)
  
  img_roated=im.rotate(100)
  img = ImaheTk.PhotoImage(rotated_img)
  
  
dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)   
    
  
    
btn=Button(root,text="show planet info",command=planet_info)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)

label_planet_name.place(relx=0.2,rely=0.1,anchor=CENTER)
label1_planet_name.place(relx=0.5,rely=0.25,anchor=CENTER)
label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)
label_gravity_radius.place(relx=0.5,rely=0.8,anchor=CENTER)
label_planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()