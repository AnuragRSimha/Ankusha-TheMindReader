##          Ankusha is a program developed with a pattern matching algorithm. A movie is to be kept in the mind, and then a set of Yes-No questions
##          are displayed. The iteration goes on up to five questions, and the movie is guessed by the program. If the movie is not guessed properly,
##          the iteration continues upto the next five questions. This cycle goes on up till a limit of twenty-one questions.

from tkinter import *
from PIL import ImageTk,Image
from time import *
from random import *
import pygame
import os
from time import *

##  Starting the music
pygame.mixer.init()
Ankusha_theme=pygame.mixer.music
other_music=pygame.mixer
oth_msc_bool=0
Ankusha_theme.load('Ankusha_theme.mp3')
time_n=open("Time.txt",'r')
time=time_n.read()
time_n.close()
os.remove('Time.txt')
Ankusha_theme.play(-1,(int(time)+5000)/5000)

##  Orienting the size
root=Tk()
root.title("Ankusha- The mind reader")
root.configure(background="black",bd=None)
root.resizable(0,0)
width,height=Image.open("Ankusha_background.png").size
root.geometry(str(width)+'x'+str(height))

##  Creating the background and placing the character
canvas=Canvas(root,width=width,height=height)
canvas.pack()
backgnd=PhotoImage(file="Ankusha_background.png")
canvas.create_image(0,0,anchor=NW,image=backgnd)
q1toq5img=PhotoImage(file="q1toq5.png")
canvas.create_image(450,350,image=q1toq5img,tags="mr")
canvas.backgnd=q1toq5img
spch_bub=PhotoImage(file="Speech_bubble.png")
canvas.create_image(600,220,image=spch_bub,tags="sb")
canvas.backgnd=spch_bub
questions=Label(root,bg="white",font=("Gabriola",13),justify=LEFT,anchor='w',wraplength=283)
questions.place(x=560,y=130)

def get_ansY():
##  Function called on click of 'Yes'
    global answer
    global i
    global all_questions
    
    other_music.Sound('Yes.wav').play().set_volume(0.25)
    
    try:
        if(i!=limit):
            i+=1
            questions.configure(text=str(i+1)+'. '+all_questions[i])
            answer.append('Y')

        else:
            movie()

    except:
        update_movie()

def get_ansN():
##  Function called on click of 'No'
    global answer
    global i
    global all_questions,nq

    other_music.Sound('No.wav').play().set_volume(0.25)

    try:
        if(i!=limit):
            if(nq==1):
                questions.configure(text=str(i+1)+'. '+all_questions[i])

            elif(nq==0):
                i+=1
                questions.configure(text=str(i+1)+'. '+all_questions[i])
                answer.append('N')
            nq=0

        else:
            movie()
            
    except:
        update_movie()

def conf_movieY():
##  Control transferred from get_ansY() to this function for the answer_Y button 
    global Ankusha_earnings,new_Ankusha_earnings

    other_music.Sound('Yes.wav').play().set_volume(0.25)
    answer_y.place_forget()
    answer_n.place_forget()
    final_stage0img=PhotoImage(file="final_stage0.png")
    canvas.create_image(450,350,image=final_stage0img,tags="mr")
    canvas.backgnd=final_stage0img
    moviebox.place_forget()
    questions.configure(text="It was nice spending time with you. I deeply hope we maintain this friendly bond between us. Nevertheless, there are instances where I too can fail. Bye for now.")
    money_earned=randrange(0,501)

    Ankusha_earnings=int(Ankusha_earnings)
    Ankusha_earnings+=money_earned
    Ankusha_earnings=str(Ankusha_earnings)
    earnings=open('Ankusha_earnings.txt','w')
    earnings.write(Ankusha_earnings)
    earnings.close()

    new_Ankusha_earnings=money()
    canvas.delete('ae')
    canvas.create_text(812+len(Ankusha_earnings),40,font="Gabriola 15",text=new_Ankusha_earnings,tags='ae')
    close = lambda event:quitt() if(event.char.lower()!='') else None
    root.bind('<KeyPress>',close)
def conf_movieN():
##  Control transferred from get_ansN() to this function for the answer_N button
    global limit,lim1,lim2,flag,i,nq,all_the_movie_list,pos

    other_music.Sound('No.wav').play().set_volume(0.25)
    pos+=1

    if(pos<=len(all_the_movie_list)-1):
        questions.configure(text="You thought of "+all_the_movie_list[pos]+"?")

    else:
        if(limit<=20):
            answer=[]
            flag=0
            limit+=5
            lim1+=10
            lim2+=10
            nq=1
            answer_y.configure(command=get_ansY)
            answer_n.configure(command=get_ansN)
            get_ansN()

        if(i==20): 
            update_movie()

