#python program to translate
#speech to text and text to speech
import speech_recognition as sr
import pyttsx3

import OS
from dotenv import load_dotenv
load_dotenv[]
OPENAI=os.getenv ('OPENAI_KEY')

import openai
openai.api_key=OPENAI_KEY

#function to convert text to
#speech
def speaktext(command):

    #initiate the engine
    engine = pyttsx3.init()
    engine.say(command):
    engine.RunAndWait()

    #initiate the recognizer
    r=sr.Recognizer()

    def record_text():

        #loop incase of errors
        while(1):
          try():
                #use the microphone as a source of input
                with sr.microphone() as source2:

                    #prepare recognzier to receive input
                    r.adjust_for_ambient_noise (source2, duration=0.2)
                    print("Listening...")

                    #listen for the users input
                    audio = r.listen(source2)

                    #using google to recognize audio
                    MyText =r.recognize_google(audio2)

                    return MyText

except sr.RequestError as a:
print("could not request result; {0}".formart(e))

except sr.UnknownValueError:
print("unknown error occured")

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

response= openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature= 0.5,
    )
messages=response.choice [0].message.content
messages.append[response.choice[0].message]
return message

messages=[{"role": "user", "content": "please act like Jarvis from IronMan"}]
while(1):
        text=record_text()
        messages.append({"role": "user", "content": text})
        response=send_to_chatGPT(messages)
        SpeakText(response)

        print(response)
        
