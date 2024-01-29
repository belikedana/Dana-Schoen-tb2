# TODO: clean up code & advance the code

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
from scr.helpers import add_image, clear_widgets, custom_style, customstyle, customstyle_quotes, custom_style2, \
    custom_style3, custom_style_meditations, custom_style_meditations_name, custom_style_meditations_play, \
    recom_list_string, affirmations, list1_string, list2_string, list3_string, image_files, general_meditation_string, \
    meditation_label1_string, meditation_label2_string, meditation_label3_string, feel_good_statements, \
    emergency_contacts_string

# Code to create the gui window
root = tk.Tk()

# Give your gui a title
root.title('Free Your Mind')

# Set the height and width as separate parameters to give you more flexibility
screen_width = 1400
screen_height = 800
# Use the minsize function to set the geometry
root.minsize(screen_width, screen_height)

# Create variables in order to redirect file_path
code_file_path = os.getcwd()

# Create a StringVar to act as the flag to either show the extra menu buttons when logged into account or not
flag = tk.StringVar()
# Initial value is "false"
flag.set("false")

# Initiate pg mixer
pg.mixer.init()


# Definition that creates my exit button and standard menu buttons
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
                             command=music_page)
    playlist_button.place(x=50, y=30)

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
                          command=login_or_register_page)
    login_button.place(x=50, y=80)

    # The standard menu buttons with the custom style
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


# Definition that creates extra feature menu buttons and is being called when user is logged in
def extra_menu_buttons():
    global meditation_page_button

    meditation_page_button = Button(root, text='Meditations',
                                    **custom_style,
                                    foreground='black',
                                    command=meditations_page)
    meditation_page_button.place(x=1200, y=40)


# Homepage Section.
# Here you can find all the definitions, variables, lists that are needed to create the homepage.

# Create an empty label to store the feel good statements in
corner_label = tk.Label()


# This function randomizes the statements from the list and places them in one of the four corners
# Reference: https://stackoverflow.com/questions/64918341/python-tkinter-how-to-adjust-the-x-y-default-0-0-coordinates
def generate_feel_good_statement():
    global corner_label
    # Randomly select a statement from the list
    statement = random.choice(feel_good_statements)
    # Randomly position the label in one of the corners
    x = random.choice([30, root.winfo_width() - 300])
    y = random.choice([30, root.winfo_height() - 50])
    corner_label.place(x=x, y=y)
    # Display the statement in the chosen corner
    corner_label.config(text=statement)
    # forgets the statements after 4000 milliseconds
    root.after(4000, hide_feel_good_statement)


# Definition that the statements disappear after 4 seconds
def hide_feel_good_statement():
    # If a corner label still exists then forget it after 4 seconds
    if corner_label:
        corner_label.place_forget()


# Definition that creates the homepage
def homepage():
    # Declare variable global
    global corner_label

    # Add a background image to my page
    add_image(root, "images/Meditations.png", screen_width, screen_height)

    # The label where the feel good statements appear in
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
                        foreground='black',
                        border=7,
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
                             foreground='black',
                             activebackground='pink',
                             border=8,
                             height=45,
                             width=270,
                             command=journal_entry)
    continue_button.place(x=555, y=670)


# Journal Entry Section
# Here you can find all the definitions, variables, lists that are needed to create the journal entry page.

# Define variables at the module level
recom_label = tk.Label()
entry = tk.Entry()
message_label = tk.Label()


# Definition to safe the entry made in the text file and safe it as journal.txt
# Reference: https://tkdocs.com/tutorial/text.html#basics
def save_entry():
    # retrieves the text entered by the user into the tkinter Text widget named entry, removes any leading or trailing
    # whitespace, and assigns the cleaned text to the variable entry_text for further processing
    entry_text = entry.get("1.0", tk.END).strip()
    # When entered a text into the entry field
    if entry_text:
        # Saves the entry as a file with today's date
        today = date.today()
        entry_date = today.strftime("%d/%m/%Y")
        journal_file = open("journal.txt", "a")
        journal_file.write(f"{entry_date}:\n{entry_text}\n\n")
        journal_file.close()
        # When saved, the entry field gets cleared
        entry.delete("1.0", tk.END)
        # Create message that shows that the entry was saved
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


