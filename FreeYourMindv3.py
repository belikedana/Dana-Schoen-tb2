# things that I need to do:
# definitions out of definitions (check)
# homepage also in a definition that is just being called at the end (check)
# clean global variables and defined variables up (check)
# changed the button location (check)
# find reference
# problems: music page: once played music the gui cant load other pages (done)
# Exit Button in the same color as bg (done)
# clean up filepath (done)
# no double code (means the menu buttons have to be put in a definition) (done)

# TODO: clean up code & advance the code
# TODO: clean up the Meditations page
# TODO: design the login and register page
# TODO: Username recognition and welcome label on the Journal page after logging in?
# Question: do you want me to create a variable for the style of buttons? (when I use the code two times)
# Question: should we export our other pages and import them?
# Question: by the meditationspage the button grows! What the hell?
# Flag: the csv file did not create itself but i had to import it

# Need to import all these libraries
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import random
from datetime import date
from tkmacosx import Button
from PIL import Image, ImageTk
import pygame as pg
import os
import webbrowser
from gtts import gTTS
import pandas as pd

# Code to create the gui window
root = tk.Tk()

# Give your gui a title
root.title('Free Your Mind')

# Set the height and width as separate parameters to give you more flexibility
screen_width = 1400
screen_height = 800
# Use the minsize function to set the geometry
root.minsize(screen_width, screen_height)

# Create a custom style for the menu buttons
custom_style = dict(relief='raised', background='lightblue', border=7, highlightcolor='white',
                    highlightthickness=4, overbackground='lightgreen', bordercolor='lightblue',
                    activebackground='lightgreen', borderless=1, font='arial 17 bold', width=165, height=30)

# create variables in order to redirect file_path
code_file_path = os.getcwd()


# This definition will place the image on the gui window.
def add_image(root, file_path, width, height):
    # for some reason this image will not appear without specifying global variables
    global pic, f1

    # Reset the file path to find the images as uploading the music breaks the flow
    os.chdir(code_file_path)

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()


# Definition t clear all the widgets created before
def clear_widgets():
    for i in root.winfo_children():
        i.destroy()


# The definition that creates my exit button and menu buttons without login or register menu buttons
def menu_buttons():
    global exit_button, entry_button, reminders_button, quotes_button, books_button
    # Exit button to leave the app
    exit_button = Button(root, text='EXIT',
                         font='arial 10 bold',
                         width=60,
                         height=20,
                         relief='groove',
                         background='pink',
                         foreground='black',
                         overbackground='darkgrey',
                         border=7,
                         command=root.destroy)
    exit_button.place(x=1290, y=730)

    # Playlist Button that leads to Music Selection Section
    playlist_button = Button(root, text='PLAYLIST',
                             font='arial 15 bold',
                             width=100,
                             height=22,
                             relief='groove',
                             background='#7C93C3',
                             foreground='white',
                             overbackground='#BB9CC0',
                             border=7,
                             command=music_page
                             )
    playlist_button.place(x=50, y=50)

    # Create a Login Button
    login_button = Button(root, text='LOGIN',
                          font='arial 15 bold',
                          width=100,
                          height=22,
                          relief='groove',
                          background='#7C93C3',
                          foreground='white',
                          overbackground='#BB9CC0',
                          border=7,
                          command=login_or_register_page
                          # meditations_page
                          )
    login_button.place(x=1260, y=50)

    # The menu buttons with the applied custom style (can not be in the definition for the buttons because when clicked
    # they change colors and this cant be generalized
    reminders_button = Button(root, text='Affirmations',
                              **custom_style,
                              foreground='black',
                              command=display_affirmations)
    reminders_button.place(x=500, y=40)

    quotes_button = Button(root, text='Quotes',
                           **custom_style,
                           foreground='black',
                           command=display_quotes)
    quotes_button.place(x=1000, y=40)

    books_button = Button(root, text='Recommendations',
                          **custom_style,
                          foreground='black',
                          command=display_recommendations)
    books_button.place(x=750, y=40)

    entry_button = Button(root, text='Journal Entry',
                          **custom_style,
                          foreground='black',
                          command=journal_entry)
    entry_button.place(x=250, y=40)

# Create a Definition that is being called when user is logged in
def extra_menu_buttons():
    global meditation_page_button

    meditation_page_button = Button(root, text='Meditations',
                                    **custom_style,
                                    foreground='black',
                                    command=meditations_page)
    meditation_page_button.place(x=1200, y=150)


# Hompage Section.
# Here you can find all the definitions, variables, lists that are needed to create the homepage.

# Click on the name "Free your mind" - affirmations appear randomly
feel_good_statements = [
    "You are loved and appreciated!",
    "You are capable of amazing things!",
    "You bring joy to those around you!",
    "You are making a positive impact!",
    "You are doing great things!",
    "You are enough just as you are!",
    "You are a constant learner and grow every day!",
    "You have the power to overcome any challenge!",
    "You are a valuable and unique individual!"]

corner_label = tk.Label()


# This function generates the statements from the list and puts them in one of the four corners
def generate_feel_good_statement():
    global corner_label
    # Randomly select a statement from the list
    statement = random.choice(feel_good_statements)
    # Randomly position the label in one of the corners
    # Reference: https://stackoverflow.com/questions/64918341/python-tkinter-how-to-adjust-the-x-y-default-0-0-coordinates
    x = random.choice([30, root.winfo_width() - 300])
    y = random.choice([30, root.winfo_height() - 50])
    corner_label.place(x=x, y=y)
    # Display the statement in the chosen corner
    corner_label.config(text=statement)
    # forgets the statements after 4000 milliseconds
    root.after(4000, hide_feel_good_statement)


