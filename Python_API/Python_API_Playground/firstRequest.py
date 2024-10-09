import requests

url = "http://www.google.com"
response = requests.get(url)

print(f"Your request to {url} came back as {response.status_code}") #This is how we get the status code