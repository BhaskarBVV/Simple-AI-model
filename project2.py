import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Mr.Bhaaskar")
    elif hour>=12 and hour<18:
        speak("Good afternoon Mr.Bhaskar")
    else:
        speak("Good evening Mr.Bhaskar")
    speak("I'm Elissa, how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio= r.listen(source)
    
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: ", query)

    except Exception as e:
        print(e)
        print("Say that again..")
        return "None"
    return query   

def musc():
    music='F:\\rock'
    songs=os.listdir(music)
    os.startfile(os.path.join(music, songs[random.randint(1,135)]))

def get_price(url): 
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser') 
    ans = soup.find("div", class_ = 'dailyGoldrate').text
    return ans

def search_file(search_input):
    listing = os.walk("E:/")
    listing2= os.walk("F:/")
    found=False
    x=1
    file_list=[]
    for root_path in listing:
        for directories in root_path:
            for files in directories:
                if search_input in files.lower():
                    if found==False:
                        print("These are the matching files:\n")
                        speak("these are the matching files")
                    found=True
                    z=os.path.join(root_path[0],files)
                    print(x," ",files)
                    file_list.append(z)
                    z=""
                    x=x+1
    for root_path in listing2:
        for directories in root_path:
            for files in directories:
                if search_input in files.lower():
                    found=True
                    z=os.path.join(root_path[0],files)
                    print(x," ",files)
                    file_list.append(z)
                    z=""
                    x=x+1
    if found==True:
        print("Enter the file number to open and 0 to exit")
        speak("Enter the file number to open and 0 to exit")
        file_number=int(input())
        if file_number!=0:
            os.startfile(file_list[file_number-1])
        if found==False:
            print("Opps, No such matching file found!")
            speak("Opps, no such matching file found")

if __name__ == "__main__":
    speak("hello,")
    wishMe()
    
    while True:
        query=takeCommand().lower()

        if'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia: ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'facebook' in query:
            speak("opening Facebook")
            webbrowser.open("https://www.facebook.com/")
        elif 'twitter' in query:
            speak("opening Twitter")
            webbrowser.open("https://twitter.com/?lang=en")
        elif 'codeforces' in query:
            speak("opening codeforces")
            webbrowser.open("https://codeforces.com/")
        elif 'whatsapp' in query:
            speak("opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com/")    
        elif 'codechef' in query:
            speak("opening Codechef")
            webbrowser.open("https://www.codechef.com/")
        elif 'music' in query:
            musc()
            speak("Playing Music from PC")
        elif 'google search' in query:
            query=query.replace('google search',"")
            speak("opening google search results")
            webbrowser.open('https://google.com/?#q='+query)
        elif 'youtube search' in query:
            query=query.replace('youtube search',"")
            speak("opening youtube search results")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif 'time now' in query:
            curent_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is")
            speak(curent_time)
        elif 'vs code' in query:
            vs_path="C:\\Users\\Bhaskar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening Visual studio code")
            os.startfile(vs_path)
        elif 'ms word' in query:
            ms_path="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("opening Microsoft office Word")
            os.startfile(ms_path)
        elif 'moodle' in query:
            speak("Opening moodle")
            webbrowser.open("http://moodleglbitm.live:9091/my/")
        elif 'verbal' and  'moodle' in query:
            speak("Opening moodle")
            webbrowser.open("http://lms.glbitm.org:9099/moodle/login/index.php")
        elif 'feeling bored' in query:
            speak('Wait, would you like to listen songs, or play games')
            problem=takeCommand().lower()
            if 'song' in problem:
                speak("don't worry i'm playing music") 
                musc()
            elif 'game' in problem:
                speak("don't worry, which game would you like to play")
                print('POOL')
                print("CHESS")
                speak("chesss or pool")
                game=takeCommand().lower()
                if 'chess' in game:
                    webbrowser.open("https://www.chess.com/play/computer")
                    speak("Wooooooohhhh, let's play chess")
                elif 'pool' in game:
                    webbrowser.open("https://www.miniclip.com/games/8-ball-pool-multiplayer/en/")
                    speak("Woooooh, let's play Pool")
        elif 'gold rate' in query:
            ans = get_price("https://www.policybazaar.com/gold-rate/") 
            print(f'{ans} per 10 gram')
            speak(ans)
        elif 'map' in query:
            speak("Tell me the location please")
            loc=takeCommand().lower()
            speak(f"opening map of {loc}")
            loc.replace(" ","+")
            webbrowser.open("https://www.google.com/maps/place/"+loc)
        elif 'mail' in query:
            speak("openning your inbox")
            print("openning your inbox")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
        elif 'search file' in query:
            print("enter the file name: ")
            speak("enter the file name")
            file_name=input().lower()
            search_file(file_name)
        elif 'break' or 'stop' in query:
            break   