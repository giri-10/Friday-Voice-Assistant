import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit as kt
from selenium import webdriver
import time
from tkinter import *
from tkinter import messagebox
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import sys
from dadjokes import Dadjoke

#Setting up voice from Microsoft
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Login_Info():
    user_name = e1.get()
    password = e2.get()
 
    if(user_name == "" and password == "") :
        messagebox.showinfo("", "Please enter username and password")
 
 
    elif(user_name == "mvj1" and password == "1234"):
 
        messagebox.showinfo("","Login Successful!")
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrect Username and Password")

def on_close():
    response = messagebox.showwarning('Warning','Please enter correct login details')
 
root = Tk()
root.title("Login: Friday")
# root.iconbitmap(r'C:\\Users\\abhim\\OneDrive\\Desktop\\Project\\Web\\Jarvis\\jarvisLogo.ico') 
root.iconbitmap(r'C:\\Users\\Giridharan U\\Downloads\\fridayLogo.ico')

root.protocol('WM_DELETE_WINDOW',on_close)


root.geometry("450x250")
global e1
global e2
 
Label(root, text="User name").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Login_Info ,height = 2, width = 10).place(x=10, y=100)
 
root.mainloop()

#After login success, voice assistant starts

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    '''
    Function to greet user according to the time
    '''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
        print("Good Morning!!")
    elif hour >= 12 and hour < 15:
        speak("Good afternoon!!")
        print("Good afternoon!!")
    elif hour >= 15 and hour < 19:
        speak("Good Evening!!")
        print("Good Evening!!")
    else:
        speak("Good Night!!")
        print("Good Night!!")

    speak("This is Friday, how may I help you?")
    print("This is Friday, how may I help you?")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

speak_count = 0

if __name__ == "__main__":
    '''
    This is the main function of the program
    '''
    greeting()

    while speak_count < 1:
        user_command = takeCommand().lower()
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        # Logic for executing tasks based on query
        if 'wikipedia' in user_command:
            speak('Searching Wikipedia...')
            user_command = user_command.replace("wikipedia", "")
            results = wikipedia.summary(user_command, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search google' in user_command:
            speak('Searching in Google...')
            user_command = user_command.replace("search google", "")
            kt.search(user_command)

        elif 'open youtube' in user_command:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in user_command:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open github' in user_command:
            webbrowser.get(chrome_path).open("github.com")

        elif 'time' in user_command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'play music' in user_command:
            # music_dir = 'C:\\Music'
            music_dir = 'C:\\Users\\Giridharan U\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open spotify' in user_command:
            webbrowser.get(chrome_path).open("spotify.com")

        elif 'open control panel' in user_command:
            os.system("control panel")

        elif 'open calculator' in user_command:
            os.system("calc")

        elif 'website' in user_command:
            user_command = user_command.replace("website", "")
            dotcom=".com"
            x=user_command+dotcom
            webbrowser.get(chrome_path).open(x)

        elif 'in maps' in user_command:
            user_command = user_command.replace("search" and "in maps", "")
            # driver = webdriver.Chrome(executable_path='C:\\Users\\abhim\\OneDrive\\Desktop\\Project\\Web\\Jarvis\\chromedriver.exe')
            driver = webdriver.Chrome(executable_path='C:\\Users\\Giridharan U\\Desktop\\Python\\Jarvis\\chromedriver.exe')
            driver.get('https://www.google.com/maps/')
            searchBox = driver.find_element(By.ID, 'searchboxinput').send_keys(user_command + Keys.ENTER)
            time.sleep(100)
            driver.quit()

        # elif 'send whatsapp message' or 'send a whatsapp message' in user_command:
        #     speak('Enter phone number to text including country code:')
        #     whatsapp_no = str(input('Enter phone number to text including country code:'))
        #     textMsg = str(takeCommand().lower())
        #     #textMsg= str(input("Enter text:"))
        #     kt.sendwhatmsg(whatsapp_no, textMsg , 6, 29)
   

        elif 'tell jokes' in user_command:
            dadjoke = Dadjoke()
            print(dadjoke.joke)
            speak(dadjoke.joke)

        elif 'news' in user_command:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list:
                print(news.title.text)
                speak(news.title.text)
                print(news.link.text)
                print(news.pubDate.text)
                speak(news.pubDate.text)
                print("-"*60)
        
        elif 'weather' in user_command:
            user_command = user_command.replace("weather", "")
            print(user_command)
            print('Displaying Weater report for: ' + user_command)
            url = 'https://wttr.in/{}'.format(user_command)
            res = requests.get(url)
            print(res.text)

        elif 'memo' in user_command:

            def newTask():
                task = my_entry.get()
                if task != "":
                 lb.insert(END, task)
                 my_entry.delete(0, "end")
                else:
                 messagebox.showwarning("WARNING", "Please enter some task")

            def deleteTask():
                lb.delete(ANCHOR)
    
            root = Tk()
            # ws.geometry('500x450+500+200')
            root.geometry('800x650+800+400')
            root.title('To Do List: Friday')
            root.config(bg='#223441')
            root.resizable(width=False, height=False)

            frame = Frame(root)
            frame.pack(pady=10)

            lb = Listbox(
                frame,
                width=25,
                height=8,
                font=('Times', 18),
                bd=0,
                fg='#464646',
                highlightthickness=0,
                selectbackground='#a6a6a6',
                activestyle="none",
                )
            lb.pack(side=LEFT, fill=BOTH)

            task_list = []

            for item in task_list:
                lb.insert(END, item)

            sb = Scrollbar(frame)
            sb.pack(side=RIGHT, fill=BOTH)

            lb.config(yscrollcommand=sb.set)
            sb.config(command=lb.yview)

            my_entry = Entry(
                root,
                font=('times', 24)
                )

            my_entry.pack(pady=20)

            button_frame = Frame(root)
            button_frame.pack(pady=20)

            addTask_btn = Button(
                button_frame,
                text='Add Task',
                font=('times 14'),
                bg='#c5f776',
                padx=20,
                pady=10,
                command=newTask
            )
            addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

            delTask_btn = Button(
                button_frame,
                text='Delete Task',
                font=('times 14'),
                bg='#ff8b61',
                padx=20,
                pady=10,
                command=deleteTask
            )
            delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
            root.mainloop()

        elif 'send whatsapp message' in user_command:
              kt.sendwhatmsg("+919980833407","Automated msg", 18, 37)

        else:
            print("Wrong command")
            speak("Wrong command")
        speak_count += 1
