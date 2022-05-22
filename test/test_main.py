import pytest
from hamcrest import assert_that, equal_to, is_


from src import main


def test_calculate_bmi():
    assert_that(main.calculate_bmi(75, 1.75), is_(equal_to(24.49)))


@pytest.mark.parametrize('bmi, category, risk', [
    (5, 'Underweight','Malnutrition Risk'),
    (20, 'Normal weight', 'Low risk'),
    (44, 'Very Severely Obese', 'Very High Risk'),
    (32, 'Moderately Obese', 'Medium Risk'),
    (39, 'Severely Obese', 'High Risk')
])
def test_find_health_risk(bmi, category, risk):
    actual = main.find_health_risk(bmi)
    expected_resp = {
        'category': category,
        'health risk': risk
    }
    assert_that(expected_resp, is_(equal_to(expected_resp)))
