# NATO alphabet project
import pandas as pd

# Reading the csv file
file = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(file)
# Creating a dictionary of our csv file data
lst1 = {row.letter: row.code for (index, row) in df.iterrows()}
name = input("Enter your name:").upper()
lst2 = [n for n in name]
# Looping through our dictionary and the letters of the name inputted
result = [lst1[key] for i in range(len(lst2)) for key in lst1.keys() if lst2[i] == key]
print(result)