# Controlling the visibility of the inspiration label
# On a click the user can see the label and with another click can make the label disappear
# Creating a visibility flag
label_visible = False


# Definition to make the label appear when clicked once and disappear when clicked again
# Used later in the Recommendations Page as well
def visibility(label, x_variable, y_variable):
    global label_visible
    if not label_visible:
        label.place(x=x_variable, y=y_variable)
        label_visible = True
    else:
        label.place_forget()
        label_visible = False


# The Definition that creates the Journal Entry page
def journal_entry():
    # Declare all these variables global
    global recom_label, entry, message_label

    # Clear all the widgets that were created before
    clear_widgets(root)

    # Add a background image to your page
    add_image(root, "images/Galaxy2.png", screen_width, screen_height)

    # Entry Introduction label with instructions
    entry_label = tk.Label(root, text='Now you can let all your thoughts go. \n Write your journal entry here:',
                           font='arial 30 bold',
                           bg='pink',
                           fg='black',
                           relief='groove',
                           border=7)
    entry_label.place(x=420, y=150)

    # Text entry field
    entry = tk.Text(root, height=25, width=80, bg='black', fg='white')
    entry.place(x=430, y=300)

    # Save button
    save_button = Button(root, text='Save Entry',
                         font='arial 20 bold',
                         background='grey',
                         foreground='black',
                         border=7,
                         highlightbackground='blue',
                         overbackground='pink',
                         relief='groove',
                         height=30,
                         width=165,
                         command=save_entry)
    save_button.place(x=610, y=650)

    # Add a label filled with journal prompt recommendations and a button that activates the label
    recom_label = tk.Label(root, text=recom_list_string,
                           font='arial 15',
                           relief='sunken',
                           wraplength=200,
                           bg='pink',
                           fg='grey',
                           border=6)

    recom_button = Button(root, text='In need of inspiration?',
                          relief='raised',
                          foreground='black',
                          background='grey',
                          border=5,
                          overforeground='lightblue',
                          command=lambda: visibility(recom_label, 45, 210))
    recom_button.place(x=70, y=160)

    # Message label to display the message that the entry was saved successfully ( mentioned in the save_entry definition)
    message_label = tk.Label(root, text="")

    # Call the definition to create the standard menu buttons
    menu_buttons()

    # The button of the page we are on appears with a white foreground to indicate on which page the user is
    entry_button.configure(foreground='white')

    # If the user is logged in, the flag is true/activated and the user can see the extra menu button
    if flag.get() == 'true':
        extra_menu_buttons()


# Display Affirmations Section.
# Here you can find all the definitions, variables, lists that are needed to create the Affirmations Page.

# Define all the variables on a module level
start_button = Button()
affirmation_label = tk.Label()
# Variable to control the affirmations loop
continue_loop = True

# Empty variable to store the current affirmation in
current_affirmation = ""

# Randomly shuffle the list of affirmations
random.shuffle(affirmations)
# Set the index at 0 to loop through the affirmations
current_affirmation_index = 0


# Definition to change the text to speech and save the affirmations audio
# Reference: https://gtts.readthedocs.io/en/latest/index.html
def convert_text_to_speech(text_to_speak):
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save('affirmation.mp3')
    os.system('afplay affirmation.mp3')


# Definition to display the randomly shuffled affirmation from the list and loop through the list
def display_and_loop_affirmation():
    # Declare variables as global
    global current_affirmation_index, current_affirmation
    # Display randomly shuffled affirmation chosen from list on the label
    current_affirmation = affirmations[current_affirmation_index]
    affirmation_label.config(text=current_affirmation)

    # Convert text to speech and play the affirmation after 2 second
    # Reference: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
    root.after(2000, lambda: convert_text_to_speech(current_affirmation))

    # Increment index for the next affirmation in the list to be displayed and looped through
    # The Modulo operation (%) ensures that when the incremented index exceeds the maximum index (length of the list - 1), it wraps around to 0, effectively creating a loop
    current_affirmation_index = (current_affirmation_index + 1) % len(affirmations)

    # Check if the loop should continue
    if continue_loop:
        # Schedule the next call to display_and_loop_affirmation after 5 seconds
        root.after(5000, display_and_loop_affirmation)