# Function to hide the statements when user doesn't press button anymore
def hide_feel_good_statement():
    corner_label.place_forget()


# The definition that creates the homepage
def homepage():
    global corner_label

    # add a background to your page
    add_image(root, "images/Mediatations.png", screen_width, screen_height)

    # All the homepage buttons and labels

    # The label where the statements appear in
    corner_label = tk.Label(root, text="",
                            bg='lightblue',
                            fg='black',
                            font='Arial 12',
                            relief='groove',
                            border=5)

    # Add the FREE YOUR MIND Logo/Button
    disclaimer = Button(root, text='FREE YOUR MIND',
                        font='arial 30 bold',
                        relief='raised',
                        background='lightblue',
                        overbackground='lightblue',
                        overforeground='white',
                        highlightcolor='blue',
                        foreground='black',
                        border=7,
                        highlightthickness=0,
                        borderless=1,
                        height=55,
                        width=285,
                        command=generate_feel_good_statement)
    disclaimer.place(x=550, y=70)

    # Add a welcome label
    welcome = tk.Label(root,
                       text='Welcome, beautiful human being! \n I am glad you want to take care of your mental well being! \n '
                            'You are in luck. \n \nWith the FREE YOUR MIND App, you can journal all your heavy feelings of your chest, '
                            '\n find daily affirmations, some well-being tips and more. Should we go explore?',
                       font='arial 20',
                       bg='#264753',
                       fg='white',
                       relief='groove',
                       border=9)
    welcome.place(x=260, y=300)

    # Add a continue button that will lead to the other pages
    continue_button = Button(root, text='Lets Go FREE YOUR MIND>>',
                             font='arial 18 bold',
                             relief='raised',
                             background='lightgreen',
                             overbackground='pink',
                             highlightcolor='purple',
                             foreground='black',
                             activebackground='pink',
                             border=8,
                             height=45,
                             width=270,
                             command=journal_entry)
    continue_button.place(x=555, y=670)


# Journal Entry Section
# Here you can find all the definitions, variables, lists that are needed to create the journal entry page.

recom_label = tk.Label()
entry = tk.Entry()
message_label = tk.Label()


# Reference: https://tkdocs.com/tutorial/text.html#basics
def save_entry():
    # Safe the entry made in the text file and safe it as journal.txt
    entry_text = entry.get("1.0", tk.END).strip()
    if entry_text:
        today = date.today()
        entry_date = today.strftime("%d/%m/%Y")
        journal_file = open("journal.txt", "a")
        journal_file.write(f"{entry_date}:\n{entry_text}\n\n")
        journal_file.close()
        entry.delete("1.0", tk.END)
        # message that the text was saved
        message_label.config(text='Entry saved successfully!',
                             font='arial 15 bold',
                             relief='groove',
                             bg='lightblue',
                             fg='purple',
                             border=5
                             )
        message_label.place(x=590, y=730)
        # Message disappears after a few seconds (in milliseconds)
        message_label.after(4000, message_label.destroy)


# Creating a list that will be displayed in a label for some inspo journal promps
recom_list = ["Here are some journal prompts for when you don't know what to journal about: \n"
              'What is the best way for you to practice self-care, when you are feeling tense, anxious or depressed? \n'
              "Write about something, that is going well in your life right now, and how it affects you. \n"
              "If you had a conversation with your younger self, what would you tell them? \n"
              "What ignites the spark in you, you felt as a kid? \n"
              "If you could relive a certain moment in your life again, which one would it be and why? \n"
              "Make a list of things that bring you joy and that make your life as delicious, as possible."
              ]
# Getting rid of the curly brackets, that are being displayed by converting to a string
recom_list_string = " ".join(recom_list)

# Controlling the visibility of the inspiration label
# Idea: On a click the user can see the label and with another click can make the label disappear
label_visible = False


# Definition to make the label appear and disappear
def visibility():
    global label_visible
    if not label_visible == True:
        recom_label.place(x=45, y=210)
        label_visible = True
    else:
        recom_label.place_forget()
        label_visible = False


# The Definition that creates the page with the Journal Entry
def journal_entry():
    # Declare all these variables global
    global recom_label, entry, message_label

    # Clear all the widgets that were created before
    clear_widgets()

    # add a background to your page
    add_image(root, "images/Galaxy2.png", screen_width, screen_height)

    # Entry label
    entry_label = tk.Label(root, text='Now you can let all your thoughts go. \n Write your journal entry here:',
                           font='arial 30 bold',
                           anchor='center',
                           bg='pink',
                           fg='black',
                           relief='groove',
                           border=7
                           )
    entry_label.place(x=420, y=150)

    # Text entry field
    entry = tk.Text(root, height=25, width=80, bg='black', fg='white', insertbackground='white')
    entry.place(x=430, y=300)

    # Save button
    save_button = Button(root, text='Save Entry',
                         font='arial 20 bold',
                         background='grey',
                         foreground='black',
                         border=7,
                         highlightbackground='blue',
                         overbackground='pink',
                         borderless=1,
                         relief='groove',
                         height=30,
                         width=165,
                         command=save_entry)
    save_button.place(x=610, y=650)

    # Button and Label for Recommendations

    # Add a label filled with recommendations and a button that activates the label
    recom_label = tk.Label(root, text=recom_list_string,
                           font='arial 15',
                           relief='sunken',
                           wraplength=200,
                           bg='pink',
                           fg='grey',
                           border=6
                           )

    recom_button = Button(root, text='In need of inspiration?',
                          relief='raised',
                          foreground='black',
                          background='grey',
                          border=5,
                          overforeground='lightblue',
                          command=visibility)
    recom_button.place(x=70, y=160)

    # Message label
    message_label = tk.Label(root, text="")
    message_label.pack()

    # Call the definition to create the exit button and the menu buttons
    menu_buttons()
    # The button of the page we are on appears with a white foreground
    entry_button.configure(foreground='white')


