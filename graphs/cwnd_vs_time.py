import json
import matplotlib.pyplot as plt
from timings import *

json_object = open('out.json')
data = json.load(json_object)

i=1
y = []
x = []
for entry in data['intervals']:
    
    
    datapoint = entry['streams'][0]
    time  = i
    bts = datapoint["snd_cwnd"]
    y.append(bts)
    x.append(time)
    print(bts)
    i+=1

plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('CWND')
plt.show()