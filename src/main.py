from . import read_json
from .calculator import calculate_bmi, find_health_risk


def find_overweight_population(file_path='data.json'):
    population_info = {
        'Underweight': 0,
        'Normal Weight': 0,
        'Overweight': 0,
        'Moderately Obese': 0,
        'Severely Obese': 0,
        'Very Severely Obese': 0
    }
    data = read_json.from_file(file_path)
    for person in data:
        bmi = calculate_bmi(height=person['HeightCm'], weight=person['WeightKg'])
        risk = find_health_risk(bmi)
        population_info[risk['category']] = population_info[risk['category']] + 1

    return population_info

