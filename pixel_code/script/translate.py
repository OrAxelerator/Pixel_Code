


def translate(text, langage) -> str:
    """
    :param text: array: [0] = english, [1] = french
    :return: array[0/1] according to the langague 
    """
    if type(text) == dict:
        return text[langage]
    if type(text) == list:
        lang : int = 0 if langage == "en" else 1
        return text[lang]


