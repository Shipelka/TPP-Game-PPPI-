import langdetect

class LanguageDetector:
    def __init__(self):
        pass

    def detect(self, text):
        try:
            return langdetect.detect(text)
        except langdetect.lang_detect_exception.LangDetectException:
            return "unknown"

    def set_language(self, lang_code):
        print(f"Language manually set to: {lang_code}")
