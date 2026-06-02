def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

bmi, category = bmi_calculator(70, 1.75)

print("BMI:", round(bmi, 2))
print("Category:", category)