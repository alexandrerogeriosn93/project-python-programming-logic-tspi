def return_basic_value(gender):
    match gender:
        case "m":
            return 10
        case "f":
            return 8


def calc_total_drinks(beers, soft_drinks):
    return beers * 2.50 + soft_drinks * 2


def calc_total_skewers(skewers):
    return skewers * 4


def return_artistic_value(total_food_and_drink):
    return 3 if total_food_and_drink <= 15 else 0


def calc_sub_total(basic_value, total_drinks, total_skewers, artistic_value):
    return basic_value + total_drinks + total_skewers + artistic_value


def calc_total(sub_total):
    return sub_total + sub_total * 0.10


gender: str = input("Qual o sexo do cliente (m/f)? ")
beers: int = int(input("Quantas cervejas foram consumidas? "))
soft_drinks: int = int(input("Quantos refrigerantes foram consumidos? "))
skewers: int = int(input("Quantos espetinhos foram consumidos? "))

basic_value = return_basic_value(gender)
total_drinks = calc_total_drinks(beers, soft_drinks)
total_skewers = calc_total_skewers(skewers)
total_drinks_and_skewers = total_drinks + total_skewers
total_artistic_value = return_artistic_value(total_drinks_and_skewers)
sub_total = calc_sub_total(
    basic_value, total_drinks, total_skewers, total_artistic_value
)
total = calc_total(sub_total)

print("Valor da conta")
print(f"R$ {basic_value:.2f} (valor básico)")
print(f"R$ {total_drinks_and_skewers:.2f} (bebida e comida)")
print(f"R$ {total_artistic_value:.2f} (cantores)")
print(f"R$ {sub_total:.2f} (subtotal sem 10%)")
print(f"R$ {total:.2f} (total)")
