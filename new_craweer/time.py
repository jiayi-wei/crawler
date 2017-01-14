import datetime

timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
tt=(datetime.datetime.now()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
print(tt)
print(timestamp)
