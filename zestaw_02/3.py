import re

def describe(string):
    def hist(l):
        h = {}
        for it in l:
            if it in h:
                h[it] += 1
            else:
                h[it] = 1
        return h

    letters = re.findall(r'[a-zA-Z]', string)
    digits = re.findall(r'\d', string)
    words = re.findall(r'[a-zA-Z]+', string)

    return {
        "words": len(words),
        "letters": len(letters),
        "letters_hist": hist(letters),
        "digits": len(digits),
        "digits_hist": hist(digits),
    }

sentence = "The quick brown fox jumps over 2 lazy dogs!"
print(sentence)

description = describe(sentence)
print(description)
