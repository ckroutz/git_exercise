import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('bmgf.pdf', 'rb'))
"""with some changes"""
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 145)

voices = speaker.getProperty('voices')
print(voices)
speaker.setProperty('voice', voices[1].id)

volume = speaker.getProperty('volume')
# print(volume)
speaker.setProperty('volume', 1.0)

# speaker.say("Hello there")
# speaker.save_to_file("Hello WOrld!", 'test.mp3')

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    print(text)
    speaker.say(text)
    speaker.save_to_file(text, 'systemantics.mp3')
    speaker.runAndWait()
speaker.stop()


# speaker.runAndWait()
