import numpy as np
import matplotlib.pyplot as plt

x = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 1000)

with plt.xkcd():
    plt.plot(x[:, 0], x[:, 1], '.')
    plt.title('Base Distribution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.yticks([])
    plt.xticks([])
    plt.savefig('npe/nf_base_example.png', dpi=300, bbox_inches='tight')
    plt.show()

# bannana distribution
a = 0.9 
b = 1.5
x1 = x[:, 0] * a
y = (x[:, 1]/a)+b*(x[:, 0]**2+a**2)

with plt.xkcd():
    plt.plot(x1, y, '.')
    plt.title('Transformed Distribution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.yticks([])
    plt.xticks([])
    plt.savefig('npe/nf_transformed_example.png', dpi=300, bbox_inches='tight')
    plt.show()