import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    s = 0
    n = len(x)
    for i in range(n):
        s = s + (x[i])**2
    Chi1 = chi2.ppf(1-alpha*0.5, 2*n)
    Chi2 = chi2.ppf(alpha*0.5, 2*n)
    l = s/(42*Chi1)
    r = s/(42*Chi2)
    
    return np.sqrt(l), \
           np.sqrt(r)
