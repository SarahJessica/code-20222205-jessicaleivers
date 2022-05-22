import pytest
from hamcrest import assert_that, equal_to, is_


from src.calculator import find_health_risk, calculate_bmi, convert_cm_to_m

@pytest.mark.parametrize('cm, m', [
    (123, 1.23), (456, 4.56), (40, 0.4)
])
def test_convert_cm_to_m(cm, m):
    assert_that(convert_cm_to_m(cm), is_(equal_to(m)))


def test_calculate_bmi():
    assert_that(calculate_bmi(75, 175), is_(equal_to(24.49)))


@pytest.mark.parametrize('bmi, category, risk', [
    (5, 'Underweight','Malnutrition Risk'),
    (20, 'Normal weight', 'Low risk'),
    (44, 'Very Severely Obese', 'Very High Risk'),
    (32, 'Moderately Obese', 'Medium Risk'),
    (39, 'Severely Obese', 'High Risk')
])
def test_find_health_risk(bmi, category, risk):
    actual = find_health_risk(bmi)
    expected_resp = {
        'category': category,
        'health risk': risk
    }
    assert_that(expected_resp, is_(equal_to(expected_resp)))
