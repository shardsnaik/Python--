import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        recognizer.adjust_for_ambient_noise(source)
        audio =recognizer.listen(source)
        try:
            print('Recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" nosncsackn ")

def txt2speech(x):
    engine = pyttsx3.init() 
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty(rate, 110)
    engine.say(x)
    engine.runAndWait()

# speech2tx('If you have gained enough knowledge about the Python programming language and want to get selected by any company at a good salary, this video is for you.')
    
if __name__ == '__main__':
    # if sptext() == 'Nidhi':
        data1 = sptext()
        if "your name" in data1:
             name = 'my name is nidhi'
             txt2speech(name)

        elif 'time' in data1:
             time = datetime.datetime.now().strftime('%I%M%p')
             txt2speech(time)

        elif 'youtube' in data1:
             webbrowser.open('https://www.youtube.com/')
                
