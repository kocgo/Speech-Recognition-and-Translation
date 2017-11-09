import speech_recognition as sr
from googletrans import Translator
import pyperclip
import winsound

r = sr.Recognizer()

# Speech Recognation API Here
audio = 0
method = r.recognize_google

# The speech will be translated into the target language
target_language = "pl"

# Speech Text and Translated Text will be stored in that file
log_file = "LogFile.txt"

# There will be a success beep after each translation
beep_sound = False

def listening():

    while True:

        with sr.Microphone() as source:
            print("-------")
            audio = r.listen(source)

            try:
                print(method(audio))
                with open(log_file, "a+") as speechfile:

                    speechfile.write('\n' + method(audio))
                    translatedtext = Translator().translate(method(audio), dest=target_language).text
                    print(translatedtext)
                    pyperclip.copy(translatedtext)
                    speechfile.write(" ---> " + translatedtext.encode('utf-8'))
                    if beep_sound: beep()

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


def beep():
    duration = 300  # millisecond
    freq = 500  # Hz
    winsound.Beep(freq, duration)

if __name__ == "__main__":
    listening()