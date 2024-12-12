n: int = int(input("Digite a quantidade de produtos: "))

names: list[str] = [0 for _ in range(n)]
purchase_price: list[float] = [0 for _ in range(n)]
sale_price: list[float] = [0 for _ in range(n)]

profit_below_ten_percent = 0
profit_between_ten_and_twenty_percent = 0
profit_above_twenty_percent = 0

value_total_purchase = 0
value_total_sale = 0
total_profit = 0

for i in range(n):
    names[i] = input(f"Digite o nome do {i + 1}° produto: ")
    purchase_price[i] = float(input(f"Digite o preço de compra do {i + 1}° produto: "))
    sale_price[i] = float(input(f"Digite o preço de venda do {i + 1}° produto: "))

for i in range(n):
    profit = (sale_price[i] - purchase_price[i]) / purchase_price[i] * 100

    if profit < 10:
        profit_below_ten_percent += 1
    elif profit < 20:
        profit_between_ten_and_twenty_percent += 1
    else:
        profit_above_twenty_percent += 1

for i in range(n):
    value_total_purchase += purchase_price[i]
    value_total_sale += sale_price[i]

total_profit = value_total_sale - value_total_purchase

print(f"Quantidade de produtos com lucro abaixo de 10%: {profit_below_ten_percent}")
print(
    f"Quantidade de produtos com lucro entre 10% e 20%: {profit_between_ten_and_twenty_percent}"
)
print(f"Quantidade de produtos com lucro acima de 20%: {profit_above_twenty_percent}")
print(f"Valor total de compra: R${value_total_purchase:.2f}")
print(f"Valor total de venda: R${value_total_sale:.2f}")
print(f"Valor total de lucro: R${total_profit:.2f}")
