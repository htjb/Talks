import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = norm(0, 1)
y = norm(0, 1)

x_samples = x.rvs(1000)
dkl = np.mean(x.logpdf(x_samples) - y.logpdf(x_samples))

with plt.xkcd():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].hist(x_samples, bins=25, density=True)
    axes[0].hist(y.rvs(1000), bins=25, density=True, alpha=0.5)
    axes[0].set_title(f'DKL = {dkl:.2f}')

    y = norm(1, 1)
    axes[1].hist(x_samples, bins=25, density=True)
    axes[1].hist(y.rvs(1000), bins=25, density=True, alpha=0.5)

    dkl = np.mean(x.logpdf(x_samples) - y.logpdf(x_samples))
    axes[1].set_title(f'DKL = {dkl:.2f}')


    y = norm(5, 1)
    axes[2].hist(x_samples, bins=25, density=True)
    axes[2].hist(y.rvs(1000), bins=25, density=True, alpha=0.5)

    dkl = np.mean(x.logpdf(x_samples) - y.logpdf(x_samples))
    axes[2].set_title(f'DKL = {dkl:.2f}')

    for i in range(len(axes)):
        axes[i].set_xlabel('x')
        axes[i].set_ylabel('Density')
        axes[i].set_xticks([])
        axes[i].set_yticks([])

plt.savefig('npe/dkl.png', dpi=300, bbox_inches='tight')
plt.show()
