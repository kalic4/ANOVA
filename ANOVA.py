import pandas as pd 
from scipy import stats

# 数据准备
data = pd.DataFrame({'A': [1,2,3], 
                     'B': [2,4,6],
                     'C': [3,6,9]})

# 单因素方差分析
fvalue, pvalue = stats.f_oneway(data['A'], data['B'], data['C'])

print(f'f值:{fvalue}') 
print(f'p值:{pvalue}')

# 检验结果
if pvalue < 0.05:
   print('三组样本之间存在显著差异')
else:
   print('三组样本之间差异不显著')
