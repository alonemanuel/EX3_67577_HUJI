import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import special

IMAGE_DIR = '..\\..\\..\\Images\\'

MEAN0 = 4
MEAN1 = 6
VAR = 1
PROB = 0.5


def get_wtag(mu0, mu1, var):
    return (var ** (-1)) * (mu1 - mu0)


def get_b(mu0, mu1, var, p0, p1):
    return ((-0.5) * (mu1 - mu0) * (var ** (-1)) * (mu1 - mu0)) + np.log(p1 /
                                                                         p0)


def get_w(mu0, mu1, var, p0, p1):
    wtag = get_wtag(mu0, mu1, var)
    b = get_b(mu0, mu1, var, p0, p1)
    return np.append(wtag, b)


def get_x_axis(mu0, mu1, var):
    spacing, spread = 100, 3
    start = min(mu0 - spread * var, mu1 - spread * var)
    end = max(mu0 + spread * var, mu1 + spread * var)
    return np.linspace(start, end, spacing)


def h_of(xtag, w):
    x = np.append(xtag, 1)
    x_prod_w = np.inner(x, w)
    return special.expit(x_prod_w)


def plot_h(mu0, mu1, var, p0, p1):
    logger('Plotting h')
    w = get_w(mu0, mu1, var, p0, p1)
    # x = get_x_axis(mu0, mu1, var) # TODO: Fix this
    x = np.linspace(-5, 5, 100)
    fig = plt.figure()
    fig.suptitle('h(x) as a Function of x')
    plt.xlabel('x = R')
    plt.ylabel('y = R')
    decor_h = lambda x: h_of(x, w)
    plt.plot(x, np.vectorize(decor_h)(x), label='h(x)')
    plt.legend()
    plt.savefig(IMAGE_DIR + 'q5_b_ii')

def plot_cdf_of_h(mu0, mu1, var, p0, p1):
    logger("Plotting cdf of h")
    w = get_w(mu0, mu1, var, p0, p1)
    x = np.linspace(0,1,1000)
    x0=np.random.normal(mu0, var, 1000)
    x1=np.random.normal(mu1, var, 1000)
    decor_h = lambda x: h_of(x, w)
    fig = plt.figure()
    fig.suptitle('CDFs of h(x)')
    plt.xlabel('x = R')
    plt.ylabel('y = R')
    plot_cdf(mu0, var, x, np.vectorize(decor_h)(x), 'CDF 1')
    plot_cdf(mu1, var, x, np.vectorize(decor_h)(x), 'CDF 2')
    plt.legend()
    plt.savefig(IMAGE_DIR + 'q5_b_iii')

def plot_gaussians(mu0, mu1, var):
    logger('Plotting gaussians')
    x = get_x_axis(mu0, mu1, var)
    fig, axarr = plt.subplots(nrows=2)
    fig.suptitle('PDF and CDF of Two Gaussians')
    plt.xlabel('x = R')
    plt.ylabel('y = R')
    plot_pdfs(mu0, mu1, var, axarr[0], x)
    plot_cdfs(mu0, mu1, var, axarr[1], x)
    plt.savefig(IMAGE_DIR + 'q5_b_i')


def plot_pdfs(mu0, mu1, var, axes, x):
    logger('Plotting PDFs')
    axes.plot(x, norm.pdf(x, mu0, var), label='PDF 1')
    axes.plot(x, norm.pdf(x, mu1, var), label='PDF 2')
    axes.legend()

def plot_cdf(mu, var, x, h_x, label):
    plt.plot(x, norm.cdf(h_x, mu, var), label=label)


def plot_cdfs(mu0, mu1, var, axes, x):
    logger('Plotting CDFs')
    axes.plot(x, norm.cdf(x, mu0, var), label='CDF 1')
    axes.plot(x, norm.cdf(x, mu1, var), label='CDF 2')
    axes.legend()


def logger(*args):
    print('Log: ', end='')
    for arg in args:
        print(arg, end='')
    print()


def main():
    plot_gaussians(MEAN0, MEAN1, VAR)
    plot_h(MEAN0, MEAN1, VAR, PROB, PROB)
    plot_cdf_of_h(MEAN0, MEAN1, VAR, PROB, PROB)

main()
