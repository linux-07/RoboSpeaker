import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

version = 1.01
print(f"Welcome to Robo Speaker {version}")
while True:
    userInp = input("What you want to speak or else type \"00\" to exit: ")
    if userInp == "00":
        speak.Speak("Bye Bye!")
        print(f"Thanks for using Robo Speaker {version}")
        break
    command = speak.Speak(userInp)


