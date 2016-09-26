import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read the csvs
anscombe_i = pd.read_csv('anscombe_i.csv')
anscombe_ii = pd.read_csv('anscombe_ii.csv')
anscombe_iii = pd.read_csv('anscombe_iii.csv')
anscombe_iv = pd.read_csv('anscombe_iv.csv')

print("Anscombe_i")
print(anscombe_i)
print()

#get the mean, count and std deviation of the datasets
print("Data Set I")
print(anscombe_i.describe()[1:3])
print("\nData Set II")
print(anscombe_ii.describe()[1:3])
print("\nData Set III")
print(anscombe_iii.describe()[1:3])
print("\nData Set IV")
print(anscombe_iv.describe()[1:3])

plt.figure(1)
plt.scatter(anscombe_i.x, anscombe_i.y,  color='black')
plt.title("anscombe_i")
plt.xlabel("x")
plt.ylabel("y")

plt.figure(2)
plt.scatter(anscombe_ii.x, anscombe_ii.y,  color='black')
plt.title("anscombe_ii")
plt.xlabel("x")
plt.ylabel("y")

plt.figure(3)
plt.scatter(anscombe_iii.x, anscombe_iii.y,  color='black')
plt.title("anscombe_iii")
plt.xlabel("x")
plt.ylabel("y")

plt.figure(4)
plt.scatter(anscombe_iv.x, anscombe_iv.y,  color='black')
plt.title("anscombe_iv")
plt.xlabel("x")
plt.ylabel("y")

plt.show()