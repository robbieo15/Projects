import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from config import token    
import requests

token = token
topheadlinesdata = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={token}").json()

def headlines():

    headline_names = []
    key = 0
    keys_for_headline = []
    headline_urls = []

    for items in range(0,10):
        headline_names.append(topheadlinesdata['articles'][key]['title'])
        headline_urls.append(topheadlinesdata['articles'][key]['url'])
        keys_for_headline.append(key)
        key += 1
    
    headline_dict = list(zip(keys_for_headline,headline_names,headline_urls))
    
    for items in headline_dict:
        print(items[0],items[1])
    
    read_article = input("Type yes if you want to read an article or anything else to go back to the main menu: ").lower()

    while True:
        
        if read_article == 'yes':
            headline_inputted = int(input("Select the article's number that you want to read: "))
            print(headline_dict[headline_inputted][2])
            read_article = input("Type yes if you want to read an article or anything else to go back to the main menu: ").lower()
        else:
            return False

allsides = open('allsides.json')

data_allsides = json.load(allsides)

adfontes_df = pd.read_table('adfontes2019.csv', delimiter=",")

#community thoughts on ranking
def news_bias():
    for items in data_allsides:
        if int(items['agree']) >= int(items['disagree']):
            print(f"{items['name']} : {items['bias']} : Community Agrees with Analysis")
        else:
            print(f"{items['name']} : {items['bias']} : Community Disagrees with Analysis")

    search_1 = input("Enter the First News Channel(like ABC, Fox, AP, etc) you would like to compare: ")
    search_2 = input("Enter the First News Channel(like ABC, Fox, AP, etc) you would like to compare: ")

    print(adfontes_df[adfontes_df['News'].str.contains(search_1,flags=re.IGNORECASE,regex=True)])
    print(adfontes_df[adfontes_df['News'].str.contains(search_2,flags=re.IGNORECASE,regex=True)])

    search_highlight = adfontes_df.loc[adfontes_df['News'] == search_1]

    print(adfontes_df['News'][1])
    search_highlight.plot(x = 'Hori', y = 'Vert', kind = 'scatter', xlabel = 'Political Bias', ylabel = 'Reliability')
    plt.show()

'''
Dataframes use this format

dataframe[Header Name][Row Number]
'''
'''

#graphing the datapoints

# News API Time

1. Compare News Channel Bias
2. The Latest News
3. Most Viewed Topics by Bias
'''

def main():
    
    menu_options = {
        '1': 'Compare the News Channel Bias',
        '2': 'Headline News of the Day',
        '3': 'Most Viewed Topics and Bias',
        '4': 'Exit'
    }
    print(f"Welcome to the News Bias Analyzer!")

    while True:
        for label,option in menu_options.items():
            print(f'{label} {option}')

        inputted_option = input("\nEnter the number of the action you would like to perform\n ")
        inputted_option = menu_options.get(inputted_option)

        if inputted_option == 'Compare the News Channel Bias':
            news_bias()

        elif inputted_option == 'Headline News of the Day':
            headlines()

        elif inputted_option == 'Most Viewed Topics and Bias':
            pass

        elif inputted_option == 'Exit':
            print("Thanks for using our News Bias Analyzer!")
            break

        else:
            print("Try again, this doesn't seem to be an option...")


main()