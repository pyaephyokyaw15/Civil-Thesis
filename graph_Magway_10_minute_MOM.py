import matplotlib.pyplot as plt
import data
import matplotlib

# data
years = list(range(2003, 2023))
recorded_wind_speeds = data.MAGWAY_10_MINUTE_WIND_SPEED
estimated_wind_speeds = data.MAGWAY_10_MINUTE_Wi_star
LCL_95 = data.MAGWAY_10_MINUTE_LCL_95
UCL_95 = data.MAGWAY_10_MINUTE_UCL_95

# Setting font properties
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 12

# Plotting
plt.xticks(years)  # Set the x-ticks to exactly 20 years
plt.plot(years, recorded_wind_speeds, marker='o', linestyle='-', label='Recorded(gust wind)')
plt.plot(years, calculated_wind_speeds, marker='s', linestyle='-', label='Gumbel using MOM')
plt.title('Magway 10 minute')
plt.xlabel('Year')
plt.ylabel('Maximum Wind Speed(m/s)')



plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()