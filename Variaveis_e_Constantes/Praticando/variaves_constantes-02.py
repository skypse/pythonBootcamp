# Definindo constantes
TAX_VALOR = 0.07 # 7% imposto

# Definindo variáveis
item_preco = 100.0
quantidade = 4
total_custo = item_preco * quantidade # custo sem imposto
tax_valor = total_custo * TAX_VALOR # valor do imposto
preco_final = total_custo + tax_valor # preço final com imposto

print("Constante:")
print(f"TAX_VALOR: {TAX_VALOR:.2f}")

print("\nVariáveis:")
print(f"Preço do item: {item_preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Custo total (sem imposto): {total_custo:.2f}")
print(f"Valor do imposto: {tax_valor:.2f}")
print(f"Preço final (com imposto): {preco_final:.2f}")
