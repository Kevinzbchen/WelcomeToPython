import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
sns.set()

norm_rvs = norm(loc=0, scale=20).rvs(size=10000)
plt.hist(norm_rvs, density=True, alpha=0.3, color='b', bins=100, label='original')

mean_array = []
for i in range(1000):
    sample = np.random.choice(norm_rvs, size=5, replace=False)
    mean_array.append(np.mean(sample))
plt.hist(mean_array, density=True, alpha=0.3, color='r', bins=100, label='sample size=5')

for i in range(1000):
    sample = np.random.choice(norm_rvs, size=50, replace=False)
    mean_array.append(np.mean(sample))
plt.hist(mean_array, density=True, alpha=0.3, color='g', bins=100, label='sample size=50')

plt.gca().axes.set_xlim(-60, 60)
plt.legend(loc='best')
plt.show()