import matplotlib.pyplot as plt
import numpy as np

def update(prior_mean,prior_variance, measurement_mean,measurement_variance):
    x = prior_mean
    P = prior_variance        # mean and variance of prior
    z= measurement_mean
    R = measurement_variance# mean and variance of measurement
    K = P/(P+R)  # Kalman gain
    x = x+K*(z-x)  # State update
    P = (1-K)*P  # Covariance Update
    return x, P

def predict(posterior_mean,posterior_variance, movement_mean,movement_variance):
    x = posterior_mean
    P = posterior_variance  # mean and variance of posterior
    dx = movement_mean
    Q = movement_variance  # mean and variance of movement
    x = x + dx  #State Extrapolation
    P = P + Q  #Covariance Extrapolation
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

