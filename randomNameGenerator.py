#This program generates random funny names
#Names starting with vowels will be in RED and others will be in GREEN

import random_name
from colorama import init, Fore

init()

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
    randomName = random_name.generate_name()
    if randomName[0] in vowels:
        print(Fore.RED + '\n', randomName)
    else:
        print(Fore.GREEN + '\n', randomName)


input("\n Press ENTER to continue")
