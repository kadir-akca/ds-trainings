import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d

from sklearn.cluster import KMeans


# data from https://allisonhorst.github.io/palmerpenguins/

def scatter():
    data_adelie = pd.read_csv('ML_examples/penguins_adelie.csv')
    data_adelie['Species'] = 'Adelie'
    data_gentoo = pd.read_csv('ML_examples/penguins_gentoo.csv')
    data_gentoo['Species'] = 'Gentoo'
    data_chinstrap = pd.read_csv('ML_examples/penguins_chinstrap.csv')
    data_chinstrap['Species'] = 'Chinstrap'

    data_penguins = pd.concat([data_adelie, data_gentoo, data_chinstrap])[
        ['Species', 'Flipper Length (mm)', 'Culmen Length (mm)', 'Culmen Depth (mm)']]

    data_penguins = data_penguins.reset_index(drop=True)

    data = data_penguins.dropna().reset_index(drop=True)

    data.columns = ['Species', 'Flipper Length', 'Culmen Length', 'Culmen Depth']

    print(data)

    for sp in ['Adelie', 'Gentoo', 'Chinstrap']:
        plt.scatter(data[data['Species'] == sp]['Flipper Length'], data[data['Species'] == sp]['Culmen Length'],
                    data[data['Species'] == sp]['Culmen Depth'], alpha=.75, linewidths=.5, label=sp)
    plt.legend()
    plt.xlabel('Flipper Length (mm)')
    plt.ylabel('Culmen Length (mm)')
    plt.show()
