# BMI Calculator

## Anaconda Distribution of Python 

If using an Anaconda distribution of Python, create a virtual environment called `bmi` with dependencies:

`conda create --name bmi --file bmi-env.txt`

Activate it:

`conda activate bmi`

NB. There are extra packages added by Anaconda that are not required for this project to run. 


## Running the tests

Make sure your `$PYTHONPATH` is set correctly and run the command: `pytest` from the root of this project.


## Observations

Using the ranges given, some BMIs would fall outside of these ranges, for example 29.94, it is greater than 29.9 but less than 30.