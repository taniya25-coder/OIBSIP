import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

#Text to speech engine initialization
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)  #0 for male 1 for female
engine.setProperty('rate',170)  #Speed of speech

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio=r.listen(source,timeout=5,phrase_time_limit=5)
            command=r.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except sr.WaitTimeOutError:
            print("Listening timed out.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""
        #Main execution loop
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""


if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        query = listen_command()

        if not query:
            continue

        #1. Respond to hello
        if "hello" in query or "hi" in query:
            speak("Hello! Nice to hear from you. How can I assist you today?")

        #2. Tell the current time
        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {str_time}")

        #3. Tell the current date
        elif "date" in query:
            str_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {str_date}")

        #4. Open a website
        elif "search" in query or "open google" in query:
            speak("What do you want to search for?")
            search_query = listen_command()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {search_query} on Google.")

        #5. Exit the assistant
        elif "exit" in query or "bye" in query or "stop" in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I am not programmed for that command yet,but you can ask me for"
                  " the time, date, or to search something on Google.")
                 


 