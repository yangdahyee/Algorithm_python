from datetime import datetime, timedelta

utc = datetime.utcnow()
ans = utc + timedelta(hours=9)

print(ans.strftime("%Y-%m-%d"))