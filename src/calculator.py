from math import pow


from .Category import Category
from .Risk import Risk


def convert_cm_to_m(measurement):
    return measurement / 100


def calculate_bmi(weight, height):
    '''
    Takes arguments of weight in kg and height in centimetres.
    Returns BMI in kg/m^2 using the formula:
    BMI(kg/m2) = mass(kg) / height(m)2
    '''
    height_m = convert_cm_to_m(height)
    height_sq = pow(height_m, 2)
    bmi = weight / height_sq

    return round(bmi, 2)


def find_health_risk(bmi):
    group = Category.VERY_SEVERE
    risk = Risk.VERY_SEVERE
    if bmi <= 18.4:
        group = Category.UNDER
        risk = Risk.UNDER
    elif bmi <25:
        group = Category.NORMAL
        risk = Risk.NORMAL
    elif bmi <30:
        group = Category.OVER
        risk = Risk.OVER
    elif bmi < 35:
        group = Category.MODERATE
        risk = Risk.MODERATE
    elif bmi < 40:
        group = Category.SEVERE
        risk = Risk.SEVERE

    return {
        'category': group.value,
        'health risk': risk.value
    }