def movie():
##  Heart of the program, where all main events occur    
    global store,answer,flag,limit,lim1,lim2,all_the_movie_list,pos

    store+=answer
    all_the_movie_list=[]

    if(limit==5):
        canvas.delete("mr")
        q6toq10img=PhotoImage(file="q6toq10.png")
        canvas.create_image(450,350,image=q6toq10img,tags="mr")
        canvas.backgnd=q6toq10img

    elif(limit==10):
        canvas.delete("mr")
        q11toq15img=PhotoImage(file="q11toq15.png")
        canvas.create_image(450,350,image=q11toq15img,tags="mr")
        canvas.backgnd=q11toq15img

    elif(limit==15):
        canvas.delete("mr")
        q16toq20img=PhotoImage(file="q16toq20.png")
        canvas.create_image(450,350,image=q16toq20img,tags="mr")
        canvas.backgnd=q16toq20img

    for j in movie_patterns:
        if(j[lim1:lim2]==','.join(answer)[0:10]):
            flag=1
            all_the_movie_list.append(movie_names[movie_patterns.index(j)])

    pos=0

    if(flag==1 and len(all_the_movie_list)!=0):
        answer=[]
        questions.configure(text="You thought of "+all_the_movie_list[pos]+"?")
        answer_y.configure(command=conf_movieY)
        answer_n.configure(command=conf_movieN)

    elif(flag==0):
        if(limit<=20):
            answer=[]
            flag=0
            limit+=5
            lim1+=10
            lim2+=10
            answer_y.configure(command=get_ansY)
            answer_n.configure(command=get_ansN)

    else:
        if(i==20):
            update_movie()

def update_movie():
##  Function to update movie to the database
    global i,Ankusha_earnings,new_Ankusha_earnings,oth_msc_bool,click_value

    def nextstatement():
        global oth_msc_bool,click_value
        canvas.delete("mr")
        sad_stage2img=PhotoImage(file="sad_stage2.png")
        canvas.create_image(450,350,image=sad_stage2img,tags="mr")
        canvas.backgnd=sad_stage2img
        other_music.stop()
        Ankusha_theme.unpause()
        click_value=0
        music_button.configure(text='Music: Playing')
        oth_msc_bool=1
        questions.configure(text="...Yet, Ankusha loses no hopes. Please tell me the name of your movie.")
        nextbutton.place_forget()
        moviebox.place(x=560,y=190)

    def newmovie(event):
        new_movie=moviebox.get("1.0",END)
        if('_' in new_movie):
            new_movie=moviebox.get("1.0",'end-2c')
            state=1
            for j in movie_names:
                if(j==new_movie):
                    movie_patterns[movie_names.index(j)]=','.join(store)
                    state=0
            if(state==1):
                movie_names.append(new_movie)
                movie_patterns.append(','.join(store))
            all_movies=[]
            for j in movie_names:
                all_movies.append(j+':'+(movie_patterns[movie_names.index(j)]+'\n'))
            all_movies[-1]=all_movies[-1].strip()
            update_movies=open("All_movies.txt","w")
            for j in all_movies:
                update_movies.write(j)
            update_movies.close()
            moviebox.delete("1.0",END)
            moviebox.insert("1.0",new_movie)
            canvas.delete("mr")
            final_stage1img=PhotoImage(file="final_stage1.png")
            canvas.create_image(450,350,image=final_stage1img,tags="mr")
            canvas.backgnd=final_stage1img
            moviebox.place_forget()
            questions.configure(text="It was nice spending time with you. This failure, has overwhelmed me. Can I be a good mind reader, lest I work upon my mistakes. Bye.")
            close = lambda event:quitt() if(event.char.lower()!='') else None
            root.bind('<KeyPress>',close)

    answer_y.place_forget()
    answer_n.place_forget()
    canvas.delete("mr")
    sad_stage1img=PhotoImage(file="sad_stage1.png")
    canvas.create_image(450,350,image=sad_stage1img,tags="mr")
    canvas.backgnd=sad_stage1img
    Ankusha_theme.pause()
    other_music.Sound('Lost.wav').play()
    click_value=1
    music_button.configure(text='Music: Paused')
    questions.configure(text="Alas, I have lost. An outcome with such in-vein efforts, was unexpected to occur. I have failed to you...")
    oth_msc_bool=0
    money_cut=randrange(0,21)
    Ankusha_earnings=int(Ankusha_earnings)
    Ankusha_earnings-=money_cut

    if(Ankusha_earnings>-1):
        pass
    else:
        Ankusha_earnings=0

    Ankusha_earnings=str(Ankusha_earnings)
    earnings=open('Ankusha_earnings.txt','w')
    earnings.write(Ankusha_earnings)
    earnings.close()
    new_Ankusha_earnings=money()
    canvas.delete('ae')
    canvas.create_text(812+len(Ankusha_earnings),40,font="Gabriola 15",text=new_Ankusha_earnings,tags='ae')
    nextbutton=Button(root,image=button_image,font="Gabriola 10",bg="white",relief=FLAT,command=nextstatement,bd=0,text="Next",compound="center")
    nextbutton.place(x=668,y=190)
    root.bind('<KeyRelease>',newmovie)

