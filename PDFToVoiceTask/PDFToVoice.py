import PyPDF2
import pyttsx3

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page =  reader.pages[page_num]
            text += page.extract_text()
    return text

def read_text_out_loud(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)  # You can adjust the speaking rate
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    text = extract_text_from_pdf(pdf_path)
    if text.strip() == "":
        print("No text found in the PDF.")
    else:
         read_text_out_loud(text)
        