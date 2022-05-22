def calculate_bmi(weight, height):
    # BMI(kg/m2) = mass(kg) / height(m)2
    return True

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


