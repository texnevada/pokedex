#!/usr/bin/python3
"""
Program name: Pokedex
Author: !@¤%&/()=?
Created: 12.02.19 - Europe
"""

"""
=====================
Import libraries here
=====================
"""
#Allows us to read the json file
import json
#Allows us to fetch files from the internet
import requests
#Allows us to use arguments
import argparse
#Allows us to use colors in terminal. init is required for colorama to work on windows properly
from colorama import init, Fore, Style
#Imports the system. Used for the image function
import sys
"""
==============
ArgumentParser
==============
"""
#Variable we can call when making arguments. -By default. --help is on
parser = argparse.ArgumentParser()
#Arguments that the user can call
parser.add_argument("-t", "--type", help="Will display the pokemon's type.", action="store_true")
parser.add_argument("-m", "--measurements", help="Will display the pokemon's measurements.", action="store_true")
parser.add_argument("-s", "--stats", help="Will display the pokemon's stats.", action="store_true")
parser.add_argument("-a", "--abilities", help="Will display the pokemon's possible abilities", action="store_true")
parser.add_argument("-v", "--moves", help="Will display what moves the pokemon can learn", action="store_true")
parser.add_argument("-f", "--forms", help="Will display the pokemon's possible forms. (Most pokemon only have 1 form)", action="store_true")
parser.add_argument("-i", "--items", help="Will display the possible itmes held by the pokemon", action="store_true")
parser.add_argument("-g", "--gameversion", help="Will display what game the pokemon appears in", action="store_true")
parser.add_argument("-p", "--picture", help="Will display a image of the pokemon", action="store_true")
parser.add_argument("--noarg", help="Running this argument will cause no arguments to run\n-------------------------------------------------------\nWhen no arguments is given. The code will cause them all to run!", action="store_false")
#args variable is made so we can call it later in if a argument is given
args = parser.parse_args()

"""
================
Code begins here
================
"""

#prints information to terminal
print("Please insert name or Pokemon ID below.")
#variable named "i" that references to input() which request user input.
i = input("> ")
#binds the http url to the variable "pokedex"
pokedex = "https://pokeapi.co/api/v2/"
#this variable is made to be added ontop of pokedex variable
pokemons = "pokemon/"

#Sends a GET request to the website for file information
r = requests.get(pokedex+pokemons+i)
#binds the variable "content" to load the json file content
data = json.loads(r.content)

"""
##This meant for future content like evolutions.
##While the classes are in use. The ID position can be lost if later requested in code.
#A list to store the pokemon id
id = []
#Will store the pokemon in the id list
id.append(data["id"])
"""
#init is required by colorama to work properly in Windows.
init()

"""
============
Classes here
============
"""

class pokemon():
    #A function that will print out the pokemon's id & name
    def pokemon():
        #prints the pokemon id in green color
        print("Pokemon id: "+Fore.GREEN+str(data["id"])+Fore.RESET)
        #prints the pokemon name in green color
        print("Pokemon name: "+Fore.GREEN+data["name"]+Fore.RESET)
#New class is made which can be called later with its functions
class type():
    #new function called type()
    def type():
        #prints to terminal
        print("\nPokemon's types")
        #list to store the pokemon's type
        PokemonType = []
        #Makes the value of "n" to "-1"
        n = -1
        #starts a for loop in the API list under "types" that will look for the key "name"
        for data["name"] in data["types"]:
            #Makes the value of "n" to "0" by adding 1 to the value
            n = n+1
            #Will store the pokemon type under "name" thats under "type" thats under the value of "n"
            #that us under "types" to be stored in the "PokemonType" list
            PokemonType.append(data["types"][n]["type"]["name"])
        #Will reverse the order of the list because the API list is in the wrong order
        PokemonType.reverse()
        #Makes the value of "n" to "1"
        n = 1
        #Starts a for loop for the "PokemonType" list
        for i in PokemonType:
            #Makes a if statement to see if the pokemon's type is equal to the type in the following list
            #will print different colors of the different types because of if statements
            if i == "normal":
                print("Type:", n, Fore.GREEN, i+Fore.RESET)
            if i == "grass":
                print("Type:", n, Fore.GREEN, i+Fore.RESET)
            if i == "fire":
                print("Type:", n,Fore.RED+ i+Fore.RESET)
            if i == "water":
                print("Type:", n,Fore.CYAN+ i+Fore.RESET)
            if i == "fighting":
                print("Type:", n,Fore.RED+ i+Fore.RESET)
            if i == "flying":
                print("Type:", n,Fore.CYAN+ i+Fore.RESET)
            if i == "poison":
                print("Type:", n,Fore.MAGENTA+ i+Fore.RESET)
            if i == "ground":
                print("Type:", n,Fore.YELLOW+ i+Fore.RESET)
            if i == "rock":
                print("Type:", n,Fore.YELLOW+ i+Fore.RESET)
            if i == "bug":
                print("Type:", n,Fore.YELLOW+ i+Fore.RESET)
            if i == "ghost":
                print("Type:", n,Fore.MAGENTA+ i+Fore.RESET)
            if i == "electric":
                print("Type:", n,Fore.YELLOW+ i+Fore.RESET)
            if i == "psychic":
                print("Type:", n,Fore.YELLOW+ i+Fore.RESET)
            if i == "ice":
                print("Type:", n,Fore.CYAN+ i+Fore.RESET)
            if i == "dragon":
                print("Type:", n,Fore.MAGENTA+ i+Fore.RESET)
            if i == "dark":
                print("Type:", n,Fore.BLACK+Back.WHITE+ i+Fore.RESET)
            if i == "steel":
                print("Type:", n,Fore.WHITE+ i+Fore.RESET)
            if i == "fairy":
                print("Type:", n,Fore.WHITE+ i+Fore.RESET)
            #Makes the value of "n" to "2" by adding 1 to the value
            n = n+1
