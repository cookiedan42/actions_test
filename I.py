import datetime
with open("./test.txt", 'w') as fp:
    fp.write(str(datetime.datetime.now()))