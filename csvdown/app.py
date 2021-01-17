import wget
from datetime import datetime, timedelta

root_url = 'https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/quote/'

now = datetime.utcnow()
oneday = timedelta(days=1)

today = now.strftime('%Y%m%d')
yesterday = (now - oneday).strftime('%Y%m%d')

filename = yesterday + '.csv.gz'

url = root_url+filename
print(url)