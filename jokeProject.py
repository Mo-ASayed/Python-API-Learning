import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("BEST DAD JOKES")
header = colored(header, color="blue")
print(header)

inputTerm = input("What would you like to search?")
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={"Accept" : "application/json"},
    params={"term":inputTerm}
    ).json()

total_jokes = response["total_jokes"]
results = response["results"]
if total_jokes > 1:
    print(f"There are multiple jokes, I found {total_jokes} about {inputTerm}")
    print(choice(results)["joke"])
elif total_jokes == 1:
    print(f"There is only one joke about {inputTerm}")
    print(results[0]['joke'])
else:
    print("Sorry,There are no jokes... except you :)")