# Copyright (c) 2021 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == GET CONFIG VALUES ==
fname = config['psd']
new_name  = config['new_name']
#channel_list  = json.loads(config['channel_list'])
channel_list1  = config['channel_list']
channel_list = channel_list1.replace('[','').replace(']','').split(", ")

'''  
# Gradiometers
channel_list = [
    'MEG2042','MEG2043','MEG1913','MEG1912','MEG2113','MEG2112','MEG1922','MEG1923','MEG1942','MEG1943',
    'MEG1642','MEG1643','MEG1933','MEG1932','MEG1733','MEG1732','MEG1723','MEG1722','MEG2143','MEG2142',
    'MEG1742','MEG1743','MEG1712','MEG1713',
    'MEG2032','MEG2033','MEG2313','MEG2312','MEG2342','MEG2343','MEG2322','MEG2323','MEG2433','MEG2432',
    'MEG2122','MEG2123','MEG2333','MEG2332','MEG2513','MEG2512','MEG2523','MEG2522','MEG2133','MEG2132',
    'MEG2542','MEG2543','MEG2532','MEG2533']

    MEG2042, MEG2043, MEG1913, MEG1912, MEG2113, MEG2112, MEG1922, MEG1923, MEG1942, MEG1943, MEG1642, MEG1643, MEG1933, MEG1932, MEG1733, MEG1732, MEG1723, MEG1722, MEG2143, MEG2142, MEG1742, MEG1743, MEG1712, MEG1713, MEG2032, MEG2033, MEG2313, MEG2312, MEG2342, MEG2343, MEG2322, MEG2323, MEG2433, MEG2432, MEG2122, MEG2123, MEG2333, MEG2332, MEG2513, MEG2512, MEG2523, MEG2522, MEG2133, MEG2132, MEG2542, MEG2543, MEG2532, MEG2533

# Magnetometers
channel_list = [
    'MEG2041','MEG1911','MEG2111','MEG1921','MEG1941','MEG1641',
    'MEG1931','MEG1731','MEG1721','MEG2141','MEG1741','MEG1711',
    'MEG2031','MEG2311','MEG2341','MEG2321','MEG2431','MEG2121',
    'MEG2331','MEG2511','MEG2521','MEG2131','MEG2541','MEG2531']
'''


# == LOAD DATA ==
df_psd = pd.read_csv(fname, sep='\t')

# Get only selected channels
sel_data = df_psd[df_psd.channels.isin(channel_list)].copy()

# Average channels
avd_data = np.mean(sel_data, axis=0)
std_data = np.std(sel_data, axis=0)


# Channels averaged
chin  = list(set(sel_data.channels).intersection(set(channel_list)))
chout = list(set(sel_data.channels).difference(set(channel_list)))
#chin == sel_data.channels
print('- Channels averaged (', len(chin) ,'):', *chin,  sep=' ')
print('- Channels not found (',len(chout),'):', *chout, sep=' ')

# == SAVE FILE ==
df_psd_avg = pd.DataFrame(avd_data, columns=[new_name]).transpose()
df_psd_avg.index.name = 'channels'
df_psd_avg.columns.name = 'freqs'
df_psd_avg.to_csv(os.path.join('out_dir','psd.tsv'), sep='\t')

#List of frequencies
freqs = df_psd_avg.columns.to_numpy()
freqs = freqs.astype(float)

# == FIGURES ==
plt.figure(1)
plt.plot(freqs,avd_data)
plt.xticks(freqs[::40]) #take every 40th value in 'freqs'
plt.fill_between(freqs, avd_data+std_data, avd_data-std_data, facecolor='blue', alpha=0.2)
plt.grid(visible=1, alpha=0.5)
plt.xlim(freqs[0], freqs[-1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD')
plt.title('Averaged PSD')
plt.savefig(os.path.join('out_figs','avg_channels.png'))




