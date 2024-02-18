from datetime import date, timedelta

current_date = date.today()
result = current_date - timedelta(days=5)
print(result)
