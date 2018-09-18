question=input ("Hello! Welcome to Nicks Game Store! Todays special is street fighter 2! and its 50 Bucks!")

Store_game = {
    'title':"Street Fighter 2.",
    'genre':"2D Fighting.",
    'release date':"1991.",
    'cost':50,
    'platform':("Super Nintendo.")}


mystore = {'S': 'Street Fighter',}

me = {
    "money":100
    }

if Store_game["cost"] < me["money"]:
    print("you got Street Fighter! You got 50 bucks left!")

question=input ("Want Another game? Type Yes")

Store_game = {
    'title':"Street Fighter 2.",
    'genre':"2D Fighting.",
    'release date':"1991.",
    'cost':50,
    'platform':("Super Nintendo.")}


mystore = {'S': 'Street Fighter',}

me = {
    "money":60
    }

if Store_game["cost"] < me["money"]:
    print("Congrats!")
