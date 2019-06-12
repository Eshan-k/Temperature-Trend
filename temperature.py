import pandas as pd
import matplotlib.pyplot as plt

# read city temp data
city_temp = pd.read_csv('city_data.csv')

# read global temp data
global_temp = pd.read_csv('global_data.csv')

# calculate moving average
city_mv_avg = city_temp['avg_temp'].rolling(10).mean()
gbl_mv_avg = global_temp['avg_temp'].rolling(10).mean()

# plot the temperatures
plt.title('New York Temperature Trend')
plt.xlabel('Years')
plt.ylabel('Temperature in Celsius')

# city temp
# plt.plot(city_temp['year'], city_mv_avg, label='City')

# global temp
# plt.plot(global_temp['year'], gbl_mv_avg, label='Global')

# city temp vs global temp
plt.plot(city_temp['year'], city_mv_avg, label='City')
plt.plot(global_temp['year'], gbl_mv_avg, label='Global')
plt.legend()
plt.show()