import requests
from random import choice
import pyfiglet
from termcolor import colored

# Generate an ASCII art header for the project
header = pyfiglet.figlet_format("BEST DAD JOKES")
header = colored(header, color="blue")
print(header)

# Prompt the user for a joke topic
inputTerm = input("What do you want a joke about?: ")

# API endpoint for fetching dad jokes
url = "https://icanhazdadjoke.com/search"

# Send a GET request to the API with the user's input term and accept a JSON response
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": inputTerm}
).json()

# Store the number of jokes found for the input term in a variable
total_jokes = response["total_jokes"]

# Store the list of jokes in a variable
results = response["results"]

# Check the number of jokes found and print a message accordingly
if total_jokes > 1:
    print(f"There are multiple jokes, I found {total_jokes} jokes about {inputTerm}.")
    print(choice(results)["joke"])  # Print a random joke from the list
elif total_jokes == 1:
    print(f"There is only one joke about {inputTerm}.")
    print(results[0]["joke"])  # Print the single joke found
else:
    print("Sorry, there are no jokes... except you :)")