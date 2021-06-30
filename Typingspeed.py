words=['Grapes','Mango','Apple','door','Laptop']




def labelSlider():
    global count,sliderwords
    text='welcome to typing speed increaser game'
    if(count>=len(text)):
        count=0
        sliderwords =''
    sliderwords=sliderwords+text[count]
    count+=1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelSlider)



def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timeLableCount.configure(fg='red')
    if (timeleft>0):
        timeleft-=1
        timeLableCount.configure(text=timeleft)
        timeLableCount.after(1000,time)
    else:
        gamePlayDetaillabel.configure(text='Score={},Miss={}, Total Score={}'.format(score,miss,score-miss))
        retry=messagebox.askretrycancel('Notification','For play game again retry button')
        if(retry==True):
            score=0
            timeleft=60
            miss=0
            timeLableCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

        
def  startGame(event):
    global score,miss
    if(timeleft==60):
        time()
    gamePlayDetaillabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)



from tkinter import *
import random
from tkinter import messagebox

root= Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing Speed Increaser Game')
root.iconbitmap('typingspeed.ico')


score=0
timeleft=60
count=0
sliderwords=''
miss=0

fontLabel=Label(root,text='',font=('times new roman',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel=Label(root,text=words[0],font=('times new roman',25,'italic bold'),bg='powder blue')
wordLabel.place(x=350,y=200)

scoreLabel=Label(root,text='Your Score:',font=('times new roman',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=('times new roman',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=180)


timeLableCount=Label(root,text=timeleft,font=('times new roman',25,'italic bold'),bg='powder blue',fg='blue')
timeLableCount.place(x=600,y=100)

gamePlayDetaillabel=Label(root,text='Type word and hit Enter Button',font=('times new roman',25,'italic bold'),bg='powder blue',fg='black')
gamePlayDetaillabel.place(x=120,y=450)
wordEntry=Entry(root,font=('times new roman',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()


root.bind('<Return>',startGame)


root.mainloop()
