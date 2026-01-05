

def translate(self, text) -> str:
    """
    :param text: array: [0] = english, [1] = french
    :return: array[0/1] according to the langague 
    """
    lang : int = 0 if self.parametre.language == "en" else 1
    return text[lang]

