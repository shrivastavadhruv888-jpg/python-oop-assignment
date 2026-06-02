def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = principal * monthly_rate * (1 + monthly_rate) ** months
    emi /= ((1 + monthly_rate) ** months - 1)

    return emi

emi = calculate_emi(500000, 8, 5)

print("Monthly EMI:", round(emi, 2))