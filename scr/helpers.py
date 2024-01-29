import tkinter as tk
from PIL import Image, ImageTk
import os

# Create variables in order to redirect file_path
code_file_path = os.getcwd()


# This definition will place the image on the gui window.
def add_image(root, image_file_path, width, height):
    # Reset the file path to find the images as uploading the music breaks the flow
    os.chdir(code_file_path)

    img = Image.open(image_file_path)
    img = img.resize((width, height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)


# Definition to clear all the widgets created before
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()


# All the Custom Styles I created for buttons that use the same design
# Create a custom style for the menu buttons
custom_style = dict(relief='raised', background='lightblue', border=7, highlightcolor='white',
                    highlightthickness=4, overbackground='lightgreen', font='arial 17 bold', width=165, height=30)

# Create custom style for recommendations buttons on the Recommendations Page
customstyle = dict(font='arial 15 bold', background='darkblue', foreground='white', border=7, overrelief='raised',
                   overforeground='darkred', highlightthickness='4', highlightcolor='darkred', relief='raised')

# CustomStyle for the Start and Stop Buttons on the Slideshow Page
customstyle_quotes = dict(relief='raised', font='arial 15 bold', background='darkgreen', foreground='white',
                          width=90, height=30, border=6, highlightthickness=4, highlightcolor='white',
                          overbackground='lightgreen')

# CustomStyle for the playlist buttons on the Playlist Page
custom_style2 = dict(font='arial 17 bold', width=150, height=30, relief='raised', border=5,
                     background='#BB9CC0', foreground='black', overbackground='#E7BCDE')

# CustomStyle for the play, pause and stop button on the Playlist Page
custom_style3 = dict(font='arial 17 bold', background='#E7BCDE', relief='raised', border=5,
                     foreground='black', overbackground='#BB9CC0', highlightthickness=4, highlightcolor='#7C93C3')

# CustomStyle for the Meditation Labels on the Meditations Page
custom_style_meditations = dict(wraplength=750, font='arial 15', bg='#E47455', fg='#4C213A',
                                relief='groove', border=6, borderwidth=8, width=90, height=3)

# CustomStyle for the Name Labels on the Meditations Page
custom_style_meditations_name = dict(font='arial 17 bold', bg='#AD3B49', fg='#4C213A', relief='groove',
                                     border=6, borderwidth=6, width=17)

# CustomStyle for the Play, Pause and Stop Buttons on the Meditations Page
custom_style_meditations_play = dict(font='arial 12 bold', background='#AD3B49', foreground='#FF8C00', border=5,
                                     overrelief='raised', overbackground='#4C213A', highlightthickness='4',
                                     highlightcolor='darkred', relief='raised')


# Lists I created that I included into the helpers file because they were taking up to much space in the main file

# Creating a list that will be displayed in a label for some inspirational journal prompts (Journal Page)
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

# List with all the affirmations (Affirmations Page)
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

# Create lists containing the different recommendations that are being displayed on the Recommendations page
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

# List of image filenames for the slideshow (Slideshow Page)
image_files = ["quotes/1.jpeg", "quotes/2.jpeg", "quotes/3.jpeg", "quotes/4.jpeg", "quotes/5.jpeg", "quotes/6.jpeg",
               "quotes/7.jpeg", "quotes/8.jpeg", "quotes/9.jpeg", "quotes/10.jpeg", "quotes/11.jpeg",
               "quotes/12.jpeg", "quotes/13.jpeg", "quotes/14.jpeg", "quotes/15.jpeg", "quotes/16.jpeg",
               "quotes/17.jpeg", "quotes/18.jpeg", "quotes/19.jpeg", "quotes/20.jpeg", "quotes/21.jpeg",
               "quotes/21.jpeg", "quotes/22.jpeg", "quotes/23.jpeg", "quotes/24.jpeg", "quotes/25.jpeg"]


# Texts for the Meditation Labels (Meditation Page)
general_meditation = [
    "Meditation has many benefits. It reduces stress, increases calm \n and focus, and promotes greater "
    "physical and emotional well-being. \n Anyone can do it, and the rewards can come quickly. \n These guided "
    "meditations will help you get started."]

meditation_label1 = [
    "This bedtime sleep meditation uses deep breathing, mindfulness, and body scan techniques to help"
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

# List with all the statements (intro page)
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


# Emergency phone number list (Recommendations Page)
emergency_contacts = ["Telefon-Seelsorge (DE):\n0800 1110 111 \n"
                      "Children and Teenage-Hotline:\n116111 \n"
                      "Domestic Violence-Hotline:\n116 016"]

# Getting rid of the curly brackets that are being displayed by converting to a string
emergency_contacts_string = " ".join(emergency_contacts)