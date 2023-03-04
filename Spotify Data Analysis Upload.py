import pandas as pd

df = pd.read_json('StreamingHistory0.json')

df['endTime'] = pd.to_datetime(df['endTime'], utc=True)

df = df.set_index('endTime')

df.index = df.index.tz_convert('US/Eastern')

df = df.reset_index()

df['msPlayed'] = pd.to_timedelta(df['msPlayed'])

mac = df[df['artistName'].str.contains('Mac Miller', regex=False)]

df['weekday'] = df['endTime'].dt.weekday
df['hour'] = df['endTime'].dt.hour

import matplotlib
import matplotlib.pyplot as plt
df['hour'] = pd.Categorical(df['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

mac_by_day = df['hour'].value_counts()

mac_by_day = mac_by_day.sort_index()

matplotlib.rcParams.update({'font.size': 22})

mac_by_day.plot(kind='bar', figsize=(20,10), title='Mac Miller Songs Listened by Hour')

plt.show()