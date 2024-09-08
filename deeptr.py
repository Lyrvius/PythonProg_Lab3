from translation_modules import deeptr_module as dt

print(dt.TransLate("Hello", "en", "uk"))
print(dt.LangDetect("Hello, how are you today? Nice, I feel very good, what about you?"))
print(dt.CodeLang("English"))
dt.LanguageList("screen", "Hello")
