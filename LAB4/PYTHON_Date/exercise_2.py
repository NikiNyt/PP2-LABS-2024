from datetime import date, timedelta


today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Today is", today)
print("Yesterday was", yesterday)
print("Tomorrow will be", tomorrow)