# Display Affirmations Section.
# In this Section are all the Definitions, Lists and Variables used for the Affirmations Page.
start_button = Button()
affirmation_label = tk.Label()
# Variable to control the loop
continue_loop = True

# Global variable to store the current affirmation
current_affirmation = ""

# List with all the affirmations
affirmations = ['I am glowing!',
                'I am worthy of love and happiness.',
                "I embrace the power within me.",
                "I am confident and capable of achieving my goals.",
                "I choose to let go of negativity and embrace positivity.",
                "I am deserving of success and abundance.",
                "I am grateful for all the wonderful things in my life.",
                "I am strong and can overcome any challenge.",
                "I radiate love and positivity to those around me.",
                "I am enough just as I am.",
                "I trust in my abilities and intuition.",
                "I am in the right place at the right time, doing the right things.",
                "I am okay, I am loved and I am safe.",
                "Great things will happen to me.",
                "The chance to love and be loved, exists no matter where I am. ",
                "I am the best version of myself.",
                "It's okay to feel my feelings.",
                "I let go of what no longer serves me.",
                "I forgive myself and I am deserving of all the love and happiness in the world.",
                "I love myself for who I am.",
                "I trust the universe to guide me on this journey called life.",
                "I can overcome any challenge that stands in my way.",
                "I find my way back to myself again and again and again."]
# Shuffle the list of affirmations
random.shuffle(affirmations)
# Set the index at 0 to loop through the affirmations
current_affirmation_index = 0


# Definition to change the text to speech
# Reference: https://gtts.readthedocs.io/en/latest/index.html
def convert_text_to_speech(text_to_speak):
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save('affirmation.mp3')
    os.system('afplay affirmation.mp3')


# Definition to display the current chosen affirmation from the list and loop through the list
def display_and_loop_affirmation():
    global current_affirmation_index, current_affirmation
    # Display current affirmation chosen from list on the label
    current_affirmation = affirmations[current_affirmation_index]
    affirmation_label.config(text=current_affirmation)

    # Convert and play the current affirmation after 1 second
    # Reference: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
    root.after(2000, lambda: convert_text_to_speech(current_affirmation))

    # Increment index for the next affirmation in the list to be displayed and looped through
    # This expression increments the index by 1, moving to the next affirmation in the list
    # The Modulo operation (%) ensures that when the incremented index exceeds the maximum index (length of the list - 1), it wraps around to 0, effectively creating a loop.
    current_affirmation_index = (current_affirmation_index + 1) % len(affirmations)

    # Check if the loop should continue
    if continue_loop:
        # Schedule the next call to display_and_loop_affirmation after 5 seconds
        root.after(5000, display_and_loop_affirmation)


# Function to stop and restart affirmations
def toggle_affirmations():
    global continue_loop
    # Toggle the value of continue_loop between True and False
    # Reference: https://docs.python.org/3/library/stdtypes.html#boolean-values
    continue_loop = not continue_loop
    # Update button text based on the current state
    start_button.config(text='Stop Affirmations' if continue_loop else 'Start Affirmations')
    # If restarting, call the display_and_loop_affirmation function
    if continue_loop:
        display_and_loop_affirmation()


# The Definition that creates the page with the Affirmations
def display_affirmations():
    # Declare all the variables global, so we can delete them later
    global start_button, affirmation_label
    # Clear all the widgets that were created before
    for i in root.winfo_children():
        i.destroy()

    # add a background to your page
    add_image(root, "images/Aura8.jpeg", screen_width, screen_height)

    # Start Affirmations button
    start_button = Button(root, text='Generate Affirmations',
                          command=toggle_affirmations,
                          relief='groove',
                          font='arial 20 bold',
                          background='#9B4171',
                          foreground='black',
                          border=8,
                          overbackground='#7C3681')
    start_button.place(x=590, y=670)

    # Affirmation label
    affirmation_label = tk.Label(root, text='Affirmations will appear here:',
                                 wraplength=300,
                                 font='arial 17 bold',
                                 bg='orange',
                                 relief='flat',
                                 fg='black',
                                 border=5,
                                 width=30,
                                 height=3)
    affirmation_label.place(x=535, y=370)

    # Call the definition to create the exit button and menu buttons
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='blue')
    # The button of the page we are on appears with a white foreground
    reminders_button.configure(foreground='white')


