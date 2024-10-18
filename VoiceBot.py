import pyttsx3
import speech_recognition as sr

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to make the bot speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak into the microphone.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust to background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-IN')  # Recognize speech
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        speak("Sorry, I'm unable to reach the speech recognition service.")
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        speak("An error occurred.")
        print(f"An error occurred: {e}")
        return None

# Main chatbot loop
if __name__ == '__main__':
    speak("Welcome to Voicebot 1.0 created by Rammani Pandey")
    
    while True:
        speak("How can I help you?")
        user_input = listen()  # Capture voice input

        if user_input is None:
            continue  # If speech is not recognized, keep listening
        
        user_input = user_input.lower()

        if 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
            speak("Bye bye, friend! Take care!")
            break

        elif 'your name' in user_input:
            speak("My name is Voicebot 1.0, created by Rammani Pandey.")
        
        elif 'how are you' in user_input:
            speak("I'm just a program, but I'm doing fine! How about you?")
        
        elif 'time' in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The current time is {current_time}")

        else:
            speak("I didn't understand that. Could you please ask again?")
