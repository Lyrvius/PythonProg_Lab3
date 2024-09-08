from translation_modules.gtrans_module import TransLate
import os

def read_config(config_path):
    with open(config_path, 'r') as config_file:
        lines = config_file.read().splitlines()
        config = {
            "text_file": lines[0],  # The name of the text file
            "dest_lang": lines[1],  # Language for translation
            "output": lines[2],  # Where to output the result (file or screen)
            "max_chars": int(lines[3]),  # Maximum number of characters
            "max_words": int(lines[4]),  # Maximum number of words
            "max_sentences": int(lines[5])  # Maximum number of sentences
        }
        return config


def read_text_file(file_path):
    if not os.path.exists(file_path):
        return None, "File not found."

    with open(file_path, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
    return text, None


# Function for counting characters, words and sentences
def count_text_stats(text):
    chars = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    return chars, words, sentences


# Function for trimming the translation of the text
def cut_text(text, config):
    chars, words, sentences = count_text_stats(text)

    if chars > config['max_chars']:
        text = text[:config['max_chars']]
    if words > config['max_words']:
        text = ' '.join(text.split()[:config['max_words']])

    sentences_in_text = text.split('.')
    if len(sentences_in_text) > config['max_sentences']:
        text = '.'.join(sentences_in_text[:config['max_sentences']]) + '.'

    return text

def translate_text(config_file):
    config_path = config_file
    config = read_config(config_path)

    # Reading file
    text, error = read_text_file(config["text_file"])
    if error:
        print(error)
        return

    # Outputting basic text statistics
    chars, words, sentences = count_text_stats(text)
    print(f"File name: {config['text_file']}")
    print(f"Symbols count: {chars}")
    print(f"Words count: {words}")
    print(f"Sentences count: {sentences}")

    # Cutting text by parameters
    text_to_translate = cut_text(text, config)

    translated_text = TransLate(text_to_translate, 'auto', config['dest_lang'])

    # Outputting result
    if config['output'] == 'screen':
        print(f"\nTranslation to {config['dest_lang']}:\n{translated_text}")
    else:
        output_file = f"{config['text_file'].split('.')[0]}_{config['dest_lang']}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print(f"Translation saved to: {output_file}")


if __name__ == "__main__":
    translate_text("config_file.txt")