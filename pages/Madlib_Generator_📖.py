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
import streamlit as st
import textwrap
from PIL import Image

#streamlit formatting/functionality
st.title('Choose which madlib to play!')
madlib_choice = st.selectbox('', ('The Lonely Companion', '...You just lost my business'))
ML1, Cover = st.columns(2)
ML2, Cover2 = st.columns(2)

## importing story(book) covers
c1 = Image.open('LonelyCompanionMLcover.png')
c2 = Image.open('LMBMLcover.png')
    

#defining functions here


## creating user input for variables then placing the variables inside of the actual madlib story
def madlib1():
    
    
    with ML1:
       with st.form(key= 'ml1v'):
        noun = st.text_input(' Enter a noun: ' )
        noun2 =  st.text_input(' Enter 2nd noun: ' ) 
        verb =   st.text_input('Enter a verb(ing):  ' ) 
        verb2 =   st.text_input('Enter a 2nd verb(ing):  ' )
        bodys =  st.text_input('Enter a body part (plural):  ' ) 
        emo =  st.text_input('Enter an emotion:  ' ) 
        adj =  st.text_input('Enter an adjective:  ' ) 
        adj2 =  st.text_input('Enter a 2nd adjective:  ' )
        adj3 =  st.text_input('Enter a 3rd adjective:  ' )
        name =  st.text_input('Enter a male name:  ' ) 
        name2 =  st.text_input('Enter a female name:  ' )
        drink = st.text_input('Enter a type of drink: ') 
        city = st.text_input('Enter a city: ')
        submit = st.form_submit_button('Submit')
        
        
    stry = (name + ' looked at the ' + adj3 + ' ' + noun + ' in his hands and felt '  +  emo  +    '. He walked over to the window and reflected on his '  +  adj2   +   ' surroundings. He had always loved ' +
           adj  + ' ' +  city  +    ' with its many mountains. It was a place that encouraged his tendency to feel '  +  emo    +  '. Then he saw something in the distance, or rather someone. It was the figure' 
         ' of '  +  name2   +   '. '  +  name2 + ' was a gentle saint with flawless ' +   bodys  +    ' and a heart filled with ambition. '  +  name   +   ' was shocked. His friends saw him as a helpful hero. Once, he had even helped a puppy cross the road. However, not even a remarkable person who had once helped a puppy cross the road, was ' 
         'prepared for what '  +  name2   +   ' had in store today. Even from a short distance away from the door you could hear ' +  name2  + ' crying, sniffling. As ' +   name   +   ' stepped '
         'outside and '   + name2  +    ' came closer, he could see the shivering glint in their eye. '  +  name2   +   ' looked with the pain on her face. She said, in frustration, "The warrior exams ended, and all the others are '  +  verb   +   ' with their partners", making ' +   name2   +   ' sad.  "There is no one left for me. I want to be apart of a duo like everyone else, I want to fight and do good with YOU,'  +  name + ' " ' .   +  name +     ' looked back, and still fidgeting with the '  +  adj3 + ' ' + noun   +   ', "'  +  name2   +   ', you really want to partner up with me?", he replied. ' +
           name   +   ' thought it over, and decided it was better than having to keep '  +   verb2  +    ' all these foes by him self, '  +   name    +   ' could use '  +   name2  +     's flawless '   +  bodys  +     ' and heart of ambition. "Its settled' 
         ', we are a team now." revealed '  +  name   +   ' with a grin. '  +  name2 +     ' looked happy, Their emotions erupting like a noisy '   + noun2    +  '. Then '   + name2    +  ' came inside for a nice drink of '   + drink +
         
         ' The End.')
        
        
    with Cover:
        st.image(c1)
        if submit:
            st.write(textwrap.fill(stry, 150))
        
   


def  madlib2():
    
   
    with ML2:
       with st.form(key = 'ml2v'):
        noun = st.text_input(' Enter a noun: ' )
        cash1 =   st.text_input('Enter a number:  ' ) 
        cash2 =   st.text_input('Enter 2nd number:  ' )
        name =  st.text_input('Enter a name:  ' ) 
        emo =  st.text_input('Enter an emotion ending in "-ness or -ion":  ' ) 
        adj =  st.text_input('Enter an adjective:  ' ) 
        adj2 =  st.text_input('Enter a 2nd adjective:  ' )
        gender =  st.text_input('Boy or Girl:  ' ) 
        submit = st.form_submit_button('Submit')
        
        
    stry =  (    emo  +    ' was on the rise. I had to buy a new car. How much would it cost? $'  +  cash1   +   ',000 ?  $ '  +  cash2  +    ' ? I had no clue but I knew it would be expensive.'
'I got to the dealership, and the salesman did not seem very knowledgeable about cars. He was wearing a tight-fitting '  +   adj2    +  ' suit that looked like it was about to burst at the seams and his hair looked like he had just been electrocuted. When I asked him which one he recommended, he said that he was really fond of the car with ' +   adj   +   ' wheels. '
' He slaps the roof of car with the ' +   adj  +    ' wheels and says "This bad '   + gender  +    ' can fit so many ' +   noun    +  ' in it" '
'I asked the salesman what his name was and he replied, "' +   name   +   "'. I said, "  +  name   +   ', would you be offended if I called you a terrible car salesman?" '
' He laughed and said, "No. It is actually a term of endearment in our industry. I then smiled and said, "In that case  '  +  name    +  ', I am NOT buying your car."')

        
    with Cover2:
        st.image(c2)
        if submit:
          st.write(textwrap.fill(stry, 80))

        
    
def mlc():
    if madlib_choice == 'The lonely companion':
       madlib1()
    else:
       madlib2()


# code to play

## call madlib function

if madlib_choice == 'The Lonely Companion':
 madlib1()
else:
 madlib2()
## just a separator so its easier on your eyes
print('------------------------------------------------------------')