# Recommendations Section.
# # In this Section are all the Definitions, Lists and Variables used for the Recommendations Page.
current_label = tk.Label()
label_button1 = Button()
label_button2 = Button()
label_button3 = Button()
emergency_label = tk.Label()
# Create lists containing the different recommendations that are being displayed
# Book recommendations
list1 = [
    "1. 'Untamed' by Glennon Doyle \n Author Glennon Doyle wants to help readers find themselves, and the great "
    "success of her book, Untamed, seems to suggest she has done just that. People magazine calls her the “patron "
    "saint of female empowerment”",
    "and hails her call to trust the voice inside as phenomenal. ",
    "For many years, Doyle says she ignored her own discontent with life, burying herself beneath addictions, "
    "cultural conditioning, and institutional allegiances until she found her voice and power.",
    "In this memoir, you learn her story and discover how to follow suit and bring your whole self the table. \n",

    "2. \'The Mountain is You\' by Brianne Wiest \n This is a book about self-sabotage. Why we do it, when we do it, "
    "and how to stop doing it—for good. Coexisting but conflicting needs create self-sabotaging behaviors. This is "
    "why we resist efforts to change, often until they feel completely futile. But by extracting crucial insight from "
    "our most damaging habits, building emotional intelligence by better understanding our brains and bodies, "
    "releasing past experiences at a cellular level, and learning to act as our highest potential future selves, "
    "we can step out of our own way and into our potential. \n",

    "3. 'The Power of Now' by Eckhart Tolle \n The book discusses the importance of stepping back from consumption in "
    "negative thoughts to listening to the conversations you have with yourself from an outside perspective. If you "
    "suffer from anxiety, overthinking, depression, or panic attacks, The Power of Now will ignite change in how you "
    "interact with yourself and with the world. Although the switch is a difficult journey, Eckhart elegantly lifts "
    "readers up to a higher altitude of being where you can breathe better air."
]

#  Podcast recommendations
list2 = [
    "1. The Mel Robbins Podcast \n In The Mel Robbins Podcast, Mel gets more personal than ever, welcoming you into "
    "her life and taking you behind the scenes in real time. Every episode is packed with deeply relatable topics, "
    "tactical advice, hilarious screwups, compelling conversations, and the tools and inspiration you need to create "
    "a better life. \n",
    "2. Attitudes \n This show tackles big political and cultural issues facing women and marginalized communities, "
    "including LGBT communities. Hosts Erin Gibson and Bryan Safi put these sometimes esoteric but crucial "
    "conversations firmly in the spotlight. Their aim is to leave no doubts that these issues can affect you "
    "mentally, emotionally, and personally in toxic ways. Gibson and Safi strike a delicate balance between the "
    "political and the personal by making it feel OK to think of yourself as part of a bigger movement while also "
    "affirming that your thoughts and feelings matter. \n",
    "3. The Happiness Lab \n Happiness can seem unattainable sometimes. This is especially true when the things you "
    "work hard to earn don’t bring the happiness you expect. Dr.Laurie Santos hopes to show you that your own "
    "happiness is in your control in even the smallest ways using findings from cutting-edge scientific research on "
    "the link between human behavior and emotions."
]

# Instagram recommendations
list3 = [
    "1. @mentl.sesh \n Advocacy, resources and community for people who want to receive their information from "
    "Instagram. There are so many great tips and pointers for dealing with mental health on this account. \n",
    "2. @selfloveblossom \n Selflove is a practice we all need to learn and some would even say, the key to find "
    "happiness is to love yourself unconditionally. \n",
    "3. @dearmyanxiety \n One way to manage anxiety is to follow this relatable account, which hopes to destigmatise "
    "anxiety for all followers. \n",
    "4. @themindgeek \n There is excellent mental health advice and tips on achieving wellbeing on this account, "
    "which has a focus on overcoming relationship trauma. \n",
    "5. @makedaisychains \n One of the most popular mental health Instagram accounts for a reason. Queer artist "
    "Hannah Daisy shares drawings and powerful quotes through her platform to an audience of more than 100,"
    "000 fans. Her focus is on LGBTQI rights and inclusivity, and her feed is a welcoming place for all."
]
# Convert to string so the curly brackets are not showing
list1_string = " ".join(list1)
list2_string = " ".join(list2)
list3_string = " ".join(list3)


def display_theme(theme_text):
    current_label.config(text=theme_text)
    current_label.place(x=300, y=300)


# Emergency phone number label/button (only on the recommendations page)
emergency_contacts = ["Telefon-Seelsorge (DE):\n0800 1110 111 \n"
                      "Children and Teenage-Hotline:\n116111 \n"
                      "Domestic Violence-Hotline:\n116 016"]

# Getting rid of the curly brackets that are being displayed by converting to a string
emergency_contacts_string = " ".join(emergency_contacts)

# Controlling the visibility of the emergency contacts label
# On a click the user can see the label and with another click can make the label disappear
label_visible1 = False


def visibility2():
    global label_visible1
    if not label_visible1 == True:
        emergency_label.place(x=55, y=550)
        label_visible1 = True
    else:
        emergency_label.place_forget()
        label_visible1 = False


