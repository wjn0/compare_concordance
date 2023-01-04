import numpy as np

import scipy as sp
import scipy.stats

from compare_concordance import estimate_concordance


def compare_concordance_with_bootstrap(
    event_time, event_indicator, score_x, score_y, num_samples=1000, seed=None
):
    if seed is not None:
        np.random.seed(seed)
    concordance_x = estimate_concordance(event_time, event_indicator, score_x)
    concordance_y = estimate_concordance(event_time, event_indicator, score_y)
    diff = concordance_x - concordance_y
    samples = []
    for _ in range(num_samples):
        idx = np.random.choice(len(event_time), size=len(event_time), replace=True)
        concordance_x_bootstrap = estimate_concordance(
            event_time[idx], event_indicator[idx], score_x[idx]
        )
        concordance_y_bootstrap = estimate_concordance(
            event_time[idx], event_indicator[idx], score_y[idx]
        )
        samples.append(concordance_x_bootstrap - concordance_y_bootstrap)
    std = np.sqrt(np.var(samples))
    zscore = diff / std
    pval = 1.0 - sp.stats.norm.cdf(np.abs(zscore))

    return diff, zscore, pval
