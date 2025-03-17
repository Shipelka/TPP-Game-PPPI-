import langdetect

class LanguageDetector:
    """
    Класс для определения языка текста с использованием библиотеки langdetect.

    Методы:
        detect(text): Определяет язык текста.
        set_language(lang_code): Устанавливает язык вручную, выводя сообщение о выбранном языке.
    """

    def __init__(self):
        """
        Инициализация объекта LanguageDetector.
        """
        pass

    def detect(self, text):
        """
        Определяет язык текста с помощью библиотеки langdetect.

        Аргументы:
            text (str): Текст, для которого нужно определить язык.

        Возвращает:
            str: Код языка (например, "en" для английского), или "unknown", если язык не удалось определить.
        """
        try:
            return langdetect.detect(text)
        except langdetect.lang_detect_exception.LangDetectException:
            return "unknown"

    def set_language(self, lang_code):
        """
        Устанавливает язык вручную и выводит сообщение о выбранном языке.

        Аргументы:
            lang_code (str): Код языка, который нужно установить (например, "en" для английского).

        Пример:
            set_language("en")
        """
        print(f"Language manually set to: {lang_code}")