# This Definition creates th page with the Recommendations
def display_recommendations():
    # Declare all the variables as global
    global current_label, label_button1, label_button2, label_button3, emergency_label
    # Clear all the widgets that were created before
    for i in root.winfo_children():
        i.destroy()

    # add a background to your page
    add_image(root, "images/Books6.png", screen_width, screen_height)

    # Create an instruction label
    instruction_label = tk.Label(root,
                                 text='Here you can find some recommendations to increase your Mental-Well-Being' '\n'
                                      'and learn more about the topic of how to free your mind.',
                                 font='arial 20 bold',
                                 bg='blue',
                                 fg='lightblue',
                                 relief='groove',
                                 border=6,
                                 borderwidth=8
                                 )
    instruction_label.place(x=330, y=120)

    # Theme selection label
    theme_label = tk.Label(root, text='Choose a medium:',
                           font='arial 17',
                           bg='darkred',
                           fg='darkblue',
                           relief='groove',
                           border=6,
                           borderwidth=8,
                           width=17
                           )
    theme_label.place(x=100, y=210)

    # Create custom style for label buttons
    customstyle = dict(font='arial 15 bold',
                       background='darkblue',
                       foreground='white',
                       border=7,
                       overrelief='raised',
                       overforeground='darkred',
                       borderless=1,
                       highlightthickness='4',
                       highlightcolor='darkred',
                       relief='raised')

    current_label = tk.Label(root, text="",
                             wraplength=750,
                             font='arial 15',
                             bg='purple',
                             fg='lightblue',
                             relief='groove',
                             border=6,
                             borderwidth=8
                             )

    # Add buttons
    label_button1 = Button(root, text='Books', **customstyle, command=lambda: display_theme(list1_string))
    label_button1.place(x=430, y=210)

    label_button2 = Button(root, text='Podcasts', **customstyle, command=lambda: display_theme(list2_string))
    label_button2.place(x=630, y=210)

    label_button3 = Button(root, text='Instagram Accounts', **customstyle, command=lambda: display_theme(list3_string))
    label_button3.place(x=830, y=210)

    # Emergency Contact label
    emergency_label = tk.Label(root, text=emergency_contacts_string,
                               font='arial 13',
                               relief='sunken',
                               wraplength=200,
                               bg='darkred',
                               fg='lightblue',
                               border=6
                               )

    emergency = Button(root, text='need help?',
                       font='arial 11',
                       width=80,
                       height=20,
                       relief='groove',
                       background='darkblue',
                       foreground='white',
                       overforeground='darkred',
                       border=7,
                       command=visibility2)
    emergency.place(x=110, y=730)

    # Call the definition to create the menu buttons and exit button
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='darkred')
    # The button of the page we are on appears with a white foreground
    books_button.configure(foreground='white')


# Quotes Section.
# In this Section are all the Definitions, Lists and Variables used for the Quotes Page.

stop_button = Button()
slideshow_button = Button()
slideshow_label = tk.Label()

# Define a list of image filenames for the slideshow
image_files = ["quotes/1.jpeg", "quotes/2.jpeg", "quotes/3.jpeg", "quotes/4.jpeg", "quotes/5.jpeg", "quotes/6.jpeg",
               "quotes/7.jpeg", "quotes/8.jpeg", "quotes/9.jpeg", "quotes/10.jpeg", "quotes/11.jpeg",
               "quotes/12.jpeg", "quotes/13.jpeg", "quotes/14.jpeg", "quotes/15.jpeg", "quotes/16.jpeg",
               "quotes/17.jpeg", "quotes/18.jpeg", "quotes/19.jpeg", "quotes/20.jpeg", "quotes/21.jpeg",
               "quotes/21.jpeg", "quotes/22.jpeg", "quotes/23.jpeg", "quotes/24.jpeg", "quotes/25.jpeg"]

# Variable to track the current index of the slideshow
current_index = 0

# Variable to store the slideshow after() id; important to define if the image is changing or not
slideshow_id = None


# Function to update the slideshow with the next image
def update_slideshow():
    global current_index, slideshow_id

    # Load the images using PIL
    image = Image.open(image_files[current_index])
    image = image.resize((600, 400), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Update the label with the new image
    slideshow_label.config(image=photo)
    slideshow_label.image = photo

    # Increment the index for the next image; needed so the images move through the slide show (always +1 image)
    current_index += 1
    if current_index >= len(image_files):
        current_index = 0

    # Schedule the next update after a certain interval (in milliseconds)
    slideshow_id = root.after(4000, update_slideshow)


# Function to start the slideshow
def start_slideshow():
    global slideshow_id
    if slideshow_id is None:
        update_slideshow()


# Function to stop the slideshow
def stop_slideshow():
    global slideshow_id
    if slideshow_id is not None:
        root.after_cancel(slideshow_id)
        slideshow_id = None


# The Definitions that creates the Quotes page
def display_quotes():
    # Define all the variables as global
    global stop_button, start_button, slideshow_label
    # Clear all the widgets that were created before
    for i in root.winfo_children():
        i.destroy()

    # add a background to your page
    add_image(root, "images/Forest2.jpeg", screen_width, screen_height)

    # Create a label widget to display the images
    slideshow_label = tk.Label(root, border=8, text='The Quotes-Slideshow will appear here, once you press start:',
                               font='arial 17 ', bg='green', fg='white', relief='groove')
    slideshow_label.place(x=400, y=200)

    # Create start and stop buttons
    start_button = Button(root, text='Start',
                          relief='raised',
                          font='arial 15 bold',
                          background='darkgreen',
                          foreground='white',
                          width=90,
                          height=30,
                          border=6,
                          highlightthickness=4,
                          highlightcolor='darkorange',
                          overbackground='darkorange',
                          command=start_slideshow)
    start_button.place(x=550, y=700)

    stop_button = Button(root, text='Stop',
                         relief='raised',
                         font='arial 15 bold',
                         background='darkgreen',
                         foreground='white',
                         width=90,
                         height=30,
                         border=6,
                         highlightthickness=4,
                         highlightcolor='darkorange',
                         overbackground='darkorange',
                         command=stop_slideshow)
    stop_button.place(x=720, y=700)

    # Call the definition to create the exit button and menu buttons
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='darkgreen')
    # The button of the page we are on appears with a white foreground
    quotes_button.configure(foreground='white')


# Music Page Section.
# All the definitions, lists and variables for the music page and the definition that creates the music page.

play_button = Button()
pause_button = Button()
play_list = tk.Listbox()
# Store the song name as a variable
song_name = tk.StringVar()


# Create a definition that opens Spotify in the browser
def select_spotify():
    webbrowser.open('https://open.spotify.com')


