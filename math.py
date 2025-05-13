import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 数式をLaTeX記法で記述
formula = r'$\sum_{i=1}^{n} a = n a$'

plt.figure(figsize=(4, 1))
plt.text(0.1, 0.5, formula, fontsize=24)
plt.axis('off')
plt.show()
