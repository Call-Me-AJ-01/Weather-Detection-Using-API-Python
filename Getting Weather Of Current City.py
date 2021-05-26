import requests
import socket
import pyttsx3 as r
import os
engine = r.init()
engine.setProperty('rate',140)

def speak(text):
    engine.say(text)
    engine.runAndWait()

                        #Checking network Connection
speak("checking for internet connection")

i=0
while True:
    try:
        if socket.create_connection(('google.com',80)):
            speak("System has internet connection")
            speak("initializing weather condition from aj mark 2")
            break
    except:
        if i==0:
            speak("system is not connected to internet")
            speak("please connect the system to internet")
            i+=1
        pass
                        #Getting the City name,lat,log,etc... using ip address

#by default it gives as string in order to convert it as dictionary use json
r=requests.get('http://ipinfo.io/') #getting location etc.... using ip address
#print(r) before converting it to json it will be in sting format
r=r.json()
#print(r) after using json it is converted to dictionary
#print(r['city'])
city=r['city']

                        #Getting the weather condition using city name

r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1384252fb54fcbae2fd7d72d55b07bbc&units=metric').json()
print(r)
temp=r['main']['temp']
desc=r['weather'][0]['description']
humidity=r['main']['humidity']
wind=r['wind']['speed']
speak("initializing weather condition,from AJ mark 2")
speak("Weather condition")
speak("temperature :"+str(temp)+"degree celsius")
speak("Cloud condition, :"+str(desc))
speak("humidity :"+str(humidity))
speak("wind speed :"+str(wind))
