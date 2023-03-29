import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    def testGraph(self):

        plt.style.use('_mpl-gallery')

        # make data
        x = np.linspace(0, 10, 100)
        y = 4 + 2 * np.sin(2 * x)

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()

        