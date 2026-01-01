import pyttsx3
import time
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def print_lyrics():
    lyrics = [
        "Haathon ko sambhale mere haathon mein",
        "Kaise haathon ko sambhale mere haathon mein..",
        "Jab tak neend na aaye, inn lakeeron mein..",
        "Baatein ho........",
        "Haaye"
    ]

    delays = [1.0, 0.1, 1.12, 0.9, 0.8]

    print("Arz kya hai?........\n")
    speak("Arz kya hai")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        # Speak the line
        speak(line)

        # Print typing effect
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        print()  
        time.sleep(delays[i])

# Run the complete function
print_lyrics()
