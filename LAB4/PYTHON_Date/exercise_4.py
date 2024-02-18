import datetime as dt

date1 = dt.date(2024, 2, 18)
date2 = dt.date(2005, 5, 24)
difference = date1 - date2
print(difference.total_seconds())