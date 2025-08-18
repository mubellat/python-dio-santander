from datetime import datetime
import pytz

data = datetime.now(pytz.timezone("Europa/Oslo"))

print(data)