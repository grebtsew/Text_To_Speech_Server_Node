from gtts import gTTS
from datetime import datetime


def save_text_as_audio(text):
    """
    Save text as an audio file using Google Text-to-Speech.

    Args:
        text (str): The text to be converted to speech and saved.

    Returns:
        str: The filename of the saved audio file.
    """
    # Generate filename based on current date and time
    now = datetime.now()
    file_name = "recordings/" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".mp3"

    # Convert text to speech using Google Text-to-Speech
    tts = gTTS(text=text, lang="en")

    # Save the speech as an audio file
    tts.save(file_name)

    print("File saved:", file_name)
    return file_name


# Example usage:
# text_to_save = "Hello, world!"
# saved_file = save_text_as_audio(text_to_save)
