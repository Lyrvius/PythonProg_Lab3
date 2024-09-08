from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str) -> str:
    try:
        lang = detect(text)
        return lang
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    if lang in languages:
        return languages[lang]
    elif lang in languages.values():
        return list(languages.keys())[list(languages.values()).index(lang)]
    else:
        return "Error"

def LanguageList(out: str = "screen", text: str = "") -> str:
    shartLanguages = {'uk': 'Ukrainian', 'en': 'English', 'fr': 'French', 'de': 'german', 'it': 'italian'}
    table = f"{'N':<3}{'Language':<20}{'ISO-639':<10}{'Text':<20}\n"
    table += "-" * 60 + "\n"
    for i, (code, lang) in enumerate(shartLanguages.items(), 1):
        translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
        table += f"{i:<3}{lang:<20}{code:<10}{translated_text:<20}\n"

    if out == "file":
        with open("languages.txt", "w") as file:
            file.write(table)
        return "Ok"
    else:
        print(table)
        return "Ok"


languages = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic',
    'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian',
    'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
    'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'hr': 'Croatian', 'cs': 'Czech',
    'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto',
    'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French',
    'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek',
    'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'he': 'Hebrew',
    'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic',
    'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian',
    'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh',
    'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz',
    'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish',
    'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam',
    'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'ps': 'Pashto',
    'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi',
    'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic',
    'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala',
    'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish',
    'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik',
    'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa',
    'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'
}