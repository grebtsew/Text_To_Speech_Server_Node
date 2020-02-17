from speaker import speaker
from console import console
from server import server
import pyfiglet

fig = pyfiglet.Figlet(font='standard')
print(fig.renderText('Text to Speech Server Node'))

def main():
    speaker_thread = speaker()

    # Start up queue
    speaker_thread.say("Program started.")

    speaker_thread.say("Terminal is now active.")

    console_thread = console(speaker_thread)
    console_thread.start()

    server_thread = server(speaker_thread)
    server_thread.start()

    speaker_thread.say("Server started.")

    # Start speaking thread
    speaker_thread.start()

if __name__ == '__main__':
    main()
