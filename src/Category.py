from enum import Enum


class Category(Enum):
    UNDER = 'Underweight'
    NORMAL = 'Normal Weight'
    OVER = 'Overweight'
    MODERATE = 'Moderately Obsese'
    SEVERE = 'Severely Obese'
    VERY_SEVERE = 'Very Severely Obese'