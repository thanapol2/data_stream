import matplotlib.pyplot as plt
import numpy as np

def update(prior, measurement):
    x,P = prior        # mean and variance of prior
    z,R = measurement  # mean and variance of measurement
    K = P/(P+R)  # Kalman gain
    x = x+K*(z-x)  # State update
    P = (1-K)*P  # Covariance Update
    return gaussian(x, P)

def predict(posterior, movement):
    x, P = posterior  # mean and variance of posterior
    dx, Q = movement  # mean and variance of movement
    x = x + dx
    P = P + Q
    return gaussian(x, P)

def plot_filter(xs, ys=None, dt=None, c='C0', label='Filter', var=None, **kwargs):
    if ys is None and dt is not None:
        ys = xs
        xs = np.arange(0, len(ys) * dt, dt)
    if ys is None:
        ys = xs
        xs = range(len(ys))

    lines = plt.plot(xs, ys, color=c, label=label, **kwargs)
    if var is None:
        return lines

    var = np.asarray(var)
    std = np.sqrt(var)
    std_top = ys+std
    std_btm = ys-std

    plt.plot(xs, ys+std, linestyle=':', color='k', lw=2)
    plt.plot(xs, ys-std, linestyle=':', color='k', lw=2)
    plt.fill_between(xs, std_btm, std_top,
                     facecolor='yellow', alpha=0.2)

    return lines

import kalman_playground.kf_book.kf_internal as kf_internal
from kalman_playground.kf_book.kf_internal import DogSimulation
from collections import namedtuple
from kalman_playground.kf_book import book_plots as book_plots

windows_size = 500
types = ["poisson"]
patterns = ["sq"]
LS = [1,5]
IS = [100]

gaussian = namedtuple('Gaussian', ['mean', 'var'])

process_var = 2.
sensor_var = 4.5
x = gaussian(0., 400.)
process_model = gaussian(1., process_var)
N = 25

dog = DogSimulation(x.mean, process_model.mean, sensor_var, process_var)
zs = [dog.move_and_sense() for _ in range(N)]

xs, priors = np.zeros((N, 2)), np.zeros((N, 2))
for i, z in enumerate(zs):
    prior = predict(x, process_model)
    x = update(prior, gaussian(z, sensor_var))
    priors[i] = prior

    xs[i] = x

book_plots.plot_measurements(zs)
book_plots.plot_filter(xs[:, 0], var=priors[:, 1])
book_plots.plot_predictions(priors[:, 0])
book_plots.show_legend()
kf_internal.print_variance(xs)
plt.show()
