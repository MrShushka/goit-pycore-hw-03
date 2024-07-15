from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        result = (current_date - input_date).days
        return result
    except: 
        return ('Неправильний формат дати')

print(get_days_from_today('2024-07-12'))