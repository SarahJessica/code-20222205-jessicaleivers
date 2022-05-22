from math import pow

def calculate_bmi(weight, height):
    '''
    Takes arguments of weight in kg and height in metres.
    Returns BMI in kg/m^2 using the formula:
    BMI(kg/m2) = mass(kg) / height(m)2
    '''
    height_sq = pow(height, 2)
    bmi = weight / height_sq
    return round(bmi, 2)


def find_health_risk(bmi):
    category = ''
    risk = ''
    if bmi <= 18.4:
        category = 'Underweight'
        risk = 'Malnutrition Risk'
    elif bmi <25:
        category = 'Normal weight'
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

