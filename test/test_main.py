from hamcrest import assert_that, equal_to, is_

from src.main import find_overweight_population


def test_find_overweight_population():
    expected = {
        'Underweight': 1, 
        'Normal Weight': 1, 
        'Overweight': 0, 
        'Moderately Obese': 1, 
        'Severely Obese': 0, 
        'Very Severely Obese': 1
        }
    assert_that(find_overweight_population('test/fixture.json'), is_(equal_to(expected)))