# Create a definition that makes it possible to select music from your own directory
def select_music():
    # Create the  directory box
    directory = askdirectory()
    os.chdir(directory)
    song_list = os.listdir()  # this gives all the songs in the folder you selected

    # Loop through my song list and insert into the song box
    pos = 0
    for song in song_list:
        play_list.insert(pos, song)
        pos += 1


# Create a definition that clears the songs in the ListBox
def clear_tracks():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "Playlist is empty.")
        return

    # Clears all the tracks starting with the index 0 (the first item on the list) and ending at the end
    play_list.delete(0, tk.END)
    # The song name is being replaced by an empty variable
    song_name.set("")
    # Stop the music playing when cleared
    pg.mixer.music.stop()


# Create a definition that makes the music play
def play_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return
    # loads the file and activate it when listening to it
    pg.mixer.music.load(play_list.get(tk.ACTIVE))
    # plays the music
    pg.mixer.music.play()


def play_on_selection():
    play_music()


# Create definitions that make the music stop, pause and unpause
def stop_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return

    pg.mixer.music.stop()


def pause_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return

    pg.mixer.music.pause()
    pause_button.configure(text='Unpause',
                           command=unpause_music)


def unpause_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return

    pg.mixer.music.unpause()
    pause_button.configure(text='Pause',
                           command=pause_music)


# Definition to create a music page
def music_page():
    global play_button, stop_button, pause_button, play_list, song_name
    pg.mixer.init()
    # Clear all the widgets that were created before
    for i in root.winfo_children():
        i.destroy()

    # add a background to your page
    add_image(root, "images/house.jpeg", screen_width, screen_height)

    # Create a label that gives information on the music selection
    intro_label = tk.Label(root,
                           text="Welcome to the Music Selection Section. \n Why don't you put on some music while browsing through the app? \n"
                                "\n"
                                "You can either select a pre-made playlist from Spotify or create your own.",
                           font='arial 20 bold',
                           relief='groove',
                           bg='#67729D',
                           border=5)
    intro_label.place(x=350, y=170)

    # Create a button to select a playlist from spotify
    select_playlist = Button(root, text='Select Playlist',
                             font='arial 17 bold',
                             width=150,
                             height=30,
                             relief='raised',
                             border=5,
                             background='#BB9CC0',
                             foreground='black',
                             overbackground='#E7BCDE',
                             command=select_spotify)
    select_playlist.place(x=200, y=400)

    # Create a button to activate the song collection
    create_playlist = Button(root, text='Create Playlist',
                             font='arial 17 bold',
                             width=150,
                             height=30,
                             relief='raised',
                             border=5,
                             background='#BB9CC0',
                             foreground='black',
                             overbackground='#E7BCDE',
                             command=select_music)
    create_playlist.place(x=200, y=500)

    # Create buttons to play, stop and pause the music and place them
    play_button = Button(root, text='Play',
                         width=120,
                         height=30,
                         font='arial 17 bold',
                         background='#E7BCDE',
                         relief='raised',
                         border=5,
                         foreground='black',
                         overbackground='#BB9CC0',
                         highlightthickness=4,
                         highlightcolor='#7C93C3',
                         command=play_music)
    play_button.place(x=1100, y=350)

    stop_button = Button(root, text='Stop',
                         width=120,
                         height=30,
                         relief='raised',
                         border=5,
                         font='arial 17 bold',
                         background='#E7BCDE',
                         foreground='black',
                         overbackground='#BB9CC0',
                         highlightthickness=4,
                         highlightcolor='#7C93C3',
                         command=stop_music)
    stop_button.place(x=1100, y=450)

    pause_button = Button(root, text='Pause',
                          relief='raised',
                          border=5,
                          font='arial 17 bold',
                          background='#E7BCDE',
                          foreground='black',
                          overbackground='#BB9CC0',
                          highlightthickness=4,
                          highlightcolor='#7C93C3',
                          command=pause_music)
    pause_button.place(x=1100, y=550)

    # Creating a list box, that will contain all the songs in the folder I select
    play_list = tk.Listbox(root,
                           font='arial 20',
                           bg='#7C93C3',
                           fg='white',
                           selectmode=tk.SINGLE,  # only able to select one file at a time
                           width=30,
                           height=10,
                           relief='sunken',
                           border=7)
    # Place the Listbox
    play_list.place(x=530, y=350)

    # Add a Clear Playlist Button to clear the selected songs
    clear_playlist = Button(root,
                            text='Clear Playlist',
                            font='arial 14 bold',
                            width=130,
                            height=30,
                            relief='raised',
                            border=5,
                            background='#FED9ED',
                            foreground='black',
                            overbackground='#EEF5FF',
                            command=clear_tracks)
    clear_playlist.place(x=650, y=700)

    # Play music on selection
    play_list.bind('<<ListboxSelect>>', play_on_selection)

    # Call the definition to create the exit button and the menu buttons
    menu_buttons()


# Meditations Page.
# This is the section where you can find all the variables and definitions for the Meditations Page.
def pause_meditation():
    pg.mixer.music.pause()

    pause_button1.configure(text='⏯️',
                            command=unpause_meditation)

    pause_button2.configure(text='⏯️',
                            command=unpause_meditation)

    pause_button3.configure(text='⏯️',
                            command=unpause_meditation)


def unpause_meditation():
    pg.mixer.music.unpause()

    pg.mixer.music.unpause()
    pause_button1.configure(text='⏸',
                            command=pause_meditation)

    pause_button2.configure(text='⏸',
                            command=pause_meditation)

    pause_button3.configure(text='⏸',
                            command=pause_meditation)