def quitt():
##  Function to quit the program
    other_music.stop()
    Ankusha_theme.stop()
    root.destroy()
    os.environ['HIDE-GREET-MESSAGE']=''
    import Ankusha_menu

def music_toggle():
##  This is to pause or play the music
    global click_value,oth_msc_bool

    click_value+=1
    if(click_value%2==1):
        Ankusha_theme.pause()
        music_button.configure(text='Music: Paused')
    elif(click_value%2==0):
        Ankusha_theme.unpause()
        if(oth_msc_bool==0):
            other_music.stop()
        music_button.configure(text='Music: Playing')

def money():
##  Formatting of Ankusha's earning is done over here   
    global Ankusha_earnings,new_Ankusha_earnings

    if(int(Ankusha_earnings) in range(15001,90000)):
        new_Ankusha_earnings='15k+'
    elif(int(Ankusha_earnings)==15000):
        new_Ankusha_earnings='15k'
    elif(int(Ankusha_earnings) in range(90001,1000000)):
        new_Ankusha_earnings='90k+'
    elif(int(Ankusha_earnings)==90000):
        new_Ankusha_earnings='90k'
    elif(int(Ankusha_earnings)>1000000):
        new_Ankusha_earnings='1M+'
    elif(int(Ankusha_earnings)==1000000):
        new_Ankusha_earnings='1M'
    else:
        new_Ankusha_earnings=Ankusha_earnings
    return new_Ankusha_earnings

##  Creating the elements
button_image=PhotoImage(file="yesnobutton2.png")
answer_y=Button(root,image=button_image,font="Gabriola 10",bg="white",relief=FLAT,command=get_ansY,bd=0,text="Yes",compound="center")
answer_y.place(x=560,y=190)
answer_n=Button(root,image=button_image,font="Gabriola 10",bg="white",relief=FLAT,command=get_ansN,bd=0,text="No",compound="center")
answer_n.place(x=775,y=190)
back_image=PhotoImage(file="ok_button.png")
back_button=Button(root,image=back_image,font="Gabriola 10",bg="black",relief=FLAT,command=quitt,bd=0,text="Back",compound="center")
back_button.place(x=2,y=625)
moviebox=Text(root,font=("Gabriola",12),width=44,height=0)

##  File reading
qs=open("All_questions.txt","r")
all_questions=[i.strip() for i in qs]
qs.close()

ms=open("All_movies.txt","r");
all_movies=[i.strip() for i in ms]
ms.close()

movie_names=[i[0:i.index(':')] for i in all_movies]
movie_patterns=[i[i.index(':')+1:] for i in all_movies]

##  All initializations
limit=5
i=0
flag=0
lim1=0
lim2=9
nq=0
answer=[]
store=[]

##  Formatting some outputs
questions.configure(text='1. '+all_questions[0])
earns=PhotoImage(file="Ankusha_earnings.png")
canvas.create_image(807,35,image=earns)
canvas.backgnd=earns
coin=PhotoImage(file="coin.png")
canvas.create_image(790,40,image=coin)
canvas.backgnd=coin
canvas.create_text(808,17,font="Gabriola 15",text='Ankusha\'s earnings')

earnings=open('Ankusha_earnings.txt','r')
Ankusha_earnings=earnings.read()
earnings.close()
new_Ankusha_earnings=0
new_Ankusha_earnings=money()

canvas.create_text(812+len(Ankusha_earnings),40,font="Gabriola 15",text=new_Ankusha_earnings,tags='ae')
click_value=0
music_button=Button(root,image=back_image,font="Gabriola 10",bg="black",relief=FLAT,command=music_toggle,bd=0,text="Music: Playing",compound="center")
music_button.place(x=2,y=0)

root.protocol('WM_DELETE_WINDOW',quitt)
root.mainloop()
