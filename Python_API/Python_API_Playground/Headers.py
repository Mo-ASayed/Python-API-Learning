import requests

# url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "application/json"})

# data = response.json()
# # print(type(response.text))

# print(data["joke"])
# print(f"status: {data['status']}")

#vvv Query Strings vvv


searchUrl = "https://icanhazdadjoke.com/search"

searchResponse = requests.get(
    searchUrl, 
    headers={"Accept": "application/json"},
    params= {"term": "dog", "limit": 1}
)
    
searchData = searchResponse.json()

print(searchData["results"])
