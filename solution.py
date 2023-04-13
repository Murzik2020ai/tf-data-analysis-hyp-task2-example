import pandas as pd
import numpy as np


chat_id = 1226526788
from scipy import stats


def solution(x: np.array, y: np.array) -> bool:
    res = stats.cramervonmises_2samp(x, y)
    return res.pvalue < 0.08
    
