import matplotlib.pyplot as plt
import numpy as np

def update(prior_mean,prior_variance, measurement_mean,measurement_variance):
    x,P = prior        # mean and variance of prior
    z,R = measurement  # mean and variance of measurement
    K = P/(P+R)  # Kalman gain
    x = x+K*(z-x)  # State update
    P = (1-K)*P  # Covariance Update
    return x, P

def predict(posterior, movement):
    x, P = posterior  # mean and variance of posterior
    dx, Q = movement  # mean and variance of movement
    x = x + dx
    P = P + Q
    return x, P

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

