# This is a sample Python script.
from pybaseball import *
import pandas as pd
from pyemd import emd_samples
from scipy.stats import wasserstein_distance
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns
def difference_matrix():
    print(compare_pitchers(608337,608335))
    pitchy = get_pitcher_ids()
    pitchers = list(pitchy)[:30]
    final = []
    for pitcher in pitchers:
        newline = []
        for pitch in pitchers:
            try:
                newline.append(compare_pitchers(pitch,pitcher)* 10)
                print(pitch)
                print(compare_pitchers(pitch,pitcher))
            except:
                newline.append(0)
                print('added 0')
        final.append(newline)
    test = np.array(final)
    plt.imshow(test)
    plt.show()
def compare_pitchers(one, two):
    x = pitcher_array(one)

    z = pitcher_array(two)
    print(x)
    print(z)
    min_len = min(len(x),len(z))

    return (emd_samples(x[:min_len],z[:min_len]))
def pitcher_array(id):
    data = statcast_pitcher(start_dt="2020-1-1",end_dt='2020-12-31',player_id=id)
    data.dropna()
    pitches = []
    for index, row in data.iterrows():
        pitches.append([row['release_speed'],row['plate_x'],row['plate_z']])
    return pitches
def get_pitcher_ids():
    pitcher_arr = []
    data = statcast(start_dt='2020-9-1',end_dt='2020-10-1')
    for index, row in data.iterrows():
        pitcher_arr.append(int(row['pitcher']))
    return set(pitcher_arr)
def batting_histogram():
    batting = pd.read_csv('batting.csv')
    #hist = batting.hist(column='BA', bins=40)
    sns.set()  # rescue matplotlib's styles from the early '90s

    batting.hist(by='Tm', column='BA')
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    difference_matrix()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
