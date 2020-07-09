##              Ankusha has a menu designed which displays
##              the start button, a howto button and a credits button.
##              Click on the button, with symbol '?' for understanding how the game/app goes about
from tkinter import *
from PIL import ImageTk,Image
from time import *
from remove import *

##  Removing pygame print statement
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']=''

import pygame

##  Starting pygame
pygame.mixer.init()
Ankusha_theme=pygame.mixer.music

##  Running a check for any corrupted files
qs=open("All_questions.txt","r")
all_questions=[i.strip() for i in qs]
qs.close()

ms=open("All_movies.txt","r");
all_movies=[i.strip() for i in ms]
ms.close()

movie_names=[i[0:i.index(':')] for i in all_movies]
movie_patterns=[i[i.index(':')+1:] for i in all_movies]

##  Creating error if corrupt file is found
class CorruptFileFound(Exception):
    pass

##  Error message
message='File is corrupted. Contact Black Soil Technology at +91 90086 08043 for more details.'

if(len(all_questions)!=21):
    raise CorruptFileFound(message)
    exit(1)

for i in range(0,len(movie_patterns)):
    for j in range(0,len(movie_patterns[i])):
        if(movie_patterns[i][j] not in ['Y',',','N']):
            raise CorruptFileFound(message)
            exit(1)
        if(len(movie_patterns[i][j])>1):
            raise CorruptFileFound(message)
            exit(1)
    if(len(without(movie_patterns[i],','))!=20):
        raise CorruptFileFound(message)
        exit(1)
    if(len(without(movie_patterns[i],['Y','N']))!=19):
        raise CorruptFileFound(message)
        exit(1)

##  Program begins
if 'HIDE-GREET-MESSAGE' not in os.environ:
    print("A product of Black Soil Technology (B.S.T). Contact +91 90086 08043 for any queries.")

##  Creating and orienting the interface
root=Tk()
root.title("Ankusha- The mind reader")
root.configure(background="black",bd=None)
root.resizable(0,0)
width,height=Image.open("Ankusha_intro.png").size
root.geometry(str(width)+'x'+str(height))

## Starting the music
Ankusha_theme.load('Ankusha_theme.mp3')
Ankusha_theme.play(-1)

##  Creating the graphics
canvas=Canvas(root,width=width,height=height)
canvas.pack()
backgnd=PhotoImage(file="Ankusha_intro.png")
canvas.create_image(0,0,anchor=NW,image=backgnd)
action_buttonsimg=PhotoImage(file="action_buttons.png")

def Ankusha():
##  Function to start the main program    
    time=open('Time.txt','w')
    time.write(str(Ankusha_theme.get_pos()))
    time.close()
    root.destroy()
    import Ankusha

def back():
##  Closing the howto window or the credit window (depends on circumstance)
    action_button_start.place(x=280,y=250)
    action_button_howto.place(x=280,y=340)
    action_button_credits.place(x=280,y=430)
    canvas.delete('?')
    ok_button.place_forget()
    
def howto():
##  Function that displays how to use the app on boolean state 0, and displays credits on boolean state 1    
    global ok_button,state,pic_state

    howto=''
    if(state==0):
        howto=open('Howto.txt','r')
    elif(state==1):
        howto=open('credits.txt','r')
        pic_state=1
        state=0

    howto=howto.read()
    Howto=PhotoImage(file="Howto.png")
    canvas.create_image(450,340,image=Howto,tags='?')
    canvas.create_text(450,320,text=howto,font='Gabriola 15 bold',tags='?')
    canvas.backgnd=Howto

    if(pic_state==1):
        logo=PhotoImage(file='logo.png')
        canvas.create_image(320,320,image=logo,tags='?')
        canvas.Howto=logo
        pic_state=0

    action_button_start.place_forget()
    action_button_howto.place_forget()
    action_button_credits.place_forget()
    ok_button=Button(root,image=ok_buttonimg,bd=0,bg="Black",text='Back',compound="center",font='Gabriola 10 bold',command=back)
    ok_button.place(x=400,y=510)

def credits():
##  Changing boolean value
    global state
    
    state=1
    howto()

def quitt(event):
##  Exiting the program
    if(event.char.lower()=='q'):
        Ankusha_theme.stop()
        exit(0)
        
def stop_music():
##  Halting the music    
    Ankusha_theme.stop()
    root.destroy()

##  Creating the buttons    
action_button_start=Button(root,image=action_buttonsimg,bd=0,bg="Black",text='Start',compound="center",font='Gabriola 20 bold',command=Ankusha)
action_button_start.place(x=280,y=250)
action_button_howto=Button(root,image=action_buttonsimg,bd=0,bg="Black",text='?',compound="center",font='Gabriola 20 bold',command=howto)
action_button_howto.place(x=280,y=340)
action_button_credits=Button(root,image=action_buttonsimg,bd=0,bg="Black",text='Credits',compound="center",font='Gabriola 20 bold',command=credits)
action_button_credits.place(x=280,y=430)
ok_buttonimg=PhotoImage(file="ok_button.png")

root.bind('<KeyPress>',quitt)
root.protocol('WM_DELETE_WINDOW',stop_music)

##  Few necessary initializations
state=0
pic_state=0

root.mainloop()
