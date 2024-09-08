from translation_modules import gtrans_module as gt

print(gt.TransLate("Hello", "en", "uk"))
print(gt.LangDetect("Hello"))
print(gt.CodeLang("English"))
gt.LanguageList("screen", "Hello")
