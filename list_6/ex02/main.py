def calc_bank_tax(bank_income, percent):
    return (bank_income * percent) / 100


def calc_salary_or_services_tax(salary_or_services_income):
    if salary_or_services_income <= 8000:
        percent = 0
    elif salary_or_services_income <= 24000:
        percent = 15
    else:
        percent = 20

    return (salary_or_services_income * percent) / 100


def calc_other_incomes(other_incomes, percent):
    return (other_incomes * percent) / 100


def calc_total_tax(tax_bank, tax_salary_or_services, tax_other_incomes):
    return tax_bank + tax_salary_or_services + tax_other_incomes


def calc_rebate(tax_total, percent):
    return (tax_total * percent) / 100


def calc_possible_rebate(medical_services, educational_services):
    return medical_services + educational_services


def calc_tax_total_with_rebate(tax_total, total_rebate):
    return tax_total - total_rebate


bank_income = float(input("Total de rendimentos bancários: "))
salary_or_services_income = float(
    input("Total de rendiemtnos de salários ou serviços: ")
)
other_incomes = float(input("Total de outros rendimentos: "))
medical_services = float(input("Serviços médicos pagos: "))
educational_services = float(input("Serviços educacionais pagos: "))

tax_bank_income = calc_bank_tax(bank_income, 20)
tax_salary_or_services_income = calc_salary_or_services_tax(salary_or_services_income)
tax_other_incomes = calc_other_incomes(other_incomes, 10)
tax_total = calc_total_tax(
    tax_bank_income, tax_salary_or_services_income, tax_other_incomes
)
total_rebate = calc_rebate(tax_total, 30)
total_possible_rebate = calc_possible_rebate(medical_services, educational_services)
tax_total_with_rebate = calc_tax_total_with_rebate(tax_total, total_rebate)

print("\nTotal de impostos:")
print(f"R${tax_bank_income:.2f} (sobre rendimentos bancários)")
print(f"R${tax_salary_or_services_income:.2f} (sobre salários e/ou serviços)")
print(f"R${tax_other_incomes:.2f} (sobre outros rendimentos)")
print(f"R${tax_total:.2f} (total)")
print(f"\nMáximo a ser abatido: R${total_rebate:.2f}")
print("\nTotal de valores possíveis de abater:")
print(f"R${medical_services:.2f} (serviços médicos)")
print(f"R${educational_services:.2f} (serviços educacionais)")
print(f"R${total_possible_rebate:.2f} (total)")
print("\nImposto total:")
print(f"R${tax_total:.2f} (imposto bruto)")
print(f"R${total_rebate:.2f} (abatimentos)")
print(f"R${tax_total_with_rebate:.2f} (total)")
