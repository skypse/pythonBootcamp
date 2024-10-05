games = ["Dark Souls", "DDTank", "Legion TD2"]
GOTY_2023 = "Baldur's Gate III"

# Há 'Dark Souls' em games? SIM = true
print("Dark Souls" in games) # true

# Há 'LOL' em games? NÃO = false
print("LOL" in games) # false

# Há 'DDTank' em games? SIM = True
# Mas estamos utilizando o 'not in', que inverte a operação
print("DDTank" not in games) # false

# Há 'Legion Td2' em games? NÃO = false
# CASE_SENSITIVE!
print("Legion Td2" in games) # false

# Há 'Gate' na string GOTY_2023 ? SIM = true
print("Gate" in GOTY_2023) # true