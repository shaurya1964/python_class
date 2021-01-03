keys = ["SRK", "Salman", "Amir"]
names = {
  "SRK" : 20,
  "Salman" : 40,
  "Amir" : 50
}
print(names)
for key_label in names.keys():
  print(key_label)
for key_label in names.values():
  print(key_label)
names["Akshay"] = 60
print (names) 
names["Salman"] = 80
print(names)
for key_label, value_label in names.items():
  print(key_label+" "+ str(value_label))

   ======================
    OUTPUT
  
#  {'SRK': 20, 'Salman': 40, 'Amir': 50}
#SRK
#Salman
#Amir
#20
#40
#50
#{'SRK': 20, 'Salman': 40, 'Amir': 50, 'Akshay': 60}
#{'SRK': 20, 'Salman': 80, 'Amir': 50, 'Akshay': 60}
#SRK 20
#Salman 80
#Amir 50
#Akshay 60
