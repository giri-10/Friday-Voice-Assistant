import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
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
import pyjokes
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


# sapi5 is a speech api from Microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


#login
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "mvj1" and password == "1234"):
 
        messagebox.showinfo("","Login Success")
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 
root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2
 
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
 
root.mainloop()


#After login success, voice assistant starts
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet user according to the time
def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 15:
        speak("Good afternoon!!")
    elif hour >= 15 and hour < 19:
        speak("Good Evening!!")
    else:
        speak("Good Night!!")

    speak("This is Jarvis . How may I help you?")


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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

temp_variable = 0

if __name__ == "__main__":
    greeting()

    while temp_variable < 1:
        query = takeCommand().lower()
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search google' in query:
            speak('Searching in Google...')
            query = query.replace("search google", "")
            kt.search(query)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open github' in query:
            webbrowser.get(chrome_path).open("github.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open photoshop' in query:
            PPath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
            os.startfile(PPath)

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open spotify' in query:
            webbrowser.get(chrome_path).open("spotify.com")

        elif 'open cyberpunk' in query:
            CPath = "C:\\Program Files\\Cyberpunk.2077.v1.6\\Cyberpunk.2077.v1.6\\REDprelauncher.exe"
            os.startfile(CPath)

        elif 'open control panel' in query:
            os.system("control panel")

        elif 'open calculator' in query:
            os.system("calc")

        elif 'open' and 'website' in query:
            query = query.replace("open" and "website", "")
            dotcom=".com"
            x=query+dotcom
            webbrowser.get(chrome_path).open(x)

        elif 'in maps' in query:
            query = query.replace("search" and "in maps", "")
            driver = webdriver.Chrome(executable_path='C:\\Users\\abhim\\OneDrive\\Desktop\\Project\\Web\\Jarvis\\chromedriver.exe')
            driver.get('https://www.google.com/maps/')
            searchBox = driver.find_element(By.ID, 'searchboxinput').send_keys(query + Keys.ENTER)
            time.sleep(10000)
            driver.quit()

        elif 'todo list' in query:
            #To do list using tkinter 
            # Initializing the python to do list GUI window
            root = Tk()
            root.title('Jarvis To-Do List')
            root.geometry('300x400')
            root.resizable(0, 0)
            root.config(bg="blue")
            # Heading Label
            Label(root, text='TechVidvan Python To Do List', bg='PaleVioletRed', font=("Comic Sans MS", 15), wraplength=300).place(x=35, y=0)
            # Listbox with all the tasks with a Scrollbar
            tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
            scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
            scroller.place(x=260, y=50, height=232)
            tasks.config(yscrollcommand=scroller.set)
            tasks.place(x=35, y=50)
            # Adding items to the Listbox
            with open('tasks.txt', 'r+') as tasks_list:
                for task in tasks_list:
                    tasks.insert(END, task)
                tasks_list.close()
            # Creating the Entry widget where the user can enter a new item
            new_item_entry = Entry(root, width=37)
            new_item_entry.place(x=35, y=310)
            # Creating the Buttons
            add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                            command=lambda: add_item(new_item_entry, tasks))
            add_btn.place(x=45, y=350)
            delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                            command=lambda: delete_item(tasks))
            delete_btn.place(x=150, y=350)
            # Finalizing the window
            root.update()
            root.mainloop()
            # Adding and Deleting items functions
            def add_item(entry: Entry, listbox: Listbox):
                new_task = entry.get()

                listbox.insert(END, new_task)

                with open('tasks.txt', 'a') as tasks_list_file:
                    tasks_list_file.write(f'\n{new_task}')


            def delete_item(listbox: Listbox):
                listbox.delete(ACTIVE)

                with open('tasks.txt', 'r+') as tasks_list_file:
                    lines = tasks_list_file.readlines()

                    tasks_list_file.truncate()

                    for line in lines:
                        if listbox.get(ACTIVE) == line[:-2]:
                            lines.remove(line)
                        tasks_list_file.write(line)

                    tasks_list_file.close()
        elif 'weather report' in query:
                query = query.replace("weather report", "")
                print(query)
                print('Displaying Weather report for: ' + query)

                #fetch the weater details
                url = 'https://wttr.in/{}'.format(query)
                res = requests.get(url)

                #display the result!
                print(res.text)
                speak(res.text)

        #category of jokes: neutral, twister, all
        elif 'tell jokes' in query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(My_joke)
        elif 'todays news' in query:
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
                speak(news.link.text)
                print(news.pubDate.text)
                speak(news.pubDate.text)
                print("-"*60)


        temp_variable += 1
