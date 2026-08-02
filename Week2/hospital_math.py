def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def calculate_bsa(weight, height):
    bsa = (weight ** 0.425) * (height ** 0.725) * 0.007184
    return round(bsa, 2)