#New class is made which can be called later with its functions
class measurements():
    #new function called measurements()
    def measurements():
        #prints information to terminal
        print("\nPokemon's measurements")
        #prints information about the pokemon's height with colorama & in cm
        print("Height: "+Fore.GREEN+str(data["height"])+"cm"+Fore.RESET)
        #prints information about the pokemon's weight with colorama & in hg
        print("Weight: "+Fore.GREEN+str(data["weight"])+"hg"+Fore.RESET)
#New class is made which can be called later with its functions
class get_stats():
    #new function called get_stats()
    def get_stats():
        #prints information to terminal
        print("\nPokemon's stats")
        #A list called PokemonStats
        PokemonStats = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "stats" & loops until it cannot find any more
        for data['name'] in data['stats']:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the stats name into PokemonStats list
            PokemonStats.append(data['stats'][n]['stat']['name'] +(": ") +Fore.GREEN +str(data['stats'][n]['base_stat'])+Fore.RESET)
        #Calls for the reverse function to reverse the PokemonStats list
        PokemonStats.reverse()
        #for the number of items in PokemonStats list. Print the list that number of times
        for i in PokemonStats:
            #print the information to terminal
            print(i)
#New class is made which can be called later with its functions
class abilities():
    def abilities():
        #prints information to terminal
        print("\nPokemon's abilities")
        #A list called PokemonAbilities
        PokemonAbilities = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "abilities" & loops until it cannot find any more
        for data["name"] in data["abilities"]:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the Game name into PokemonAbilities list
            PokemonAbilities.append(data["abilities"][n]["ability"]["name"])
        #Calls for the reverse function to reverse the PokemonAbilities list
        PokemonAbilities.reverse()
        #a variable where "n" is equal to "1"
        n = 1
        #for the number of items in PokemonAbilities list. Print the list that number of times
        for i in PokemonAbilities:
            #print the information to terminal with the ability text, the "n" number & colorama color for the information in PokemonAbilities list
            print("Ability:", n, Fore.GREEN, i+Fore.RESET)
            #a variable where "n" has its number updated to "n+1"
            n = n+1
#New class is made which can be called later with its functions
class image():
    def image():
        #
        #nb! Not tested on linux enviourment.
        #Further testing required. Not enough time to test before deadline.
        #
        #Will try to run the code
        try:
            #Code borrowed for effect & speed purposes. Not enough time to rebuild from the ground up.
            #https://www.daniweb.com/programming/software-development/code/440946/display-an-image-from-a-url-tkinter-python
            import io
            import base64
            try:
                # Python2
                import Tkinter as tk
                from urllib2 import urlopen
            except ImportError:
                # Python3
                import tkinter as tk
                from urllib.request import urlopen
            root = tk.Tk()
            root.title("Pokemon")
            # a little more than width and height of image
            w = 520
            h = 320
            x = 80
            y = 100
            # use width x height + x_offset + y_offset (no spaces!)
            root.geometry("%dx%d+%d+%d" % (w, h, x, y))
            #image is called from API sprites.
            image_url = data["sprites"]["front_default"]
            image_byt = urlopen(image_url).read()
            image_b64 = base64.encodestring(image_byt)
            photo = tk.PhotoImage(data=image_b64)
            # create a white canvas
            cv = tk.Canvas(bg='white')
            cv.pack(side='top', fill='both', expand='yes')
            # put the image on the canvas with
            # create_image(xpos, ypos, image, anchor)
            cv.create_image(10, 10, image=photo, anchor='nw')
            root.mainloop()
        #If import of modules results in errors.
        except ImportError:
            #Prints out a error message to terminal
            print("Your system does not support the image function!")
