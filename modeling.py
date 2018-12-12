import math
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

thing = pd.DataFrame(columns = ['t','st','vt','at','ARF','dt'])
thing.loc[0,'t'] = 0
thing.loc[0,'st'] = 200
thing.loc[0,'vt'] = 100
thing.loc[0,'at'] = -9.81
thing.loc[0,'ARF'] = 0
thing.loc[0,'dt'] = 0
interval = 0.01
for i in range(2500):
    thing.loc[i,'t'] = i * interval
    thing.loc[i,'at'] = -9.81
    thing.loc[i,'ARF'] = 6.3 * thing.loc[i,'vt']
    thing.loc[i,'dt'] = thing.loc[i,'ARF'] / 250
    thing.loc[i+1,'vt'] = -thing.loc[i,'dt']*interval + thing.loc[i,'at']*interval + thing.loc[i,'vt']
    thing.loc[i+1,'st'] = thing.loc[i,'st'] + thing.loc[i,'vt'] * interval

thing = thing[['t','st','vt','at','ARF','dt']]
print(max(thing['st']))
print(thing)
plt.figure(1)
plt.plot(thing['t'],thing['st'])
plt.show()
