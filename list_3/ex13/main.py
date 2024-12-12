n: int = int(input("Digite a quantidade de produtos: "))
names: list[str] = []
prices: list[float] = []
quantities: list[int] = []
most_expensive_product_name = names[0]
most_expensive_product_price = prices[0]
quantity_products_below_ten_units = 0
sum_products_prices_below_ten_units = 0

for i in range(n):
    names.append(input(f"Digite o nome do {i + 1}° produto: "))
    prices.append(float(input(f"Digite o preço do {i + 1}° produto: ")))
    quantities.append(int(input(f"Digite a quantidade do {i + 1}° produto: ")))

for name, price, quantity in zip(names, prices, quantities):
    if price > most_expensive_product_price:
        most_expensive_product_price = price
        most_expensive_product_name = name

    if quantity < 10:
        sum_products_prices_below_ten_units += price
        quantity_products_below_ten_units += 1

average_price = sum_products_prices_below_ten_units / quantity_products_below_ten_units

print(f"O nome do produto mais caro é: {most_expensive_product_name}")
print(f"O preço médio dos produtos com quantidade inferior a 10 é: {average_price}")
