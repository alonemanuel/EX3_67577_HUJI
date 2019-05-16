import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

IMAGE_DIR = '..\\..\\..\\Images\\'

MEAN0 = 4
MEAN1 = 6
VAR = 1
PROB = 0.5


def get_w(mean0, mean1, var, prob):
    pass


def plot_gaussians(mu0, var0, mu1, var1):
    log('Plotting gaussians')
    spacing, spread = 100, 3
    start = min(mu0 - spread * var0, mu1 - spread * var1)
    end = max(mu0 + spread * var0, mu1 + spread * var1)
    fig, axarr = plt.subplots(nrows=2)
    fig.suptitle('PDF and CDF of Two Gaussians')
    x = np.linspace(start, end, spacing)
    plt.xlabel('x = R')
    plt.ylabel('y = R')
    plot_pdfs(mu0, var0, mu1, var1, axarr[0], x)
    plot_cdfs(mu0, var0, mu1, var1, axarr[1], x)
    plt.savefig(IMAGE_DIR+'q5_b_i')

def plot_pdfs(mu0, var0, mu1, var1, axes, x):
    log('Plotting PDFs')
    axes.plot(x, norm.pdf(x, mu0, var0), label='PDF 1')
    axes.plot(x, norm.pdf(x, mu1, var1), label='PDF 2')
    axes.legend()


def plot_cdfs(mu0, var0, mu1, var1, axes, x):
    log('Plotting CDFs')
    axes.plot(x, norm.cdf(x, mu0, var0), label='CDF 1')
    axes.plot(x, norm.cdf(x, mu1, var1), label='CDF 2')
    axes.legend()

def log(*args):
    print('Log: ', end='')
    for arg in args:
        print(arg)

def main():
    plot_gaussians(MEAN0, VAR, MEAN1, VAR)


main()
