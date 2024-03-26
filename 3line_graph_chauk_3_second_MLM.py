import matplotlib.pyplot as plt
import data
import matplotlib

# data
years = data.T
calculated_wind_speeds = data.CHAUK_3_SECOND_WT
UCL_95 = data.CHAUK_3_SECOND_UCL_95
LCL_95 = data.CHAUK_3_SECOND_LCL_95


# Setting font properties
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 12

# Plotting
plt.plot(range(len(years)), calculated_wind_speeds, marker='s', linestyle='-', label='Estimated wind speed using MLM')
plt.plot(range(len(years)), UCL_95, marker='^', linestyle='-', label='UCL at 95% level')
plt.plot(range(len(years)), LCL_95, marker='d', linestyle='-', label='LCL at 95% level')

# Set x-axis ticks and labels
plt.xticks(range(len(years)), years)

plt.title('Chauk 3 seconds')
plt.xlabel('Return Period (yr)')
plt.ylabel('Maximum Wind Speed(m/s)')



plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()