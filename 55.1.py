class Text:
    def __init__(self, text):
        self.__text = text

    def getCharacterCount(self):
        return len(self.__text)

    def getLetterCount(self):
        letter_count = 0
        for char in self.__text:
            if char.isalpha():
                letter_count += 1
        return letter_count

    def getSpaceCount(self):
        space_count = 0
        for char in self.__text:
            if char.isspace():
                space_count += 1
        return space_count

    def getCharacterCountWithoutSpaces(self):
        character_count = 0
        for char in self.__text:
            if not char.isspace():
                character_count += 1
        return character_count

    def getWordArray(self):
        word_array = self.__text.split()
        return word_array

    def getSentenceArray(self):
        sentence_array = self.__text.split('.')
        return sentence_array



text = "Hello, world! Abugi agagi agagashenki."
text_obj = Text(text)

print("Количество символов в тексте:", text_obj.getCharacterCount())
print("Количество букв в тексте:", text_obj.getLetterCount())
print("Количество пробелов в тексте:", text_obj.getSpaceCount())
print("Количество символов без пробелов в тексте:", text_obj.getCharacterCountWithoutSpaces())
print("Массив слов в тексте:", text_obj.getWordArray())
print("Массив предложений в тексте:", text_obj.getSentenceArray())