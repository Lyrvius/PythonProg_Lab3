from googletrans import Translator
from googletrans import LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    translator = Translator()
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {detection.confidence}"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
        return "Error"

def LanguageList(out: str = "screen", text: str = "") -> str:
    languages = {'uk': 'Ukrainian', 'en': 'English', 'fr': 'French', 'de': 'german', 'it': 'italian'}
    table = f"{'N':<3}{'Language':<20}{'ISO-639':<10}{'Text':<20}\n"
    table += "-" * 60 + "\n"
    for i, (code, lang) in enumerate(languages.items(), 1):
        translated_text = TransLate(text, 'auto', code) if text else ""
        table += f"{i:<3}{lang:<20}{code:<10}{translated_text:<20}\n"
    if out == "file":
        with open("languages.txt", "w") as file:
            file.write(table)
        return "Ok"
    else:
        print(table)
        return "Ok"


