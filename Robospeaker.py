import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()


if __name__ == '__main__':
    print("'Welcome to Robospeaker 1.0 Created by Rammani'")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'q':
            engine.say("Bye bye friends")
            engine.runAndWait()
            break
        
        # Speak the entered text
        engine.setProperty('voice', 'female')  # Choose a voice (e.g., female, male)
        engine.setProperty('rate', 150)  # Set speech rate (e.g., 150 words per minute)
        engine.say(x)
        engine.runAndWait()
