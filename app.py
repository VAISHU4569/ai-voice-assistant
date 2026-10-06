import speech_recognition as sr
import pyttsx3
import re
import speech_recognition.audio as sr_audio
import os

sr_audio.get_flac_converter = lambda:os.path.abspath("flac.exe")

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def process_command(text):
    if "hello" in text or "hi" in text:
        speak("Hello! I am your student voice assistant.")

    elif "how are you" in text or "how r u" in text:
    
        speak("I am doing great. How can I help you?")

    elif "your name" in text:
        speak("I am your AI voice assistant for students.")

    elif len(re.findall(r"\d+", text)) >= 2:
        numbers = re.findall(r"\d+", text)

        num1 = int(numbers[0])
        num2 = int(numbers[1])

        if "+" in text or "plus" in text:
            answer = num1 + num2

        elif "-" in text or "minus" in text:
            answer = num1 - num2

        elif "*" in text or "x" in text or "multiply" in text or "times" in text:
            answer = num1 * num2

        elif "/" in text or "divide" in text:
            if num2 == 0:
                speak("Sorry, I cannot divide by zero.")
                return
            answer = num1 / num2

        else:
            speak("I understand the numbers, but please tell me the operation.")
            return

        speak(f"The answer is {answer}.")

    elif "bye" in text:
        speak("Goodbye! Have a great day.")

    else:
        speak("I heard you, but I don't know that command yet.")


print("Starting AI Voice Assistant...")

while True:
    try:
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)

        text = recognizer.recognize_google(audio_data).lower()
        print("You said:", text)

        process_command(text)

        if "bye" in text:
            break

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand you.")

    except sr.RequestError as e:
        speak("There was a problem connecting to the speech recognition service.")
        print(e)

    except Exception as e:
        print("Error:", e)