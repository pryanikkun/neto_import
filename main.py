import datetime
import emoji

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == "__main__":
    print(f"Сегодня: {datetime.date.today()}")
    calculate_salary()
    get_employees()
    result = emoji.emojize('Python is :red_heart:')
    print(result)
