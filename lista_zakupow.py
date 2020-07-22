print("Lista zakupów")
lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "drożdzówka"],
    "warzywniak": ["marchew", "seler", "rukola", "pomidor", "ogórek"]
}
for sklep in lista_zakupow:
  print("Idę do " + sklep + " i kupuję tu nastepujące rzeczy: ")
  print(lista_zakupow["piekarnia"])
  print(lista_zakupow["warzywniak"])

print(" ")

print(lista_zakupow.values())#roboczo

print(" ")

print("W sumię kupuję")
print(len(lista_zakupow["piekarnia"] + lista_zakupow["warzywniak"]))
print("produktów")

name = "mac"
name2 = name.capitalize()
print(name2)
# jak uzyc funkcji capitalize w słowniku?
