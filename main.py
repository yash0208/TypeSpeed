from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('800x600+300+50')
root.title('Typing Speed Game')
root.configure(bg='#191c2f')
words = ['Lorem','Ipsum','simply','dummy','close', 'into','me', 'well', 'been', 'car', 'his', 'family', 'little', 'might', 'sometimes', 'have', 'by', 'away','change', 'new', 'its', 'always', 'these', 'play', 'good', 'there', 'world', 'group', 'together', 'men', 'come', 'say', 'who','stop','printing','typesetting','cleavercode','ostrich','industry','essentially','software','versions ']
random.shuffle(words)

def welcomeLabel():
    global count,sliderWord
    text = 'Welcome To Typing Speed Testing Game'
    if(count >= len(text)):
        count=0
        sliderWord=''
    sliderWord += text[count]
    count += 1
    titleLabel.configure(text=sliderWord)
    titleLabel.after(150,welcomeLabel)


def startGame(event):
    global score,miss
    if(timeLeft == 60):
        time()
    gamePlayDetailLabel.configure(text='Enjoy The Game')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreCountLabel.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

def time():
    global timeLeft,score,miss
    if(timeLeft >=11):
        pass
    else:
        timeCountLabel.configure(fg='red')
    if(timeLeft >0):
        timeLeft -= 1
        timeCountLabel.configure(text=timeLeft)
        timeCountLabel.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        notific = messagebox.askretrycancel('Notification','For Play Again Please Hit The Retry Button!')
        if(notific==True):
            score=0
            timeLeft=60
            miss=0
            timeCountLabel.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)

score = 0
miss = 0
timeLeft = 60
count = 0
sliderWord = ''

titleLabel = Label(root,text='',bg='#191c2f',fg='white',font=('Gilroy',30,'bold'),width=33)
titleLabel.place(x=10,y=10)
welcomeLabel()

scoreLabel = Label(root,text='Your Score :',bg='#191c2f',fg='white',font=('Helvetica',25,'bold'))
scoreLabel.place(x=10,y=100)
scoreCountLabel = Label(root,text=score,bg='#191c2f',fg='white',font=('Helvetica',25,'bold'))
scoreCountLabel.place(x=80,y=150)

timeLabel = Label(root,text='Time Left :',bg='#191c2f',fg='White',font=('Helvetica',25,'bold'))
timeLabel.place(x=570,y=100)
timeCountLabel = Label(root,text=timeLeft,bg='#191c2f',fg='White',font=('Helvetica',25,'bold'))
timeCountLabel.place(x=680,y=150)

wordLabel = Label(root,text=words[0],bg='#191c2f',fg='white',font=('Helvetica',25,'bold'))
wordLabel.place(x=320,y=220)


wordEntry = Entry(root,font=('Helvetica',25,'bold'),bd=10,justify='center')
wordEntry.place(x=200,y=300)
wordEntry.focus_set()



gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',bg='#191c2f',fg='White',font=('arial',15,'italic bold'))
gamePlayDetailLabel.place(x=220,y=450)

root.bind('<Return>',startGame)
root.mainloop()