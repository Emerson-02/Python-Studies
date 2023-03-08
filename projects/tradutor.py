from translate import Translator

texto = input("Texto: ")

translator = Translator(from_lang = 'Portuguese', to_lang = 'english')

result = translator.translate('{}' .format(texto))
print(result)