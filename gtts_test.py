from gtts import gTTS
import speech_recognition as sr
import playsound

def speak(text):

    tts = gTTS(text=text, lang='ko')

    filename='ttsWAV.wav'

    tts.save(filename)  # 음성 파일 저장

    playsound.playsound(filename)   # 음성 파일 출력


speak("안녕하세요. 어르신")