# Operação lógica com o 'Parênteses'

saldo = 1000
saque = 250
limite = 250
conta_especial = True

test01 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(test01)

# primeiro grupo:
# saldo é maior ou igual que saque ? SIM | saque é menor ou igual ao limite? SIM = True
# segundo grupo:
# conta_especial = true | saldo é maior ou igual que saque? SIM = True
test02 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #  True!
print(test02)