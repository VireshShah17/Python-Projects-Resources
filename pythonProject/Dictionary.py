import json
from difflib import get_close_matches
data=json.load(open("G:\data.json"))
ex='0'
while ex!="exit":
    word = input("Enter the word whose meaning you want to find")
    word = word.lower()
    def translate(word):
        if word in data:
            return data[word]
        elif len(get_close_matches(word,data.keys()))>0:
            print("Did you mean %s"%get_close_matches(word,data.keys())[0])
            decide=input("Press y for yes or n for no")
            if decide=="y" or decide=="Y":
                return data[get_close_matches(word,data.keys())[0]]
            elif decide=="n" or decide=="N":
                print("Word not found in our dictionary database")
            else:
                return ("Please input correct input")
        else:
            print("Word not found in our dictionary database")
    output = translate(word)
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
    ex=input("Press enter to continue to search meaning of words or press exit to exit the dictionary")
    ex=ex.lower()