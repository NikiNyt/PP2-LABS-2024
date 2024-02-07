from pprint import pprint

def word_frequency(text):
    result = {}
    for w in text.lower().split():
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    return result

text_in = "aaa bbb ccc aaa bbb ccc aaa aa aa aa bb"

pprint(word_frequency(text_in))
