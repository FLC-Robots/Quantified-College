import csv
import pandas as pd
import numpy as np

class data_processor():
    def __init__(self):
        pass
    def get_csv_data(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    def process_csv_data(self, path):
        df = pd.DataFrame(self.get_csv_data(path))
        print(df.head)

        