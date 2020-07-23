print("Lista zakupów")
lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for sklep in lista_zakupow:
  sklep_C = sklep.capitalize()
  print("Idę do " + sklep_C + " i kupuję tu nastepujące rzeczy: ")
  print(lista_zakupow["piekarnia"])
  print(lista_zakupow["warzywniak"])

print(" ")

print(lista_zakupow.values())#roboczo

print(" ")

print("W sumię kupuję")
print(len(lista_zakupow["piekarnia"] + lista_zakupow["warzywniak"]))
print("produktów")

name = "maciej"
name2 = name.capitalize()
print(name2)

print(" ")

for key in lista_zakupow:
  key_C = key.capitalize() 
  print(key_C)
