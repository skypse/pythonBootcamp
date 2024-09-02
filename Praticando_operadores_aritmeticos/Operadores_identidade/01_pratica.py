curso = "Curso de Python na DIO"
nome_curso = curso # = "Curso de Python na DIO"
saldo, limite = 200, 200


# Curso está na mesma posição de memória que nome_curso? SIM = True
print(curso is nome_curso) # True

# Curso está na mesma posição de memória que nome_curso? SIM /
# Mas estamos utilizando o operador NOT que inverte e retorna = False
print(curso is not nome_curso) # False

# saldo está na mesma posição de memória que limite? SIM = True
print(saldo is limite) # True