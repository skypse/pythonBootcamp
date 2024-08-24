nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

print(f"Olá {nome}, você tem {idade} anos!")
print("Testando quebra de linha do 'end'")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")