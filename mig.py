from __future__ import division

import numpy as np
from scipy.io import loadmat
from collections import Counter
import os
import itertools
import math

data_dir = 'dane'
filenames = ['Data_8.mat', 'Data_7M_EM_cl.mat']
paths = list(map(lambda x: os.path.join(data_dir, x), filenames))


def discretize(series):
    median = np.median(series)
    return ''.join(map(lambda x: '1' if x > median else '0', series))


def compute_prob(items):
    c = Counter(items)
    return dict(map(lambda x: (x, c[x] / len(items)), c))


def states_from_timeseries(ts):
    binary_series = discretize(ts)
    return [binary_series[i:i + 4] for i in range(len(binary_series) - 3)]


def get_transitions(states):
    state_pairs = [tuple(states[i:i + 2]) for i in range(len(states) - 1)]
    return state_pairs


def MIG(ts):
    states_list = states_from_timeseries(ts)
    states_prob = compute_prob(states_list)
    transitions_list = get_transitions(states_list)
    transitions_prob = compute_prob(transitions_list)

    def compute_mig(unique_states):

        def information_gain(i, j):
            try:
                i_j_prob = transitions_prob.get((i, j), 0.) / states_prob.get(i)
                return math.log(1 / i_j_prob, 2)
            except ZeroDivisionError:
                return 0
        s = 0
        for i in unique_states:
            for j in unique_states:
                s += transitions_prob.get((i, j), 0.) * information_gain(i, j)
        return s

    return compute_mig(np.unique(states_list))

def read_and_run(path):
    data_blob = loadmat(path)
    data = data_blob['EEGCond'][0,0]['data'][0][0]

    chs,obs,trs = data.shape
    for ch in range(chs):
        for tr in range(trs):
            print(MIG(data[ch,:,tr]))
