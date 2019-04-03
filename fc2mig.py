#creating plots for comparing FC & MIG

import fc
import mig
from sinus import sinuses
from scipy.io import loadmat

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


noise = loadmat('dane/noise.mat')['X'][0]
migs = list(map(mig.MIG, sinuses))
fcs = list(map(fc.FC, sinuses))
# migs.append(mig.MIG(noise))
# fcs.append(fc.FC(noise))

# max = 5 # = log_2 (2 * 16)
# migs = [x / max for x in migs]

print(migs)
print(fcs)

eeg_fcs = [
    1.69455974791394,
    1.32688570507392,
    1.61087940732341,
    1.44948725048326,
    1.79502189947243,
    1.33493448420028,
    1.4822149499622,
    1.19309790264157,
    1.51899440581486,
]

eeg_migs = [
    3.35793819709446,
    3.53239682853587,
    3.84466871646907,
    3.45576247775813,
    3.65998835153399,
    2.95861027627032,
    3.35923193629349,
    3.30023117562533,
    3.18795821518606,
]

plt.scatter(migs, fcs, label="sinuses")
plt.scatter([mig.MIG(noise)], [fc.FC(noise)], label="noise")
plt.scatter(eeg_migs, eeg_fcs, label="eeg")
plt.gca().set_xlim(-0.1)
plt.gca().set_ylim(-0.1)
plt.xlabel("MIG")
plt.ylabel("FC")
plt.legend()
plt.show()
