from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='en')
print(translator.translate("Pfälzerstr. 10 90443 Nürnberg"))