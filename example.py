from python_translator import Translator

translator = Translator()

source = input('Source Language:\n> ').lower()
output = input('Output Language:\n> ').lower()

text = input('Text to Translate:\n> ').lower()

result = translator.translate(text, output, source)

print('\n' + result.new_text)