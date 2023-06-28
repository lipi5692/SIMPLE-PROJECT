from tkinter import *
screen=Tk()
screen.title("GAME")
screen.geometry("500x450")
Label(screen,text="This is GAME(snake,water,gun)",font="ariel 20 bold",bg="yellow",fg="black").pack(fill="both")
from PIL import ImageTk,Image
print("This is GAME(snake,water,gun)")
you=0
comp=0
for i in range(1,11):
    print("Turn",i)
    List=["SNAKE","WATER","GUN"]
    m="Computer Win!!"
    n="You Win!!"
    import random
    b=random.randint(0,2)
    a=input("Enter your choice:")
    if a.upper() == "SNAKE":
        img = Image.open("C:/Users/asus/Downloads/snake.jfif")
        img = img.resize((50, 50))
        my = ImageTk.PhotoImage(img)
        label = Label(screen, image=my).place(x=240, y=50)
    print("YOU :",a.upper(),end=" , ")
    print("COMPUTER :",List[b])
    if a.upper()==List[b]:
        print("Draw both are same choice")
    if a.upper()==List[0] and List[b]==List[1]:
        print(n)
        you=you+1
    if a.upper()==List[1] and List[b]==List[0]:
        print(m)
        comp=comp+1
    if a.upper()==List[0] and List[b]==List[2]:
        print(m)
        comp=comp+1
    if a.upper()==List[2] and List[b]==List[0]:
        print(n)
        you=you+1
    if a.upper()==List[1] and List[b]==List[2]:
        print(n)
        you=you+1
    if a.upper() == List[2] and List[b] == List[1]:
        print(m)
        comp=comp+1
if you > comp:
    print("Congrats\n You Win this match","your score is",you,"/10","your Opponent Score is:",comp,"/10")
elif you==comp:
    print("GAME DRAW both have same score, And your score is:",you,"computer score is:",comp)
else:
        print(" You Lost this match","your score is",you,"/10","your Opponent Score is:",comp,"/10")
mainloop()
    
