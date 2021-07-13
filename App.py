import json
import difflib


'''This is a activity from the Udemy course. The application recieves a word as input then returns the dictionary definition from the json data file'''


def definition(word):

    word = word.lower()
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(difflib.get_close_matches(word, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y if yes or N if No " %
                   difflib.get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[difflib.get_close_matches(word, data.keys()[0])]
        elif yn == "N":
            return "Word does not exist"
    else:
        return "Word does not exist"


data = json.load(open("data.json"))
user_input = input("Enter word: ")


output = definition(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
