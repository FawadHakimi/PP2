from datetime import datetime
current = datetime.now()
drop = current.replace(microsecond=0)
print(drop)