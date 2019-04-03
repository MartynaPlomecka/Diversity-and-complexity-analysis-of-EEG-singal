import numpy as np
from scipy.io import loadmat
from collections import Counter
import os
import itertools
import math

data_dir = 'dane'
filenames = ['noise.mat', 'siv_wave.mat']
paths = list(map(lambda x: os.path.join(data_dir, x), filenames))

def discretize(series):
    median = np.median(series)
    return ''.join(map(lambda x: '1' if x > median else '0', series))

def compute_prob(items):
    c=Counter(items)
    return dict(map(lambda x: (x, c[x] / len(items)), c))

def states_from_timeseries(ts):
    binary_series = discretize(ts)
    return [binary_series[i:i+4] for i in range(len(binary_series)-3)]

def get_transitions(states):
    state_pairs = [tuple(states[i:i+2]) for i in range(len(states)-1)]
    return state_pairs


def FC(ts):
    states_list = states_from_timeseries(ts)
    states_prob = compute_prob(states_list)
    transitions_list = get_transitions(states_list)
    transitions_prob = compute_prob(transitions_list)

    def compute_fc(unique_states):
        def net_information_gain(i, j):
            return math.log(states_prob[i] / states_prob[j], 2)

        # Equivalent to:
        # s = 0
        # for i in unique_states
        #   for j in unique_states
        #     s += transitions_prob.get((i,j), 0.) * net_information_gain(i,j)**2
        # return s
        return sum([transitions_prob.get((i, j), 0.) * net_information_gain(i, j) ** 2
                    for i, j in itertools.product(unique_states, unique_states)])

    return compute_fc(np.unique(states_list))

def read_and_run(path, name='X'):
    data_blob = loadmat(path)
    data = data_blob[name][0]
    print(data)
    print(FC(data))
    #print(FC(data[data_blob]))