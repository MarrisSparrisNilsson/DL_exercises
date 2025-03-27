import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Plot(object):

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.ion()

    def draw_line(self, interval, weights):
        xpoints = np.linspace(interval[0], interval[1], 10)
        # draw line based on weights (w1, w2, b)
        # y = -(w1/w2)x -b
        # NOTE: we add 0.0001 to avoid division by 0
        ypoints = -(weights[0] / (weights[1] + 0.0001)) * xpoints - weights[2] / (weights[1] + 0.0001)
        self.ax.plot(xpoints, ypoints.T, "-")

    def plot_data(self, data, weights=None):
        self.ax.clear()
        self.draw_scatter(data, 1, -1)

        if weights is not None:
            self.draw_line((-8, 12), weights)
        self.ax.axis("equal")
        self.fig.canvas.draw()

    def draw_scatter(self, data, pos, neg):
        pos_idx = data[:, 3] == pos
        neg_idx = data[:, 3] == neg
        self.ax.plot(data[:, 0][neg_idx].T, data[:, 1][neg_idx].T, "_")
        self.ax.plot(data[:, 0][pos_idx].T, data[:, 1][pos_idx].T, "+")

    def show(self):
        self.fig.canvas.draw()


class Xor(object):

    def __init__(self):
        self.xor = np.matrix([[0, 0, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0]])

    def plot_xor(self, weights1=None, weights2=None):
        interval = (0, 1)
        plot = Plot()
        plot.draw_scatter(self.xor, 1, 0)
        if weights1 is not None:
            plot.draw_line(interval, weights1)
        if weights2 is not None:
            plot.draw_line(interval, weights2)
        plot.show()

    def _calculate_hidden(self, inputs, weights):
        tmp = np.sign(inputs * weights)
        tmp[tmp <= 0] = 0
        return tmp

    def xor_truthtable(self, weights1, weights2):
        df = pd.DataFrame(self.xor, columns=["$x_0$", "$x_1$", "bias", "$y$"])
        del df["bias"]
        df["$h_1$"] = self._calculate_hidden(self.xor[:, 0:3], weights1)
        df["$h_2$"] = self._calculate_hidden(self.xor[:, 0:3], weights2)
        return df


def generate_data():
    # define mean and covariance matrix of bivariate gaussians to sample from
    # for positive and negative samples
    mean1 = [-3.5, 3.5]
    mean2 = [3.5, -3.5]
    cov = [[10, 0], [0, 2]]
    # ensure same results
    np.random.seed(1206)
    # points for negative samples
    x, y = np.random.multivariate_normal(mean1, cov, 50).T
    # points for positive samples
    x2, y2 = np.random.multivariate_normal(mean2, cov, 50).T
    min_ones, ones = np.ones(len(x)) * -1, np.ones(len(x))
    # create matrix with columns: x, y, bias extension, target class
    pos = np.matrix([x, y, ones, min_ones])
    neg = np.matrix([x2, y2, ones, ones])
    # combine positive and negative samples and randomize
    comb = np.concatenate([pos, neg], axis=1).T
    np.random.shuffle(comb)
    return comb
