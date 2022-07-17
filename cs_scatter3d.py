import matplotlib.pyplot as plt
import pandas as pd


# data from https://allisonhorst.github.io/palmerpenguins/

def scatter3d():
    data_adelie = pd.read_csv('ML_examples/penguins_adelie.csv')
    data_adelie['Species'] = 'Adelie'
    data_gentoo = pd.read_csv('ML_examples/penguins_gentoo.csv')
    data_gentoo['Species'] = 'Gentoo'
    data_chinstrap = pd.read_csv('ML_examples/penguins_chinstrap.csv')
    data_chinstrap['Species'] = 'Chinstrap'

    data_penguins = pd.concat([data_adelie, data_gentoo, data_chinstrap])[
        ['Species', 'Flipper Length (mm)', 'Culmen Length (mm)', 'Culmen Depth (mm)']]

    data = data_penguins.reset_index(drop=True).dropna().reset_index(drop=True)

    data.columns = ['Species', 'Flipper Length', 'Culmen Length', 'Culmen Depth']

    scat = plt.figure().gca(projection='3d')
    for i in ['Adelie', 'Gentoo', 'Chinstrap']:
        scat.scatter(data[data['Species'] == i]['Flipper Length'],
                     data[data['Species'] == i]['Culmen Length'],
                     data[data['Species'] == i]['Culmen Depth']
                     )

    scat.set_xlabel('Flipper Length')
    scat.set_ylabel('Culmen Length')
    scat.set_zlabel('Culmen Depth')

    scat.legend(['Adelie', 'Gentoo', 'Chinstrap'], loc=2)

    plt.show()
