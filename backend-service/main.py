'''from utils.speech_input import listen
from utils.text_output import speak
from utils.intent_handler import handle_command



if __name__ == "__main__":
    speak("Hello! I am your voice assistant. Say something.")
    
    while True:
        command = listen()

        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command:
            handle_command(command)'''

'''#For Mobile
from utils.speech_input import listen
from utils.text_output import speak
from utils.intent_handler import handle_command

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. Say something.")

    while True:
        command = listen()

        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command:
            handle_command(command)'''

