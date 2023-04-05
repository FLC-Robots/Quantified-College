# pip install MIDIUtil

import pandas as pd
from midiutil import MIDIFile
import os


# Read the CSV file
data = pd.read_csv("Data/testpur - convertcsv.csv")  # Replace with your CSV file path

# Normalize the data
data["temp_normalized"] = (data["temperature"] - data["temperature"].min()) / (data["temperature"].max() - data["temperature"].min())
data["humidity_normalized"] = (data["humidity"] - data["humidity"].min()) / (data["humidity"].max() - data["humidity"].min())
data["pressure_normalized"] = (data["pressure"] - data["pressure"].min()) / (data["pressure"].max() - data["pressure"].min())

degree_range = (36, 96)  # C2 to C7 

midi = MIDIFile(3)  # Create a MIDI file with 3 tracks (channels)
midi.addTempo(0, 0, 120)  # Set tempo to 120 BPM 
midi.addTempo(1, 0, 120)
midi.addTempo(2, 0, 120)

time = 0
for index, row in data.iterrows():
    # Map data to pitch and velocity
    temp_pitch = int(degree_range[0] + row["temp_normalized"] * (degree_range[1] - degree_range[0]))
    temp_velocity = int(row["temp_normalized"] * 127)
    
    humidity_pitch = int(degree_range[0] + row["humidity_normalized"] * (degree_range[1] - degree_range[0]))
    humidity_velocity = int(row["humidity_normalized"] * 127)
    
    pressure_pitch = int(degree_range[0] + row["pressure_normalized"] * (degree_range[1] - degree_range[0]))
    pressure_velocity = int(row["pressure_normalized"] * 127)

    # Add MIDI events
    midi.addNote(0, 0, temp_pitch, time, 1, temp_velocity)  # Temperature
    midi.addNote(1, 1, humidity_pitch, time, 1, humidity_velocity)  # Humidity
    midi.addNote(2, 2, pressure_pitch, time, 1, pressure_velocity)  # Pressure

    time += 1  # Increment time by 1


# ... (previous code to generate MIDI events)

# Save the MIDI file to a specific folder
folder_path = "Data/mid_purpleair"  # Specify the desired folder path
filename = "output.mid"  # Choose the desired filename for the output MIDI file

output_file_path = os.path.join(folder_path, filename)

with open(output_file_path, "wb") as output_file:
    midi.writeFile(output_file)

