#Allows us to read the json file
import json
#Allows us to fetch files from the internet
import requests
#Allows us to use pretty prints
import pprint

from colorama import init, Fore, Back, Style
#Sends a GET request to the website for file information
r = requests.get(pokedex+"pokemon/"+i)
#binds the variable "content" to load the json file content
data = json.loads(r.content)

class pokemon():
    #A function that will print out the pokemon's id & name
    def pokemon():
        #prints the pokemon id in green color
        print("Pokemon id: "+Fore.GREEN+str(data["id"])+Fore.RESET)
        #prints the pokemon name in green color
        print("Pokemon name: "+Fore.GREEN+data["name"]+Fore.RESET)
