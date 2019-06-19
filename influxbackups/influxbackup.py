
#~/usr/bin/python

# Make backup dir in influxbackup with date as directory name
# Change into current date directory
# Backup data from remote influxdb into current date dir


import os, sys
import datetime
import subprocess
from influxdb import InfluxDBClient

influxbackuppath = "/data/influxbackups"
now = datetime.datetime.now()
currentdate = now.strftime('%m%d%Y')
bupath = influxbackuppath + "/" + currentdate
# Make the below into a function
def crtdir(dur)
  if (os.path.exists(bupath)):
    print(bupath + " already exists so proceeding...")
  else:
    os.mkdir( bupath, 755 );
    print("Path is created")

client = InfluxDBClient(host='10.1.2.16', port=8086)
dbs = client.get_list_database()
# print(dbs)
test = [k.values()[0] for k in dbs]
print(str(test))
for x in test:
 os.mkdir( bupath + "/" + x, 755)
 subprocess.call(["/home/kmackay/influxd","backup","-portable","-database", x, "-host","10.1.2.16:8088", bupath + "/" + x])
