import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

salaryall = pd.read_excel('salary2015.xlsx')
print("Total number of employees at UW: ", len(salaryall))

#getting rows of only academicians
salary_academics = salaryall[salaryall.position.isin(['Professor','Lecturer','Associate Professor','Assistant Professor'])]
print("Total number of academicians at UW: ", len(salary_academics))
print(salary_academics[0:10])

# PIE CHART
# The slices will be ordered and plotted counter-clockwise.
count = salary_academics.position.value_counts()
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
labels = count.index.values
values = count.values
print(count)

plt.pie(values, labels=labels, colors=colors, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()

# BAR CHART
sns.countplot(salary_academics.position, data=salary_academics)
plt.show()

