import matplotlib.pyplot as plt
import data
import matplotlib

# data
years = list(range(2003, 2023))
recorded_wind_speeds = data.MAGWAY_3_SECOND_WIND_SPEED
calculated_wind_speeds = data.MAGWAY_3_SECOND_Wi_star

# Setting font properties
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 12

# Plotting
plt.xticks(years)  # Set the x-ticks to exactly 20 years
plt.plot(years, recorded_wind_speeds, marker='o', linestyle='-', label='Recorded(gust wind)')
plt.plot(years, calculated_wind_speeds, marker='s', linestyle='-', label='Gumbel using MOM')
plt.title('Magway 3 seconds')
plt.xlabel('Year')
plt.ylabel('Maximum Wind Speed(m/s)')



plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()