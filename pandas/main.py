import pandas as pd
# reading the data with pandas
# data = pd.read_csv('weather_data.csv')

# print(data['temp'])

# converting our dataframe in dictonary
# print(data.to_dict())

# Getting hold of average temprature
# temp_list = data['temp'].to_list()
# print(f"The average temperature is {round(sum(temp_list)/len(temp_list), 2)}")

# Getting data in rows
# print(data[data.temp == max(data.temp)])

# Working with the squirrel data
squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv')
fur_color = squirrel_data['Primary Fur Color'].to_list()
gray_squirrels = black_squirrels = cinamon_squirrels = 0
for color in fur_color:
    if color == 'Gray':
        gray_squirrels += 1
    elif color == 'Black':
        black_squirrels += 1
    else:
        cinamon_squirrels += 1
data_dict = {
    'Fur-Color': ['Gray', 'Black', 'Cinamon'],
    'Count': [gray_squirrels, black_squirrels, cinamon_squirrels]
}
pd.DataFrame(data_dict).to_csv('Analysed.csv', index=False)
