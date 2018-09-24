question=input ("Hello! Welcome to Nicks Game Store! Todays special is street fighter 2! and its 50 Bucks!")

Store_game = {
    'title':"Street Fighter 2.",
    'genre':"2D Fighting.",
    'release date':"1991.",
    'cost':50,
    'platform':("Super Nintendo.")}

me = {
    "money":100
    }

if Store_game["cost"] < me["money"]:
    print("you got Street Fighter! You got 50 bucks left!")

question=input ("We Also Have Super mario world For sale on 30$ ")

Store_game = {
    'title':"Super Mario World.",
    'genre':"Platformer.",
    'release date':"1990.",
    'cost':30,
    'platform':("Super Nintendo.")}

me = {
    "money":50
    }

if Store_game["cost"] < me["money"]:
    print("Congrats! you Got super mario world! you now have 2 games! and 20$ left!")

question=input ("We also Have Kirby Superstar on sale for 20$")

Store_game = {
    'title':"Kirby Superstar.",
    'genre':"Platformer/MiniGames",
    'release date':"1996.",
    'cost':20,
    'platform':("Super Nintendo.")}

me = {
    'money':20
    }

if Store_game['cost'] <= me['money']:
    print("Congrats! you Got kirby! you now have 3 Games!")
    
Store_game = {
    'title':"Zelda Link to the Past.",
    'genre':"Open world story mode.",
    'release date':"1990.",
    'cost':50,
    'platform':("Super Nintendo.")}

me = {
    "money":20
    }

if Store_game["cost"] > me["money"]:
    print("Sorry Zelda Link to the Past is 30$ you only got 20$")

    question=input ("It's Okay! Not all of us can burn 10 Grand for fun! *burns 10 grand for fun*")

Store_game = {
    'title':"Mortal Kombat 4",
    'genre':"Gory 2D Fighter",
    'release date':"1997",
    'cost':10,
    'platform':("Nintendo 64.")}

me = {
    "money":20
    }

if Store_game["cost"] < me["money"]:

    question=input ("Hey you Mortal kombat 4 great game for dirt cheap! just dont let any kids play it! gory! you have 10 dollars left!")

Store_game = {
    'title':"Bacon King",
    'genre':"not a game Burger",
    'release date':"2018",
    'cost':10,
    'platform':("Burger king")}

me = {
    "money":10
    }

if Store_game["cost"] <= me["money"]:

    question=input ("You got the bacong king! Well.. this aint a game but i mean i bet youe hungry after game shopping! Welp there goes all your money! have fun!")
