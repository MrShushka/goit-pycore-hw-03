from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_str = user['birthday']
        # Convert birthday string to datetime.date object
        birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        
        # Calculate the birthday for this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If birthday has already passed this year, calculate for next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate days until next birthday
        delta_days = (birthday_this_year - today).days
        
        # Check if birthday falls within the next 7 days (including today)
        if 0 <= delta_days <= 7:
            # Adjust date if birthday falls on a weekend (Saturday or Sunday)
            if birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            # Format congratulation date as 'рік.місяць.дата'
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            
            # Add to the result list
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date_str
            })
    
    return upcoming_birthdays

# Example usage:
users = [
    {'name': 'Іван', 'birthday': '2000.07.10'},
    {'name': 'Петро', 'birthday': '1995.07.15'},
    {'name': 'Марія', 'birthday': '1998.07.18'},
    {'name': 'Олена', 'birthday': '1990.07.09'},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)