# The Definitions to play the Meditations
# Meditations from: https://www.helpguide.org/home-pages/audio-meditations.htm
def play_1():
    pg.mixer.music.load("meditationmusic/Sleep.mp3")
    pg.mixer.music.play()


def play_2():
    pg.mixer.music.load("meditationmusic/StressRelief.mp3")
    pg.mixer.music.play()


def play_3():
    pg.mixer.music.load("meditationmusic/Gratitude.mp3")
    pg.mixer.music.play()


# Texts for the Labels
general_meditation = [
    "Meditation has many benefits. It reduces stress, increases calm \n and focus, and promotes greater "
    "physical and emotional well-being. \n Anyone can do it, and the rewards can come quickly. \n These guided "
    "meditations will help you get started."]

meditation_label1 = ["This bedtime sleep meditation uses deep breathing, mindfulness, and body scan techniques to help"
                     " you relax, calm the mind and body, and wind down for the day so you can ease gently into sleep."]

meditation_label2 = [
    "Relieve stress, anxiety, and muscle tension with this simple, yet powerful whole-body relaxation exercise."]

meditation_label3 = [
    "During extraordinarily challenging times like this coronavirus pandemic, we can become overwhelmed "
    "and lose sight of hope. But even in the most difficult of circumstances, our mind is a powerful tool."
    " When we make it a habit to focus on things we’re grateful for, it can transform our entire outlook and even ease depression."]

# Convert to string so the curly brackets are not showing
general_meditation_string = " ".join(general_meditation)
meditation_label1_string = " ".join(meditation_label1)
meditation_label2_string = " ".join(meditation_label2)
meditation_label3_string = " ".join(meditation_label3)


def meditations_page():
    global button_1, button_2, button_3, pause_button1, pause_button2, pause_button3
    # Clear all the widgets that were created before
    for i in root.winfo_children():
        i.destroy()

    # Initiate pg mixer
    pg.mixer.init()

    add_image(root, "images/mountains.jpeg", screen_width, screen_height)

    # Create an instruction label
    instruction_label = tk.Label(root,
                                 text=general_meditation_string,
                                 font='arial 17 bold',
                                 bg='#4C213A',
                                 fg='#E47455',
                                 relief='groove',
                                 border=6,
                                 borderwidth=6
                                 )
    instruction_label.place(x=430, y=120)

    meditation1 = tk.Label(root, text=meditation_label1_string,
                           wraplength=750,
                           font='arial 15',
                           bg='#E47455',
                           fg='#4C213A',
                           relief='groove',
                           border=6,
                           borderwidth=8,
                           width=90,
                           height=3)
    meditation1.place(x=300, y=310)

    meditation2 = tk.Label(root, text=meditation_label2_string,
                           wraplength=750,
                           font='arial 15',
                           bg='#E47455',
                           fg='#4C213A',
                           relief='groove',
                           border=6,
                           borderwidth=8,
                           width=90,
                           height=3)
    meditation2.place(x=300, y=490)

    meditation3 = tk.Label(root, text=meditation_label3_string,
                           wraplength=750,
                           font='arial 15',
                           bg='#E47455',
                           fg='#4C213A',
                           relief='groove',
                           border=6,
                           borderwidth=8,
                           width=90,
                           height=3)
    meditation3.place(x=300, y=670)

    label_1 = tk.Label(root, text='Sleep Meditation',
                       font='arial 17 bold',
                       bg='#AD3B49',
                       fg='#4C213A',
                       relief='groove',
                       border=6,
                       borderwidth=6,
                       width=17
                       )
    label_1.place(x=320, y=260)

    label_2 = tk.Label(root, text='Calming Meditation',
                       font='arial 17 bold',
                       bg='#AD3B49',
                       fg='#4C213A',
                       relief='groove',
                       border=6,
                       borderwidth=6,
                       width=17
                       )
    label_2.place(x=320, y=440)

    label_3 = tk.Label(root, text='Gratitude Meditation',
                       font='arial 17 bold',
                       bg='#AD3B49',
                       fg='#4C213A',
                       relief='groove',
                       border=6,
                       borderwidth=6,
                       width=17
                       )
    label_3.place(x=320, y=620)

    button_1 = Button(root, text='▶️',
                      font='arial 15 bold',
                      background='#FF8C00',
                      foreground='#4C213A',
                      border=5,
                      overrelief='raised',
                      overbackground='#AD3B49',
                      highlightthickness='3',
                      highlightcolor='darkred',
                      borderless=1,
                      relief='raised',
                      width=27,
                      command=play_1
                      )
    button_1.place(x=950, y=260)

    button_2 = Button(root, text='▶️',
                      font='arial 15 bold',
                      background='#FF8C00',
                      foreground='#4C213A',
                      border=5,
                      overrelief='raised',
                      overbackground='#AD3B49',
                      borderless=1,
                      highlightthickness='3',
                      highlightcolor='darkred',
                      relief='raised',
                      width=27,
                      command=play_2
                      )
    button_2.place(x=950, y=440)

    button_3 = Button(root, text='▶️',
                      font='arial 15 bold',
                      background='#FF8C00',
                      foreground='#4C213A',
                      border=5,
                      overrelief='raised',
                      overbackground='#AD3B49',
                      borderless=1,
                      highlightthickness='3',
                      highlightcolor='darkred',
                      relief='raised',
                      width=27,
                      command=play_3
                      )
    button_3.place(x=950, y=620)

    pause_button1 = Button(root, text='⏸',
                           font='arial 15 bold',
                           background='#FF8C00',
                           foreground='#4C213A',
                           border=5,
                           overrelief='raised',
                           overbackground='#AD3B49',
                           borderless=1,
                           highlightthickness='3',
                           highlightcolor='darkred',
                           relief='raised',
                           width=27,
                           command=pause_meditation)
    pause_button1.place(x=1020, y=260)

    pause_button2 = Button(root, text='⏸',
                           font='arial 15 bold',
                           background='#FF8C00',
                           foreground='#4C213A',
                           border=5,
                           overrelief='raised',
                           overbackground='#AD3B49',
                           borderless=1,
                           highlightthickness='3',
                           highlightcolor='darkred',
                           relief='raised',
                           width=27,
                           command=pause_meditation)
    pause_button2.place(x=1020, y=440)

    pause_button3 = Button(root, text='⏸',
                           font='arial 15 bold',
                           background='#FF8C00',
                           foreground='#4C213A',
                           border=5,
                           overrelief='raised',
                           overbackground='#AD3B49',
                           borderless=1,
                           highlightthickness='3',
                           highlightcolor='darkred',
                           relief='raised',
                           width=27,
                           command=pause_meditation)
    pause_button3.place(x=1020, y=620)

    menu_buttons()
    exit_button.configure(background='#4C213A')

    extra_menu_buttons()
    meditation_page_button.configure(foreground='white')


