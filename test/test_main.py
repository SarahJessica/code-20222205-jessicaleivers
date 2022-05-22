import pytest

from src import main

def test_calculate_bmi():
    assert main.calculate_bmi(75,165) == True

@pytest.mark.parametrize('bmi, category, risk', [
    (5, 'Underweight','Malnutrition Risk'),
    (20, 'Normal weight', 'Low risk')
])
def test_find_health_risk(bmi, category, risk):
    actual = main.find_health_risk(bmi)
    expected_resp = {
        'category': category,
        'health risk': risk
    }
    assert expected_resp == actual