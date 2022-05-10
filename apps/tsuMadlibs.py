# -*- coding: utf-8 -*-
"""Tsunamifi's Madlibs Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148wG08Z0RGVBVg-otJDWXJtMULjk21WD

# MadLib Generator :)

# *RUN BEFORE PLAYING (NECESSARY)*
"""

#importing things here
import os
from google.colab import output
from google.colab import widgets
from IPython.display import HTML, display
import textwrap

#defining functions here


## creating user input for variables then placing the variables inside of the actual madlib story
def madlib1():

        noun = input(' enter a noun: ' )
        noun2 =  input(' enter another noun: ' ) 
        verb =   input('enter a verb(ing):  ' ) 
        verb2 =   input('enter a different verb(ing):  ' )
        bodys =  input('enter a body part (plural):  ' ) 
        emo =  input('enter an emotion:  ' ) 
        adj =  input('enter an adjective:  ' ) 
        adj2 =  input('enter a second adjective:  ' )
        adj3 =  input('enter a third adjective:  ' )
        name =  input('enter a male name:  ' ) 
        name2 =  input('enter a female name:  ' )
        drink = input('enter a type of drink: ') 
        city = input('enter a city: ')

        stry = ('\033[1m' + '\033[3m' + name  + '\033[0m' + '\033[1m' + ' looked at the ' + '\033[3m' + adj3 + ' ' + noun + ' in his hands and felt ' + '\033[3m' + emo + '\033[0m' + '\033[1m' + '. He walked over to the window and reflected on his ' + '\033[3m' + adj2 + '\033[0m' + '\033[1m' + ' surroundings. He had always loved ' 
         '\033[3m' + adj + ' ' + city + '\033[0m' + '\033[1m' + ' with its many mountains. It was a place that encouraged his tendency to feel ' + '\033[3m' + emo + '\033[0m' + '\033[1m' + '. Then he saw something in the distance, or rather someone. It was the figure' 
         ' of ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + '. ' + '\033[3m' + name2 + ' was a gentle saint with flawless ' + '\033[3m' + bodys + '\033[0m' + '\033[1m' + ' and a heart filled with ambition. ' + '\033[3m' + name + '\033[0m' + '\033[1m' + ' was shocked. His friends saw him as a helpful hero. Once, he had even helped a puppy cross the road. But not even a remarkable person who had once helped a puppy cross the road, was ' 
         'prepared for what ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' had in store today. "The warrior exams ended, and all the others are ' + '\033[3m' + verb + '\033[0m' + '\033[1m' + ' with their partners", making ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' sad. As ' + '\033[3m' + name + '\033[0m' + '\033[1m' + ' stepped '
         'outside and ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' came closer, he could see the shivering glint in her eye. ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' looked with the pain on her face. She said, in frustration, "There is no one left for me. ' 
         'I want a partnership, I want to fight and do good with you." ' + '\033[3m' + name + '\033[0m' + '\033[1m' + ' looked back, and still fidgeting with the ' + '\033[3m' + adj3 + ' ' + noun + '\033[0m' + '\033[1m' + ', "' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ', you really want to be my partner?", he replied. ' 
         '\033[3m' + name + '\033[0m' + '\033[1m' + ' thought it over, and decided it was better than having to keep ' + '\033[3m'  + verb2 + '\033[0m' + '\033[1m' + ' all these foes by him self, ' + '\033[3m'  + name  + '\033[0m' + '\033[1m' + ' could use ' + '\033[3m'  + name2  + '\033[0m' + '\033[1m' + 's flawless ' + '\033[3m'  + bodys  + '\033[0m' + '\033[1m' + ' and heart of ambition. "Its settled' 
         ', we are a team now." revealed ' + '\033[3m' + name + '\033[0m' + '\033[1m' + ' with a grin. ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' looked happy, her emotions erupting like a noisy ' + '\033[3m' + noun2 + '\033[0m' + '\033[1m' + '. Then ' + '\033[3m' + name2 + '\033[0m' + '\033[1m' + ' came inside for a nice drink of ' + '\033[3m' + drink +
         
         ' THE END.')
       
  
       
      
        print(textwrap.fill(stry, 80)) 
       
       
def  madlib2():

        noun = input(' enter a noun: ' )
        cash1 =   input('enter number:  ' ) 
        cash2 =   input('enter another number:  ' )
        name =  input('enter a name:  ' ) 
        emo =  input('enter an emotion(-ness or -ion):  ' ) 
        adj =  input('enter an adjective:  ' ) 
        adj2 =  input('enter a second adjective:  ' )
        gender =  input('boy or girl:  ' ) 

        stry =  ('\033[1m' + '\033[3m' + emo + '\033[0m' + '\033[1m' + ' was on the rise. I had to buy a new car. How much would it cost? $' + '\033[3m' + cash1 + '\033[0m' + '\033[1m' + '? $' + '\033[3m' + cash2 + '\033[0m' + '\033[1m' + '? I had no clue but I knew it would be expensive.'
'I got to the dealership, and the salesman did not seem very knowledgeable about cars. He was wearing a tight-fitting ' + '\033[3m'  + adj2 + '\033[0m' + '\033[1m' + ' suit that looked like it was about to burst at the seams and his hair looked like he had just been electrocuted. When I asked him which one he recommended, he said that he was really fond of the car with ' + '\033[3m' + adj + '\033[0m' + '\033[1m' + ' wheels. '
' He slaps the roof of car with the ' + '\033[3m' + adj + '\033[0m' + '\033[1m' + ' wheels and says "This bad ' + '\033[3m' + gender + '\033[0m' + '\033[1m' + ' can fit so many ' + '\033[3m' + noun + '\033[0m' + '\033[1m' + ' in it" '
'I asked the salesman what his name was and he replied, "' + '\033[3m' + name + '\033[0m' + '\033[1m' + "'. I said, " + '\033[3m' + name + '\033[0m' + '\033[1m' + ', would you be offended if I called you a terrible car salesman?" '
' He laughed and said, "No. It is actually a term of endearment in our industry. I then smiled and said, "In that case  ' + '\033[3m' + name + '\033[0m' + '\033[1m' + ', I am NOT buying your car."')

        print(textwrap.fill(stry, 80))

def mlc():
    if madlib_choice == 'The lonely companion':
       madlib1()
    else:
       madlib2()

## asks user if they would like to run the application over again
def WPA(): #wanna play again?
      while True:
       Answer = input(' Would you like to play this Madlib again?: ')
       if Answer == 'yes' or Answer == 'Yes':
        mlc()
        output.clear()
       elif Answer == ("no") or ("No"):
        print('Thanks for playing! Try my other madlibs!')
        break
        output.clear()

"""# *OK, we can play now!*"""

#@title Choose which madlib to play!
# code to play
with st.form(key='vars'):
        submit_button = st.form_submit_button(label='Run')
        madlib_choice = st.selectbox('Madlibs',('The lonely companion', 'Lost my business'))
## call madlib function
def run():
  if madlib_choice == 'The lonely companion':
   madlib1()
  else:
   madlib2()
  output.
  ## just a separator so its easier on your eyes
  print('------------------------------------------------------------')

  ## call play again function
  WPA()

        
if submit_button:
            run()