# Definition to stop and restart affirmations
def toggle_affirmations():
    # Declare variable as global
    global continue_loop
    # Toggle the value of continue_loop between True and False
    # Reference: https://docs.python.org/3/library/stdtypes.html#boolean-values
    continue_loop = not continue_loop
    # Update button text based on the current state
    if continue_loop:
        start_button.config(text='Stop Affirmations')
        # When restarting calling the display_and_loop_affirmations definition to start the affirmations again
        display_and_loop_affirmation()

    else:
        start_button.config(text='Start Affirmations')


# Definition that creates the page with the Affirmations
def display_affirmations():
    # Declare all the variables global
    global start_button, affirmation_label

    # Clear all the widgets that were created before
    clear_widgets(root)

    # add a background image to my page
    add_image(root, "images/Aura.jpeg", screen_width, screen_height)

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

    # Affirmation label where the affirmations will appear in later
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

    # Call the definition to display the standard menu buttons
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='blue')

    # The button of the page we are on appears with a white foreground to indicate on which page the user is on
    reminders_button.configure(foreground='white')

    # When user logged in, the flag turns to true and the extra menu buttons appear
    if flag.get() == 'true':
        extra_menu_buttons()


# Recommendations Section.
# Here you can find all the definitions, variables, lists that are needed to create the Recommendations Page.

# Declare all variables on a module level
current_label = tk.Label()
label_button1 = Button()
label_button2 = Button()
label_button3 = Button()
emergency_label = tk.Label()


# Definition to show the selected recommendations in the same label that updates its text
def display_theme(theme_text):
    current_label.config(text=theme_text)
    current_label.place(x=300, y=300)


# This Definition creates the page with the Recommendations
def display_recommendations():
    # Declare all the variables as global
    global current_label, label_button1, label_button2, label_button3, emergency_label
    # Clear all the widgets that were created before
    clear_widgets(root)

    # Add a background image to your page
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
                                 borderwidth=8)
    instruction_label.place(x=330, y=120)

    # Theme selection label
    theme_label = tk.Label(root, text='Choose a medium:',
                           font='arial 17',
                           bg='darkred',
                           fg='darkblue',
                           relief='groove',
                           border=6,
                           borderwidth=8,
                           width=17)
    theme_label.place(x=100, y=210)

    # Create an empty label where the recommendations are displayed in
    current_label = tk.Label(root, text="",
                             wraplength=750,
                             font='arial 15',
                             bg='purple',
                             fg='lightblue',
                             relief='groove',
                             border=6,
                             borderwidth=8)

    # Add recommendation buttons
    label_button1 = Button(root, text='Books', **customstyle, command=lambda: display_theme(list1_string))
    label_button1.place(x=430, y=210)

    label_button2 = Button(root, text='Podcasts', **customstyle, command=lambda: display_theme(list2_string))
    label_button2.place(x=630, y=210)

    label_button3 = Button(root, text='Instagram Accounts', **customstyle, command=lambda: display_theme(list3_string))
    label_button3.place(x=830, y=210)

    # Emergency Contact label and button
    emergency_label = tk.Label(root, text=emergency_contacts_string,
                               font='arial 13',
                               relief='sunken',
                               wraplength=200,
                               bg='darkred',
                               fg='lightblue',
                               border=6)

    emergency = Button(root, text='need help?',
                       font='arial 11',
                       width=80,
                       height=20,
                       relief='groove',
                       background='darkblue',
                       foreground='white',
                       overforeground='darkred',
                       border=7,
                       # Calling the visibility definition created in Journal Entry Page
                       command=lambda: visibility(emergency_label, 55, 550))
    emergency.place(x=110, y=730)

    # Call the definition to create the standard menu buttons
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='darkred')
    # The button of the page we are on appears with a white foreground, so the user knows on which page they are on
    books_button.configure(foreground='white')

    # When user logged in, the extra menu buttons are shown because of the flag being true
    if flag.get() == 'true':
        extra_menu_buttons()


