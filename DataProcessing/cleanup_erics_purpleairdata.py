import pandas as pd
import numpy as np
df = pd.read_csv('/Users/colincasey/Documents/GitHub/Quantified-College/Data/Raw/data.csv')

# Extract column names
column_names = df.columns

# Convert to NumPy array
column_names_array = np.array(column_names)

wantedfeatures = np.array(['humidity', 'temperature', 'pressure', 'scattering_coefficient', 'deciviews', 'visual_range'], dtype='<U12')

humidity_timeseries = df['humidity']
temperature_timeseries = df['temperature']
pressure_timeseries = df['pressure']

# for i in range():
#     humidity_timeseries_dirtylab = humidity_timeseries[i]
#     i = i + 1

# print(humidity_timeseries_dirtylab)


# fields = "name,model,hardware,location_type,position_rating,led_brightness,firmware_version,rssi,uptime,pa_latency,memory,last_seen,last_modified,date_created,channel_state,channel_flags,channel_flags_manual,channel_flags_auto,confidence,humidity,temperature,pressure,analog_input,pm1.0,pm1.0_atm,pm1.0_cf_1,pm2.5_alt,pm2.5,pm2.5_atm,pm2.5_cf_1,pm2.5_10minute,pm2.5_30minute,pm2.5_60minute,pm2.5_6hour,pm2.5_24hour,pm2.5_1week,pm10.0,pm10.0_atm,pm10.0_cf_1,scattering_coefficient,deciviews,visual_range,0.3_um_count,0.5_um_count,1.0_um_count,2.5_um_count,5.0_um_count,10.0_um_count"

# # Split the string into a list of strings
# data_list = fields.split(', ')

# # Convert the list to a NumPy array
# allfeatures = np.array(data_list)

# unwatedfeatures = np.array([])



# # List the columns you want to delete
# columns_to_delete = ['column1', 'column2']

# # Drop the specified columns
# df.drop(columns_to_delete, axis=1, inplace=True)

# # Save the modified DataFrame to a new .csv file
# output_file_path = 'modified_file.csv'
# df.to_csv(output_file_path, index=False)