# Login or Register Page.
# This section has all the variables and definitions for the Login or Register Page.

# Definition to store the user data
# watch out that there is no space after the comma in the csv file
def enter_user_data():
    # do a user id check
    # read the username column
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    if username.get() in user_ids:
        tk.messagebox.showwarning("Warning", "This username already exists!")
    else:
        # create a dictionary with info from the new user page
        user_data = {"name_of_user": name.get(),
                     "username": username.get()}

        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, mode='a', header=False)

        # create a thankyou label
        thankyou_label = tk.Label(root, text="Your info has been submitted")
        thankyou_label.pack()

        # Call the Login Page for the user to login
        returning_userpage()

# Definition to check for the returning users if they entered the right username
def check_user():
    # read all the usernames
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    # check if username exist
    if user_id.get() in user_ids:
        clear_widgets()
        # calling the journal page()
        journal_entry()
        extra_menu_buttons()
        # calling the extra widgets()
    else:
        tk.messagebox.showwarning("Warning", "This name doesnt exists! Please create an account")


# Create a page for the Users to Register
def create_new_userpage():
    global name, username

    clear_widgets()

    # add an image to my gui
    add_image(root, '../exam/images/lake.jpeg', screen_width, screen_height)

    # create labels and entry boxes
    new_label = tk.Label(root, text='Welcome new user')
    new_label.place(x=700, y=250)

    # user enters name
    name_label = tk.Label(root, text='What is your name?')
    name_label.place(x=400, y=300)

    # entry box
    name = tk.StringVar()
    name_box = tk.Entry(root, textvar=name, fg='white', bg='lightblue')
    name_box.place(x=700, y=300)

    # create a user name
    username_label = tk.Label(root, text='Create a username')
    username_label.place(x=400, y=400)

    username = tk.StringVar()
    username_box = tk.Entry(root, textvar=username, fg='white', bg='lightblue')
    username_box.place(x=700, y=400)

    # create a button to store all the information
    enter_data = tk.Button(root, text='Register', command=enter_user_data)

    enter_data.place(x=700, y=600)

    # Create a button to go back
    back_button = tk.Button(root, text='Go Back', command=login_or_register_page)
    back_button.place(x=700, y=700)

    # creating a new user button
    new_user = tk.Button(root, text='new user',
                         command=create_new_userpage)
    new_user.place(x=500, y=200)

    menu_buttons()


# Create a Page for the returning users to login
def returning_userpage():
    global user_id
    # clear widgets
    clear_widgets()

    # add an image to my gui
    add_image(root, '../exam/images/lake.jpeg', screen_width, screen_height)

    # create labels and entry boxes
    welcomeback_label = tk.Label(root, text='Welcome back user!')
    welcomeback_label.place(x=700, y=200)

    # entry box to ask for the username
    # create a username
    userid_label = tk.Label(root, text='What is your username?')
    userid_label.place(x=600, y=250)

    user_id = tk.StringVar()
    userid_box = tk.Entry(root, textvar=user_id, fg='white', bg='lightblue')
    userid_box.place(x=600, y=300)

    login_button = tk.Button(root, text='Login', command=check_user)
    login_button.place(x=600, y=370)

    # Create a button to go back
    back_button = tk.Button(root, text='Go Back', command=login_or_register_page)
    back_button.place(x=700, y=700)

    # creating an existing user button
    returning_user = tk.Button(root, text='Returning user',
                               command=returning_userpage)
    returning_user.place(x=700, y=200)

    menu_buttons()


# Create a Login or Register Page:
def login_or_register_page():
    # declare variables as global
    global new_user, returning_user

    # clear widgets in the case the widgets have been created
    clear_widgets()

    # add an image to my gui
    add_image(root, '../exam/images/lake.jpeg', screen_width, screen_height)

    # creating a new user button
    new_user = tk.Button(root, text='new user',
                         command=create_new_userpage)
    new_user.place(x=500, y=200)

    # creating an existing user button
    returning_user = tk.Button(root, text='Returning user',
                               command=returning_userpage)
    returning_user.place(x=700, y=200)

    menu_buttons()


# Call the definition that creates the homepage
homepage()

root.mainloop()
