from datetime import datetime, timedelta
current_date = datetime.now()
delta = timedelta(days=5)
print(current_date-delta)