# Quotes Section.
# Here you can find all the definitions, variables, lists that are needed to create the Quotes Page.

# Declare variables on a module level
stop_button = Button()
slideshow_button = Button()
slideshow_label = tk.Label()

# Variable to track the current index of the slideshow
current_index = 0

# Variable to flag the slideshow_id, important to define if the image is changing or not
slideshow_id = None


# Definition to update the slideshow with the next image
def update_slideshow():
    global current_index, slideshow_id

    # Load the images using PIL
    image = Image.open(image_files[current_index])
    image = image.resize((600, 400), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Update the label, where the images are displayed in, with the new image
    slideshow_label.config(image=photo)
    slideshow_label.image = photo

    # Increment the index for the next image; needed so the images move through the slide show (always +1 image)
    current_index += 1
    # Creates a loop and starts from the beginning when all images have been shown already
    if current_index >= len(image_files):
        current_index = 0

    # Schedule the next image after a certain interval (in milliseconds)
    # Changing the value of the variable slideshow_id
    slideshow_id = root.after(4000, update_slideshow)


# Definition to start the slideshow
def start_slideshow():
    if slideshow_id is None:
        update_slideshow()


# Definition to stop the slideshow
def stop_slideshow():
    """
    Using the concept of None as the indicator or the absence of a value; when it is not None then slideshow_id is active.
    Therefor the slideshow is active and in order to stop it, it gets cancelled and then being assigned None as the absence of a value again.
    Enabling the user to start the slideshow again.
    """
    global slideshow_id
    if slideshow_id is not None:
        root.after_cancel(slideshow_id)
        slideshow_id = None


# Definition that creates the Quotes page
def display_quotes():
    # Define all the variables as global
    global stop_button, start_button, slideshow_label
    # Clear all the widgets that were created before
    clear_widgets(root)

    # Add a background image to your page
    add_image(root, "images/Forest2.jpeg", screen_width, screen_height)

    # Create a label to display the images in
    slideshow_label = tk.Label(root, border=8, text='The Quotes-Slideshow will appear here, once you press start:',
                               font='arial 17 ', bg='green', fg='white', relief='groove')
    slideshow_label.place(x=400, y=200)

    # Create start and stop buttons
    start_button = Button(root, text='Start',
                          **customstyle_quotes,
                          command=start_slideshow)
    start_button.place(x=550, y=700)

    stop_button = Button(root, text='Stop',
                         **customstyle_quotes,
                         command=stop_slideshow)
    stop_button.place(x=720, y=700)

    # Call the definition to create the standard menu buttons
    menu_buttons()
    # Reconfigure the exit buttons background color to match the vibe of each page
    exit_button.configure(background='darkgreen')
    # The button of the page we are on appears with a white foreground to indicate on which page the user is
    quotes_button.configure(foreground='white')

    # When user logged in and therefore the flag is being true, the extra menu buttons are shown
    if flag.get() == 'true':
        extra_menu_buttons()


# Music Page Section.
# Here you can find all the definitions, variables, lists that are needed to create the Music Page.

# Declare all variables on a module level
play_button = Button()
pause_button = Button()
play_list = tk.Listbox()
# Store the song name as a variable
song_name = tk.StringVar()


# Definition that opens Spotify in the browser
def select_spotify():
    webbrowser.open('https://open.spotify.com')


# Definition that makes it possible to select music from your own directory, therefore lets you create your own playlist
def select_music():
    # Create the  directory box
    directory = askdirectory()
    os.chdir(directory)
    # Gives the user all the songs in the folder they selected
    song_list = os.listdir()

    # Loop through the song list and insert into the song box
    pos = 0
    for song in song_list:
        play_list.insert(pos, song)
        pos += 1


# Definition that clears the songs in the ListBox
def clear_tracks():
    # Show a warning message when pushing the button and the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "Playlist is empty.")
        return

    # Clears all the tracks starting with the index 0 (the first item on the list) and ending at the end
    play_list.delete(0, tk.END)
    # The song name is being replaced by an empty variable
    song_name.set("")
    # Stop the music playing when cleared
    pg.mixer.music.stop()


# Definition that makes the music play
def play_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return
    # Loads the music files and activates them to listening to them
    pg.mixer.music.load(play_list.get(tk.ACTIVE))
    # Plays the music
    pg.mixer.music.play()


def play_on_selection():
    # Calls the definition that calls the definition to play the music
    play_music()


# Definitions that make the music stop, pause and unpause
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
    # Configure the pause button into the unpause button
    pause_button.configure(text='Unpause',
                           command=unpause_music)


def unpause_music():
    # Show a warning message when the ListBox is empty and/or no song is selected
    if play_list.size() == 0:
        messagebox.showwarning("Warning", "No music selected. Please choose a song.")
        return

    pg.mixer.music.unpause()
    # Configure the unpause button into the pause button
    pause_button.configure(text='Pause',
                           command=pause_music)


# Definition that creates the music page
def music_page():
    global play_button, stop_button, pause_button, play_list, song_name
    # Clear all the widgets that were created before
    clear_widgets(root)

    # Add a background image to your page
    add_image(root, "images/house.jpeg", screen_width, screen_height)

    # Create a label that gives information on the music selection
    intro_label = tk.Label(root,
                           text="Welcome to the Music Selection Section. \n Why don't you put on some music while browsing through the app? \n"
                                "\n" "You can either select a pre-made playlist from Spotify or create your own.",
                           font='arial 20 bold',
                           relief='groove',
                           bg='#67729D',
                           fg='#BB9CC0',
                           border=5)
    intro_label.place(x=350, y=170)

    # Create a button redirects you to spotify
    select_playlist = Button(root, text='Select Playlist',
                             **custom_style2,
                             command=select_spotify)
    select_playlist.place(x=200, y=400)

    # Create a button to activates the music selection process from your own directory
    create_playlist = Button(root, text='Create Playlist',
                             **custom_style2,
                             command=select_music)
    create_playlist.place(x=200, y=500)

    # Buttons that play, stop and pause the music and place them
    play_button = Button(root, text='Play',
                         width=120,
                         height=30,
                         **custom_style3,
                         command=play_music)
    play_button.place(x=1100, y=350)

    stop_button = Button(root, text='Stop',
                         width=120,
                         height=30,
                         **custom_style3,
                         command=stop_music)
    stop_button.place(x=1100, y=450)

    # Pause button doesn't get parameters height and width because it makes the Button grow
    pause_button = Button(root, text='Pause',
                          **custom_style3,
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

    # Call the definition to create the standard menu buttons
    menu_buttons()

    # When user logged in, the flag is defined true and the extra menu buttons will show
    if flag.get() == 'true':
        extra_menu_buttons()


# Meditations Page.
# Here you can find all the definitions, variables, lists that are needed to create the Meditations Page.

# Definitions to pause, unpause and stop the meditations
def pause_meditation():
    pg.mixer.music.pause()

    # Configure the pause button to the unpause button
    pause_button1.configure(text='UNPAUSE',
                            command=unpause_meditation)


def unpause_meditation():
    pg.mixer.music.unpause()

    # Configure the unpause button to the pause button
    pause_button1.configure(text='PAUSE',
                            command=pause_meditation)


def stop_meditation():
    pg.mixer.music.stop()


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


# The Definition that creates the Meditation Page
def meditations_page():
    global button_1, button_2, button_3, pause_button1, pause_button2, pause_button3
    # Clear all the widgets that were created before
    clear_widgets(root)

    add_image(root, "images/mountains.jpeg", screen_width, screen_height)

    # Create an instruction label
    instruction_label = tk.Label(root, text=general_meditation_string,
                                 font='arial 17 bold',
                                 bg='#4C213A',
                                 fg='#E47455',
                                 relief='groove',
                                 border=6,
                                 borderwidth=6)
    instruction_label.place(x=430, y=120)

    # Meditation labels that display the texts
    meditation1 = tk.Label(root, text=meditation_label1_string, **custom_style_meditations)
    meditation1.place(x=300, y=310)

    meditation2 = tk.Label(root, text=meditation_label2_string, **custom_style_meditations)
    meditation2.place(x=300, y=490)

    meditation3 = tk.Label(root, text=meditation_label3_string, **custom_style_meditations)
    meditation3.place(x=300, y=670)

    # Labels that display the names of the meditations
    label_1 = tk.Label(root, text='Sleep Meditation',
                       **custom_style_meditations_name)
    label_1.place(x=320, y=260)

    label_2 = tk.Label(root, text='Calming Meditation',
                       **custom_style_meditations_name)
    label_2.place(x=320, y=440)

    label_3 = tk.Label(root, text='Gratitude Meditation',
                       **custom_style_meditations_name)
    label_3.place(x=320, y=620)

    # Buttons that play the meditations
    button_1 = Button(root, text='▶PLAY',
                      **custom_style_meditations_play,
                      command=play_1)
    button_1.place(x=990, y=260)

    button_2 = Button(root, text='▶PLAY',
                      **custom_style_meditations_play,
                      command=play_2)
    button_2.place(x=990, y=440)

    button_3 = Button(root, text='▶PLAY',
                      **custom_style_meditations_play,
                      command=play_3)
    button_3.place(x=990, y=620)

    # Pause button to pause the meditations
    pause_button1 = Button(root, text='PAUSE',
                           **custom_style_meditations_play,
                           command=pause_meditation)
    pause_button1.place(x=1250, y=460)

    # Stop button to stop the meditations
    stop_button1 = Button(root, text='STOP',
                          **custom_style_meditations_play,
                          command=stop_meditation)
    stop_button1.place(x=1250, y=520)

    # Calling the definition to display the standard menu buttons
    menu_buttons()
    # Configure the exit button to match the vibe of the page
    exit_button.configure(background='#4C213A')

    # When on the extra page, display also the extra menu buttons
    extra_menu_buttons()
    # Configure the foreground of the page to indicate the user on which page they are
    meditation_page_button.configure(foreground='white')


# Login or Register Page.
# Here you can find all the definitions, variables, lists that are needed to create the Login or Register Page.

# Definition to store the user data and let the user register with a new username
# watch out that there is no space after the comma in the csv file!
def enter_user_data():
    # Read the username column to either accept new username or decline already existing usernames when creating a new account
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    # Showing warning messages when the username already exists or when no username is entered
    if username.get() in user_ids:
        tk.messagebox.showwarning("Warning", "This username already exists!")
    # When no username entered a warning message will be shown to the user
    elif not username.get():
        tk.messagebox.showwarning("Warning!", "Please enter a username")
    else:
        # create a dictionary with info from the new user in the csv file
        user_data = {"name_of_user": name.get(),
                     "username": username.get()}

        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, mode='a', header=False)

        # Call the Login Page for the user to login; the user cannot enter the premium content without logging in
        login_or_register_page()


# Definition to check that the entered username exists when logging in
def check_user():
    # Read all the usernames
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    # Check if username exist
    # If yes set the flag to true and therefore enable the extra menu buttons to be shown
    if user_id.get() in user_ids:
        clear_widgets(root)
        flag.set("true")
        # Call the journal entry page when username exists
        journal_entry()
    else:
        # If no, then the user gets shown this warning message
        tk.messagebox.showwarning("Warning", "This username doesnt exists! Please create an account!")


# Create a page for the new Users to Register (Create an Account Page)
def create_new_userpage():
    # Declare these variables global
    global name, username

    # Clear all the widgets used before
    clear_widgets(root)

    # Add a background image to my gui
    add_image(root, "images/lake.jpeg", screen_width, screen_height)

    # Create labels and entry boxes to enter the username and name of the user
    new_label = tk.Label(root, text='Welcome new user!',
                         relief='flat',
                         font='arial 25 bold',
                         background='#6C4558',
                         foreground='#B9A0AB',
                         border=5)
    new_label.place(x=580, y=220)

    # User asked for his name
    name_label = tk.Label(root, text='What is your name?',
                          relief='raised',
                          font='arial 17 bold',
                          background='#363651',
                          foreground='#B9A0AB',
                          border=6,
                          width=18)
    name_label.place(x=600, y=300)

    # Entry box to enter the name
    name = tk.StringVar()
    name_box = tk.Entry(root, textvar=name, bg='#363651', fg='lightblue', width=23)
    name_box.place(x=600, y=350)

    # Ask for the users username
    username_label = tk.Label(root, text='Create a username',
                              relief='raised',
                              font='arial 17 bold',
                              background='#363651',
                              foreground='#B9A0AB',
                              border=6,
                              width=18)
    username_label.place(x=600, y=420)

    # Entry Box to enter the username
    username = tk.StringVar()
    username_box = tk.Entry(root, textvar=username, bg='#363651', fg='lightblue', width=23)
    username_box.place(x=600, y=480)

    # Create a button to store all the new information in the cvs file
    enter_data = Button(root, text='REGISTER',
                        relief='sunken',
                        font='arial 15 bold',
                        background='#B9A0AB',
                        foreground='#4C213A',
                        border=5,
                        overbackground='#273852',
                        command=enter_user_data)
    enter_data.place(x=645, y=550)

    # Create a button to go back to the Register Page
    back_button = Button(root, text='Go Back',
                         relief='sunken',
                         font='arial 15 bold',
                         background='#B9A0AB',
                         foreground='#4C213A',
                         border=5,
                         overbackground='#273852',
                         command=login_or_register_page)
    back_button.place(x=650, y=680)

    # Call the definition of the menu buttons, so that they appear at the top
    menu_buttons()


# Create a Login or Register Page; this is the first page that is being shown when trying to LOGIN
def login_or_register_page():
    # Declare variables as global
    global new_user, returning_user, user_id

    # Clear widgets in the case the widgets have been created
    clear_widgets(root)

    # Add a background image to my gui
    add_image(root, "images/lake.jpeg", screen_width, screen_height)

    # Creating a button to register
    new_user = Button(root, text='CREATE AN ACCOUNT',
                      relief='sunken',
                      font='arial 15 bold',
                      background='#B9A0AB',
                      foreground='#4C213A',
                      border=5,
                      overbackground='#273852',
                      command=create_new_userpage)
    new_user.place(x=610, y=650)

    # Label to create an account
    createacc_label = tk.Label(root, text='New here?',
                               relief='raised',
                               font='arial 15 bold',
                               background='#363651',
                               foreground='#B9A0AB',
                               border=5)
    createacc_label.place(x=660, y=600)

    # Creating a LOGIN button
    returning_user = Button(root, text='LOGIN',
                            relief='sunken',
                            font='arial 15 bold',
                            background='#B9A0AB',
                            foreground='#4C213A',
                            border=5,
                            overbackground='#273852',
                            command=check_user)
    returning_user.place(x=660, y=455)

    # Create a welcome back label
    welcomeback_label = tk.Label(root, text='Welcome back user!',
                                 relief='flat',
                                 font='arial 25 bold',
                                 background='#6C4558',
                                 foreground='#B9A0AB',
                                 border=5)
    welcomeback_label.place(x=580, y=220)

    # Label to ask the user for the username
    userid_label = tk.Label(root, text='What is your username?',
                            relief='raised',
                            font='arial 17 bold',
                            background='#363651',
                            foreground='#B9A0AB',
                            border=6,
                            width=23)
    userid_label.place(x=580, y=320)

    # Entry box to enter the username
    user_id = tk.StringVar()
    userid_box = tk.Entry(root, textvar=user_id, bg='#363651', fg='lightblue', width=23)
    userid_box.place(x=610, y=380)

    # Call the definition for the menu buttons to appear on the page
    menu_buttons()


# Call the definition that creates the homepage as the first page in the gui
homepage()

root.mainloop()
