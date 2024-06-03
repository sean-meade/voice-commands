from datetime import date
import os
import speech_recognition as sr
import requests


lat = os.environ.get('LAT')
long = os.environ.get('LONG')
weather_API_key = os.environ.get('weather_API_key')
today = date.today()
print(today)
# Create a Recognizer instance
recognizer = sr.Recognizer()

while(True):
    # Capture audio input from the microphone
    with sr.Microphone() as source:
        print("What do you want?")
        audio_data = recognizer.listen(source)

        # Perform speech recognition using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            if "weather" in text:
                request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={weather_API_key}"
                # request_url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={long}&date={today}&appid={weather_API_key}"
                request = requests.get(request_url)
                print(request.json())
            else:
                print("Could not recognise command")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")