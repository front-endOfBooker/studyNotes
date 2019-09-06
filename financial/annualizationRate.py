import numpy as np
# 环境
# 1. python
# 2. numpy, Anaconda

# 基金定投年化率
# params number-定投金额, 最终受益
profile = np.irr([1000, 1000, 1000, -3111])
print (profile)
print(pow(profile+1, 24) - 1)