#New class is made which can be called later with its functions
class gameversion():
    #new function called gameversion()
    def gameversion():
        #prints information to terminal
        print("\nThe following are the games the pokemon has appeared in.")
        #A list called PokemonGame
        PokemonGame = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "game_indices" & loops until it cannot find any more
        for data["name"] in data["game_indices"]:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the Game name into PokemonGame list
            PokemonGame.append(data["game_indices"][n]["version"]["name"])
        #Calls for the reverse function to reverse the PokemonGame list
        PokemonGame.reverse()
        #for the number of items in PokemonGame list. Print the list that number of times
        for i in PokemonGame:
            #print the information to terminal
            print(i)
#New class is made which can be called later with its functions
class moves():
    #new function called moves()
    def moves():
        #prints information to terminal
        print("\nMoves that the pokemon can learn")
        #A list called PokemonMoves
        PokemonMoves = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "moves" & loops until it cannot find any more
        for data["name"] in data["moves"]:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the moves name into PokemonMoves list
            PokemonMoves.append(data["moves"][n]["move"]["name"])
        #Calls for the reverse function to reverse the PokemonMoves list
        PokemonMoves.reverse()
        #for the number of items in PokemonMoves list. Print the list that number of times
        for i in PokemonMoves:
            #print the information to terminal
            print(i)
#New class is made which can be called later with its functions
class forms():
    #new function called forms()
    def forms():
        #prints information to terminal
        print("\nThese are the forms that the pokemon can appear as\nMost pokemon only have 1 form")
        #A list called PokemonForms
        PokemonForms = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "forms" & loops until it cannot find any more
        for data["name"] in data["forms"]:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the forms name into PokemonForms list
            PokemonForms.append(data["forms"][n]["name"])
        #Calls for the reverse function to reverse the PokemonForms list
        PokemonForms.reverse()
        #for the number of items in PokemonForms list. Print the list that number of times
        for i in PokemonForms:
            #print the information to terminal
            print(i)
#New class is made which can be called later with its functions
class held_items():
    #New function called held_items():
    def held_items():
        #prints information to the terminal
        print("\nThese are the item that comes with the pokemon after you have captured them\nSome pokemon also can collect these items for you")
        #A list called PokemonItems
        PokemonItem = []
        #a variable where "n" is equal to "-1"
        n = -1
        #Starts a for loop in the API that looks for "name" under "held items" & loops until it cannot find any more
        for data["name"] in data["held_items"]:
            #a variable where "n" has its number updated to "n+1"
            n = n+1
            #Adds the held item's name into PokemonItem list
            PokemonItem.append(data["held_items"][n]["item"]["name"])
        #Calls for the reverse function to reverse the PokemonItem list
        PokemonItem.reverse()
        #for the number of items in PokemonItem list. Print the list that number of times
        for i in PokemonItem:
            #print the information to terminal
            print(i)

#Will run all classes if function is called
def run_all():
    #calls for function type in class type
    type.type()
    #calls for function measurements in class measurements
    measurements.measurements()
    #calls for function get_stats in class get_stats
    get_stats.get_stats()
    #calls for function abilities in class abilities
    abilities.abilities()
    #calls for function moves in class moves
    moves.moves()
    #calls for function forms in class forms
    forms.forms()
    #calls for function held_items in class held_items
    held_items.held_items()
    #calls for function gameversion in class gameversion
    gameversion.gameversion()
    #calls for function image in class image
    #Run this last or the code will pause while image is showing
    image.image()

#New function to call for a argument check
def argument_check():
    #if argument type is called then the if statement will run
    if args.type:
        #calls for function type in class type
        type.type()
    #if argument stats is called then the if statement will run
    if args.stats:
        #calls for function get_stats in class get_stats
        get_stats.get_stats()
    #if argument measurements is called then the if statement will run
    if args.measurements:
        #calls for function measurements in class measurements
        measurements.measurements()
    #if argument abilities is called then the if statement will run
    if args.abilities:
        #calls for function abilities in class abilities
        abilities.abilities()
    #if argument moves is called then the if statement will run
    if args.moves:
        #calls for function moves in class moves
        moves.moves()
    #if argument forms is called then the if statement will run
    if args.forms:
        #calls for function forms in class forms
        forms.forms()
    #if argument items is called then the if statement will run
    if args.items:
        #calls for function held_items in class held_items
        held_items.held_items()
    #if argument gameversion is called then the if statement will run
    if args.gameversion:
        #calls for function gameversion in class gameversion
        gameversion.gameversion()
    #if argument picture is called then the if statement will run
    if args.picture:
        #calls for function image in class image
        image.image()
    #checks the lengh of the arguments given. If its lower then 2. It will run.
    if len(sys.argv) < 2:
        #runs the function called run_all() which contains all classes. Making all the classes run
        run_all()

#Will run the pokemon function regardless of arguments
pokemon.pokemon()
#Will check & see if the user uses a argument

argument_check()

#Prints out help information for the user when the program finishes
print(Fore.YELLOW, Style.BRIGHT,"\nFor more information.\nUse -h when launching the program for more help", Style.NORMAL, Fore.RESET)
