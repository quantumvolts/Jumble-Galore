from tkinter import *
from random import choice
from random import shuffle

win = Tk()
win.title('Jumble Galore')
win.geometry("600x400+-1900+100")

my_label = Label(win, text="", font=("Helvetica", 48))
my_label.pack()

def shuffler():
    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text='')
    
    # List of state words
    states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska']

    # Pick random state from list
    global word
    word = choice(states)
    my_label.config(text=word)

    # Break apart chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)
    print(break_apart_word)

    # Turn shuffeled list into a word
    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter

    my_label.config(text=shuffled_word)

# Create answer function
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
    else:
        answer_label.config(text="Incorrect!!")

entry_answer = Entry(win, font=("Helvetica", 24))
entry_answer.pack(pady=20)

button_frame = Frame(win)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
my_button.grid(row=0, column=0, padx=10)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1, padx=10)

answer_label = Label(win, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

shuffler()
win.mainloop()