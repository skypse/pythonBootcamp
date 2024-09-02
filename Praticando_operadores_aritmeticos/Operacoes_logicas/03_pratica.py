# Operação lógica com o 'NOT'

comidas_na_geladeira = []

# 1000 é maior que 1500? NÃO, mas o operador 'NOT', inverte!
# retornando 'True'
test_not01 = not 1000 > 1500 # true!
print(test_not01)

# comidas_na_geladeira é false?
# listas vazia tem valor booleano = false
test_not02 = not comidas_na_geladeira # true!
print(test_not02)

# essa string é verdadeira, porque há um valor então seria 'True'
# mas o 'not' inverte esse valor para 'False'
test_not03 = not "saque 1500;" # false!
print(test_not03)

# essa string é false, porque está vazia é = false.
# mas com o 'not' ele inverte tornando em 'true'
test_not04 = not "" # true!
print(test_not04)

