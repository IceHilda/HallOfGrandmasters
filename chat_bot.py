# Packages we need
import json
import requests

# Function to accept input and look up using the API
    # 1. Get input from the user
    # 2. Generate a URL using that input
    # 3. Fetch data from that URL (will be in JSON format)
    # 4. Convert the JSON to a python object
    # 5. Print some elements of that object to the user
#poe_url = "http://api.pathofexile.com/ladders/Standard?type=labyrinth&difficulty=Normal"
swapi_url = "https://swapi.co/api/starships/"

"""
{
    "films": "https://swapi.co/api/films/",
    "people": "https://swapi.co/api/people/",Y-wing
    "planets": "https://swapi.co/api/planets/",
    "species": "https://swapi.co/api/species/",
    "starships": "https://swapi.co/api/starships/",
    "vehicles": "https://swapi.co/api/vehicles/"
}
"""
response = requests.get(swapi_url)
#print(response)
data = response.json()
results = data["results"]
# TO-DO: Get other pages as long as there's a new url listed under data['next'] and add it to the results


while True:
    ship_name = input("what ship are you searching for?(q) to quit ")
    if ship_name == "q":
        break
    if ship_name == "l":
        print([ship["name"] for ship in results])
    # List comprehension style
    my_ship = [ship for ship in results if ship['name'] == ship_name]

    if len(my_ship) == 0:
        print("You have no ship, come back with more credits scum")
    else:
        my_ship = my_ship[0]  # solves the problem of having a list of 1 item
        print("Your ship was produced by the slaves of " + my_ship["manufacturer"])







# Functionally equivalent!
#my_ship = []
#for ship in results:
#    if ship['name'] == 'X-wing':
#        my_ship.append(ship)


#print(my_ship)
#print(results)


"""
{data} (dictionary)
    'count' (int)
    'next' (str)
    'previous' (str)
    'results' (list)
        {} individual dictionaries for each result
        {}
        {}
        {}
"""

"""

A bit of JSON
{
    "total": 17,
    "title": "Labyrinth - Standard (Normal)",
    "startTime": 1578614400,
    "entries": [
        {
            "online": false,
            "rank": 3,
            "time": 460,
            "character": {
                "name": "BrotherHanfmeisda",
                "level": null,
                "class": "Shadow",
                "experience": null
            },
            "account": {
                "name": "Schmerlin",
                "realm": "pc",
                "guild": {
                    "id": "526085",
                    "name": "ArkAngels",
                    "tag": ""
                },
                "challenges": {
                    "total": 0
                }
            }
        }
    ]
}
"""