import numpy as np
import matplotlib.pyplot as plt


def refresh(x0, x1):
    x = np.linspace(x0 * np.pi, x1 * np.pi, 512, endpoint=True)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y0 = np.hstack((y1, y2))
    min_y = min(y0)
    max_y = max(y0)
    plt.plot(x, y1, label="sin line")
    plt.plot(x, y2, label='cosin line')
    plt.ylim((min_y, max_y))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    refresh(0, 2)
