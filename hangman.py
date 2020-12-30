import random
from hangman_art import *
from hangman_wordlist import word_list
print(logo)
word=random.choice(word_list)
print(len(word)*'_')
length=len(word)
print(word)
lives=6
display=[]

for char in word:
    display+="_"
end_of_game=False
while not end_of_game:
    letter=input('Guess the letter')
    if letter in display:
        print(f"You've already guessed the letter")
    for num in range(len(word)):
        if word[num]==letter:
            display[num]=letter
    if letter not in word:
        lives-=1
        if lives==0:
            end_of_game=True
            print('You loose')
        print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print('You Win')
