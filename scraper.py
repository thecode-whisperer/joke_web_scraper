from bs4 import BeautifulSoup
import requests
import random

def new_game():
    search_term = input('What would you like to hear a joke about? ')
    print('\n')
    base_url = 'https://icanhazdadjoke.com/search?term='
    url = base_url + search_term
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    jokes = []

    for joke in soup.find_all('pre', {'style': 'background-color:inherit; white-space: pre-wrap'}):
        jokes.append(joke.text)

    if jokes:
        print(random.choice(jokes))
        print('\n')
    else:
        print(f'I could not find any jokes about {search_term}! :(')
        print('\n')
    
    replay()

def replay():
    play_again = str(input('Would you like to hear another joke? (y/n) '))
    print('\n')
    if play_again in ['y', 'Y']:
        new_game()
    else:
        print('Thank you for playing! Have a good day :)')
        print('\n')

new_game()
