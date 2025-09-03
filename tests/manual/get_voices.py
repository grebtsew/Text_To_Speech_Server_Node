import pyttsx3

converter = pyttsx3.init()

# Hämta alla röster
voices = converter.getProperty("voices")

# Skriv ut information om varje röst
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print(f"  Age: {voice.age}")
    print()
