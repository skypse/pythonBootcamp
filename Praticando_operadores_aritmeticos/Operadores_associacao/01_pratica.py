curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

# Tem "Python" em curso? SIM = true
print("Python" in curso) # true

# Tem "maça" em frutas? NÃO = false
# Aqui retorna true, pois estamos utilizando o 'NOT IN'
print("maça" not in frutas) # true

# Tem 200 em saques? NÃO = false
print(200 in saques) # false