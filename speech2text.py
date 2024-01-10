import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()

def record_text():
    while(True):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2)
                return myText
        
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            
        except sr.UnknownValueError:
            print("Unknow error occurred")

def output_text():
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(True):
    text = record_text()
    output_text()
    
    print("Wrote text")