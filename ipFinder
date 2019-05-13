import requests
from colorama import init, Fore
init()

response = requests.get('https://httpbin.org/ip')

print(Fore.BLUE + 'Your IP is {0}'.format(response.json()['origin']))

input("\n Press ENTER to continue")