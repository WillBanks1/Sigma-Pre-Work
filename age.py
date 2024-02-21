from datetime import datetime


current_date = datetime.today()

def age_calculator():
    birth_date_string = input('Enter your date of birth (dd-mm-yyyy)')
    birth_date = datetime.strptime(birth_date_string, '%d-%m-%Y')
    delta_years = current_date.year - birth_date.year
    if (current_date.month < birth_date.month or 
    (current_date.month == birth_date.month and current_date.day < birth_date.day)):
        delta_years -= 1
        
    return delta_years








print(f'You are {age_calculator()} years old')