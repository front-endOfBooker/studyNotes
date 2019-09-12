# -*- coding: utf-8 -*-
"""基金定投年化率.
numpy, Anaconda
$pip install numpy
"""
import numpy as np

def getProfile( profile_list, financial, n ):
    """parmas
    profile_list 定投金额list, type：list
    financial 最终受益 type: int/float
    n 定投周期(年份与周期比值, 如周期为半个月, n=24)
    """
    financial_list = profile_list + [financial]
    item_profile = np.irr(financial_list) + 1
    profile = pow(item_profile, n) - 1
    return profile

profile = getProfile([1000] * 3, -3111, 24)
print(profile)
