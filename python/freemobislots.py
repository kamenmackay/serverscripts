# Fetch empty slot info from mobibikes and parse into two column table
# | Denman and Pender | 2 empty slots |

import requests
import json

stationdata = "http://vancouver-ca.smoove.pro/api-public/stations"
raw = requests.get(stationdata).text
data = json.loads(raw)

faves = { '0024 Hornby & Pender': '15',
          '0099 Vancouver Art Gallery - North Plaza': '67',
          '0040 Cardero & Davie':'28'}

for station,stationPos in faves.items():
    mrk = int(stationPos)
    emptySlots = int(data['result'][mrk]['free_slots'])
    stationName = str(data['result'][mrk]['name'])
    onlineStatus = (data['result'][mrk]['operative'])
    if station == stationName and onlineStatus == True:
        print("{} ({}) [{}] | {} ".format(station,stationName,onlineStatus,emptySlots))
    else:
        pass

# Future improvements: don't show station if it's not online
