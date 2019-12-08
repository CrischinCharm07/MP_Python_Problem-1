import numpy as np
import matplotlib.pyplot as plt

n = list(range(0,100,1))
y = np.zeros(100)

for i in n:
    a = i
    
    while a>=10:
        a = a-10
        
    z = ((a**2)-7)
    y[i] = z
    
    
plt.stem(n,y, use_line_collection = True)