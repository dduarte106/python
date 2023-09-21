a = "Dj Ramon"
b = "Jesus Cristo"

concaternar = (a + " e " + b + "\n")
print(concaternar)
concaternar = concaternar.upper() #deixar tudo em maisuclo

print(concaternar)

concaternar = concaternar.lower() #deixar tudo em minusculo

print(concaternar)

print(concaternar.strip()) #remove caracteres especiais ou linhas puladas
print("Dj Ramemes")

print("\n -*-NOVOS EXERCICIOS-*- \n")
#_______________________________
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)
print("\n")

minha_lista = minha_string.split("r") 
#tirar uma palavra ou letra da string
print(minha_lista)

#_______________________________
print("\n BUSCAR UMA PALAVRA NOVA \n")

busca = minha_string.find("rei")

print(busca)

 #______________________________

print("\n SUBSTITUIR PALVRAS \n")

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

