string = input("Digite a palavra: ")

index = int(input("Digite um numero: "))

tamanho_string = len(string)

if index > tamanho_string:
    index = tamanho_string % index
    
print(string)

troca = string[index]
print(f"A letra que irá ser retirada é {string[index]}")

for value, caracter in enumerate(string):
    if caracter == troca:
        string == string.replace(string[value], "0")
        break
for i, c in enumerate(string):
    if c == "0":
        pass
    else:
        print(f"index: {i} / caractere: {c}")
        
