'''
create an empty dictonary of cricket_players
* add following data to dictonary
* "ajinkya" : 1, "virat" : 7 , "jadeja" : 3, "bumrah": 5 , "bhuvaneshvar" : 2
* print all player names only (keys) from dictonary
* print all player numbers only (values) from dictionary
* print both player_name and number from dictonary
* find "bhuvaneshvar" in dictonary (remember to use the syntax dicotnary[key])
''' 

cricket_players = {}
cricket_players["ajinkya"]=1
cricket_players["virat"]=7
cricket_players["jadeja"]=3
cricket_players["bumrah"]=5
cricket_players["bhuneshvar"]=2

for player in cricket_players.keys():
    print(player)
    
for player in cricket_players.values():
    print(player)
    
for player_name,number in cricket_players.items():
    print(player_name+" "+ str (number) )
    
if "bhuneshvar" in cricket_players:
    print("bhuneshvar found")
    
'''    
ajinkya
virat
jadeja
bumrah
bhuneshvar
1
7
3
5
2
ajinkya 1
virat 7
jadeja 3
bumrah 5
bhuneshvar 2
bhuneshvar found
'''
