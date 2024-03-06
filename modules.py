import datetime
from datetime import date
# import time
from time import time

from camelcase import CamelCase
# today = datetime.date.today()

today = date.today()
# timestamp = time.time()

# print(timestamp)


c = CamelCase()
print(c.hump('hello there world!'))