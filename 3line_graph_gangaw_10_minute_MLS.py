import matplotlib.pyplot as plt
import data
import matplotlib

# data
years = data.T
calculated_wind_speeds = data.GANGAW_10_MINUTE_WT
UCL_95 = data.GANGAW_10_MINUTE_UCL_95
LCL_95 = data.GANGAW_10_MINUTE_LCL_95


# Setting font properties
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 12


plt.plot(range(len(years)), calculated_wind_speeds, marker='s', linestyle='-', label='Estimated wind speed using MLS')
plt.plot(range(len(years)), UCL_95, marker='^', linestyle='-', label='UCL at 95% level')
plt.plot(range(len(years)), LCL_95, marker='d', linestyle='-', label='LCL at 95% level')

# Set x-axis ticks and labels
plt.xticks(range(len(years)), years)

plt.title('Gangaw 10 minute')
plt.xlabel('Return Period (yr)')
plt.ylabel('Maximum Wind Speed(m/s)')



plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()