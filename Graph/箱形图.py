import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [418,421,421,422,425,427,431,434,437,439,446,447,448,453,454,463,465]

df = pd.DataFrame(data)
df.plot.box(title="boxplot")
plt.grid(linestyle='--',alpha=0.3)
plt.show()