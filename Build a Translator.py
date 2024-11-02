def _translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation += 'X'
            else:
                translation += 'x'
        else:
            translation += letter
    return translation

print(_translate(input("Enter Your Phrase: ")))