from tkinter import *
import random
global num
num = int(random.randrange(1, 10))

#click function def
def click():
    try:
        print(num)
        int(guess.get())
        guessed_num = int(guess.get())
        if guessed_num > 10 or guessed_num < 1:
            answer.config(text="This number can not be selected.\nPlease select a number within the given range.", bg="pink", fg="white")
        else:
            if num > guessed_num:
                answer.config(text="The number you selected is lower than the generated one.", bg="pink", fg="white" )
            elif num < guessed_num:
                answer.config(text="The number you selected is greater than the generated one.", bg="pink", fg="white")
            if num == guessed_num:
                answer.config(text="Congratulations! You guessed the number.", bg="pink", fg="white")

    except ValueError:
        answer.config(text="Please enter a number.", bg="pink", fg="white")

#window
window = Tk()
window.title("Guess the number game.")
window.configure(bg="pink")

#main label
Label1 =Label (window, text="Guess a number between 1 and 10.", bg="pink", fg="white", font="none")#.grid(row=0, column=0, sticky=W)
Label1.pack()


#guess = int(input("Guess a number between 1 and 10."))
guess = Entry(window, width=20, bg="white")
guess.pack()#.grid(row=2, column=0, sticky=W)

#submit button
Button1=Button(window, text="Guess it", width=8, command=click)#.grid(row=3, column=0, sticky=W)
Button1.pack()
#answers
answer = Label(window, text='')
answer.pack()

window.mainloop()