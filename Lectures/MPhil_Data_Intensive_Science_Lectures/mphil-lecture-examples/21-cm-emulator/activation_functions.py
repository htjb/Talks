import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(2):
        axes[1, i].set_xlabel('x')
        axes[i, 0].set_ylabel('y')
        for j in range(2):
            axes[i, j].axvline(0, color='black', lw=0.5, ls='--')
            axes[i, j].axhline(0, color='black', lw=0.5, ls='--')

    x = np.linspace(-10, 10, 100)
    y = np.tanh(x)
    
    axes[0, 0].plot(x, y)
    axes[0, 0].set_title('Tanh')

    y = 1 / (1 + np.exp(-x))
    axes[1, 0].plot(x, y)
    axes[1, 0].set_title('Sigmoid')

    y = np.maximum(0, x)
    axes[0, 1].plot(x, y)
    axes[0, 1].set_title('ReLU')

    axes[1, 1].plot(x, x)
    axes[1, 1].set_title('Linear')

    plt.tight_layout()
    plt.savefig('21-cm-emulator/activation_functions.png', dpi=300, bbox_inches='tight')
    plt.show()