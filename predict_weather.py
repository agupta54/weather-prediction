import matplotlib.pyplot as plt 
import numpy as np 

# Read in the weather data 
weather_filename = "fort_lauderdale.csv"
weather_file = open(weather_filename)
weather_data = weather_file.read()
weather_file.close()

# Break the weather records into files 
lines = weather_data.split("\n")

labels = lines[0]
values = lines[1:]
n_values = len(values)

# Break the list of comma-separated value strings into list of values 
year = []
month = []
day = []
max_temp = []
min_temp = []
j_year = 1 # column id of each variable 
j_month = 2 
j_day = 3 
j_max_temp = 5

for i_row in range(n_values):
    split_values = values[i_row].split(',')
    #print(split_values)
    if len(split_values) >= j_max_temp:
        year.append(int(split_values[j_year]))
        month.append(int(split_values[j_month]))
        day.append(int(split_values[j_day]))
        max_temp.append(float(split_values[j_max_temp]))

# Isolate the missing data 
i_mid = len(max_temp) // 2 
temps = np.array(max_temp[i_mid:])
temps[np.where(temps == -99.9)] = np.nan 

#plt.plot(temps, color='black', marker='.', linestyle='none')
#plt.show()




