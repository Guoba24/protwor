#import modules
from tkinter import *
from tkinter import messagebox
import time
import random
#import sleep

#getting words
Green = "#007d21"
Yellow = "#FFA500"
Black = "#000000"
White = "#FFFFFF"
words = ["sleep","steep","foods","digit","horse"]
word = words[random.randint(0,len(words)-1)]

#running the window 
root = Tk()
root.title("wordle")
root.config(bg="#808080")
try_number = 1

word_input = Entry(root)
word_input.grid(row = 7000 , column = 0 , padx = 10 , pady = 10 , columnspan = 30)

def Guess():
  global word
  global try_number
  guess = word_input.get( )
  if len(guess) == 5:
      if try_number < 6:
            if word == guess:
              messagebox.showinfo("correct",f"correct the word is {word}")
            else:
              for i, letter in enumerate(guess):
          
                label = Label(root , text = letter.upper())
                label.grid(row=try_number*1000 , column = i , padx = 4 , pady = 10)
          
                if letter == word[i]:
                  label.config(bg= Green,fg = White)
          
                if letter in word and not letter == word[i] :
                  label.config(bg= Yellow ,fg = White)
          
                if letter not in word:
                   label.config(bg= Black ,fg = White)
    
            try_number += 1 
           
      else:
          messagebox.showinfo("game over",f"correct the word is {word}")
  else: 
        messagebox.showinfo("letter error","use 5 letters")
    

      
      

word_Guessbutton = Button(root , text = "Try!" , command = Guess)
word_Guessbutton.grid(row=7000 , column = 140 , columnspan = 5)

root.mainloop()