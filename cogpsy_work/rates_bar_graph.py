import matplotlib
matplotlib.use('TkAgg') #needed for mac backend image vis
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def stats_check(): #just stats check to ensure accurate bargraphs
    data = pd.read_csv('rates_wide copy.csv')
    split_df = np.split(data, [4], axis = 1) #splits df into list of 2
    ao_df = split_df[0] #the first 4 columns were AO
    av_df = split_df[1] #last 4 were AV
    #print(ao_df.describe())
    #print(av_df.describe())

def avg_bar():
    data = pd.read_csv('rates_wide copy.csv')
    split_df = np.split(data, [4], axis = 1)
    ao_df = split_df[0]
    av_df = split_df[1]
#getting std and avgs of each column and putting in list for bargraphs
    ao_std_list = []
    av_std_list = []
    ao_mean_list = []
    av_mean_list = []
    ao_std = ao_df.std(axis=0)
    av_std = av_df.std(axis=0)
    ao_avgs = ao_df.mean(axis=0)
    av_avgs = av_df.mean(axis=0)

    for std in ao_std:
        ao_std_list.append(std)
    for std in av_std:
        av_std_list.append(std)
    for avg in ao_avgs:
        ao_mean_list.append(avg)
    for avg in av_avgs:
        av_mean_list.append(avg)
#setting up bargraph parameters
    labels = ['MultiNod', 'Nod', 'Shake', 'Total']
    ao_error = ao_std_list
    av_error = av_std_list
    x = np.arange(len(labels))
    width = 0.4
    fig, ax = plt.subplots()
#setting up bar info
    #ao_bar = ax.bar(x - width/2, ao_mean_list, width, label = 'AO', color='blue') #no error bars
    #av_bar = ax.bar(x + width/2, av_mean_list, width, label = 'AV', color='red') #^
    ao_w_error = ax.bar(x - width/2, ao_mean_list, width, label = 'AO', color='blue', yerr = ao_error, align='center', alpha=0.5, ecolor='black', capsize=10)
    av_w_error = ax.bar(x + width/2, av_mean_list, width, label = 'AV', color='red', yerr = av_error, align='center', alpha=0.5, ecolor='black', capsize=10)
#labels labels labels
    ax.set_ylabel('Averages')
    ax.set_xlabel('AO/AV')
    ax.set_title('AO vs. AV Averages')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.yaxis.grid(True)
    ax.legend()
#more label
    ax.bar_label(ao_w_error, padding = 3)
    ax.bar_label(av_w_error, padding = 3)

    fig.tight_layout()
    plt.savefig('ao_av_avg_bar') #saves bargraph as png to same path as main.py
    plt.show()


if __name__ == '__main__':
    avg_bar()
    stats_check()
