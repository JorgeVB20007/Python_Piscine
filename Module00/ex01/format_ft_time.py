from time import time
from datetime import date

ts = time()
formatted_date = date.today().strftime("%b %d %Y")

print("Seconds since January 1, 1970: {0:,.4f} or {1:.2e} in \
scientific notation".format(ts, ts))
print(formatted_date)
