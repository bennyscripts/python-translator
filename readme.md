# python-translator
A python library to translate text from one language to another.  

### Why use this?
> It uses the Google API, showing the best results. And unlike other repos, does not require an API key to operate.

### Install
> ```bash
> $ pip install python-translator
> ```

> ### Example
> ```python
> from python_translator import Translator
> 
> translator = Translator()
> result = translator.translate("Hello world!", "spanish", "english")
> 
> print(result)
> ```

## Responses
Returns a `Response` object, containing:
- source_language
- target_language
- original_text
- new_text: str