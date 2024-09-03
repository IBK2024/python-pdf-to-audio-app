import playsound
from gtts import gTTS
from PyPDF2 import PdfReader

# !Main code
PDF_READER = PdfReader("./assets/PDFs/book.pdf")


def main() -> None:
    """Main code"""
    clean_text: str = ""
    for page_num, _ in enumerate(PDF_READER.pages):
        text: str = PDF_READER.pages[page_num].extract_text()
        clean_text = text.strip().replace("\n", " ")
    speak(clean_text)


# !Converts text to speech
def speak(text_to_convert: str) -> None:
    """Converts text to speech"""
    gtts = gTTS(text_to_convert, lang="en")
    filename = "./assets/audios/book.mp3"
    gtts.save(filename)
    playsound.playsound(filename)
