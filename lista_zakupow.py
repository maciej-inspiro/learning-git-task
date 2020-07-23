print("Lista zakupów")
lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for sklep in lista_zakupow:
  print("Idę do " + sklep.capitalize() + " i kupuję tu nastepujące rzeczy: ", lista_zakupow[sklep])


print(" ")

print("W sumię kupuję:")
print(len(lista_zakupow["piekarnia"] + lista_zakupow["warzywniak"]))
print("produktów")

print(" ")


#roboczy kod, zostawiam na przyszłość, żeby wiedzieć jak doszedłem do powyższeho rozwiązania
name = "maciej"
name2 = name.capitalize()
print(name2)

print(" ")

for key in lista_zakupow:
  key_C = key.capitalize() 
  print(key_C)
