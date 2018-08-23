import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s, Enter Y if yes and N if No " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Restart the program and enter the right word"
        else:
            return "your entry is invalid, please try again"
    else:
        return "This word is not in the dictionary, try again."

word = input("Enter word: ")
word = word.casefold()

defination = translate(word)

if type(defination) == list:
    for i in defination:
        print(i)
else:
    print(defination)
