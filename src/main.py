from . import read_json
from .calculator import calculate_bmi, find_health_risk


def find_overweight_population():
    data = read_json.from_file()
    for person in data:
        pass