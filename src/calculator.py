from math import pow


def convert_cm_to_m(measurement):
    return measurement / 100


def calculate_bmi(weight, height):
    '''
    Takes arguments of weight in kg and height in centimetres.
    Returns BMI in kg/m^2 using the formula:
    BMI(kg/m2) = mass(kg) / height(m)2
    '''
    height_m = convert_cm_to_m(height)
    print(f'height in m {height_m}')
    height_sq = pow(height_m, 2)
    bmi = weight / height_sq
    return round(bmi, 2)


def find_health_risk(bmi):
    category = ''
    risk = ''
    if bmi <= 18.4:
        category = 'Underweight'
        risk = 'Malnutrition Risk'
    elif bmi <25:
        category = 'Normal Weight'
        risk = 'Low risk'
    elif bmi <30:
        category = 'Overweight'
        risk = 'Enhanced Risk'
    elif bmi < 35:
        category = 'Moderately Obese'
        risk = 'Medium Risk'
    elif bmi < 40:
        category = 'Severely Obese'
        risk = 'High Risk'
    else:
        category = 'Very Severely Obese'
        risk = 'Very High Risk'

    return {
        'category': category,
        'health risk': risk
    }

