# Dana-Schoen-tb2-exam
This ReadMe file will give a short summary of my application and instructions on how to execute the code! 

## Free Your Mind 2.0 - Project Description:
"Free Your Mind" is a comprehensive mental wellness application aimed at improving users' mental health and overall well-being.
The app offers a range of features to support users on their wellness journey. Through journaling, users can reflect on their
thoughts and emotions, fostering self-awareness and introspection. Affirmations are available to boost confidence and self-esteem, providing users with positive reinforcement.

The app also serves as an educational resource, offering insights and information on mental health topics, promoting awareness
and understanding. Users can engage with a supportive community, sharing experiences and insights in a safe and welcoming environment.
To aid relaxation and stress relief, the app provides calming music selections and guided meditations, allowing users to unwind and find inner peace.

"Free Your Mind" aims to empower users to take proactive steps towards better mental health, providing tools and resources to support them on their wellness journey.

## Installation
To run the application successfully, several libraries need to be installed beforehand. Most of these libraries we used in class, 
while others I chose to serve extra specific purposes within my application.

* **tkmacosx**: This library is essential for Mac users as it allows the design of customized buttons in tkinter, enhancing the user interface.
* **Pillow**: Used for setting background images in the GUI, providing visual appeal and customization options.
* **Pygame**: Utilized for the Music and Meditations pages, enabling users to play sound within the application.
* **GTTS** (Google Text-to-Speech): Enables text-to-speech conversion, facilitating the application to read affirmations aloud to the user.
* **Pandas**: A powerful dataset library used for storing user information such as names and usernames. This facilitates login and registration functionalities within the application.
Ensure that these libraries are installed using pip or any other package manager before executing the code.


```bash
pip install tkmacosx pillow pygame gtts pandas
```
After installing the required libraries in a virtual environment, users should proceed to clone the entire repository onto 
their local machine. The repository encompasses several crucial components, including:

**Folders:**
* **Image**: Contains images used in the graphical user interface (GUI) to enhance visual elements.
* **Quotes**: Holds quote images utilized within the application.
* **Meditation Music**: Stores music files used for the meditation application.

**Directories:**
* **Data**: Holds any necessary data files used by the application, such as user information or configurations to enable a login or register user flow.
* **Src**: Contains source code files, to ensure that the main Python script (app.py) is being executed flawlessly.

Ensuring that the entire repository is cloned is essential to guarantee the smooth operation of the application. Each component plays a vital role in its functionality and user experience.