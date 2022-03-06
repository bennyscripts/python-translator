import requests
import bs4

from . import lang_codes

class Translator:
    def __init__(self) -> None:
        self.BASE_URL = "https://translate.google.com/m?sl={source_lang}&tl={target_lang}&hl={source_lang}&q={text}"

    def _generate_url(self, source_language: str, target_language: str, text: str) -> str:
        """
        Generate a URL for the translation.

        Arguments:
            source_language (str) : Source language.
            target_language (str) : Target language.
            text (str) : Text to be translated.

        Returns:
            str : URL for the translation.
        """
        
        return self.BASE_URL.format(source_lang=source_language, target_lang=target_language, text=text)

    def translate_text(self, text: str, target_language, source_language: str = "en") -> str:
        """
        Translate text from source language to target language.
        
        Arguments:
            text (str) : Text to be translated.
            target_language (str) : Target language.
            source_language (str) : Source language.

        Returns:
            str : Translated text.
            None : If the translation failed.
        """

        if len(source_language) != 2: source_language = lang_codes.convert_to_code(source_language.lower())
        if len(target_language) != 2: target_language = lang_codes.convert_to_code(target_language.lower())

        url = self._generate_url(source_language, target_language, text)
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        
        result_container = soup.find("div", {"class": "result-container"})
        
        if result_container:
            translated_text = result_container.text
            return translated_text

        return None

    translate = translate_text