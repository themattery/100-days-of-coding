from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Ariel", 40, "italic")
LARGE_FONT = ("Ariel", 60, "bold")
current_card = {}
words_list = {}

# Fetching data
try:
    data = pandas.read_csv("data/words-to-learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    words_list = original_data.to_dict(orient="records")
else:
    words_list = data.to_dict(orient="records")

# ------------- FETCH RANDOM CARD ------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # Getting random words from data_dict
    current_card = random.choice(words_list)
    german_word = current_card["German"]
    # Putting word on word label
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=german_word, fill="black")
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
        canvas.itemconfig(card_background, image=card_back)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    words_list.remove(current_card)
    print(len(words_list))
    data = pandas.DataFrame(words_list)
    data.to_csv("data/words-to-learn.csv", index=False)

    next_card()
      
# ------------- USER UI ------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.attributes('-alpha', 0.9)

flip_timer = window.after(3000, flip_card)

# Flashcard Image
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 270, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Flashcard Text
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=(SMALL_FONT))
card_word = canvas.create_text(400, 280, text="Word", fill="black", font=(LARGE_FONT))

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, command=next_card)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, command=is_known)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
