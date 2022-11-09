import json
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot cwnd vs time')
parser.add_argument('--file', type=str, help='The file to plot')
args = parser.parse_args()

json_object = open(args.file)
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