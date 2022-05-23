from enum import Enum


class Risk(Enum):
    UNDER = 'Malnutrition Risk'
    NORMAL = 'Low Risk'
    OVER = 'Enhanced Risk'
    MODERATE = 'Medium Risk'
    SEVERE = 'High Risk'
    VERY_SEVERE = 'Very High Risk'