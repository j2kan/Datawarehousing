import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

salaryall = pd.read_excel('salary2015.xlsx')
salary_academics = salaryall[salaryall.position.isin(['Professor','Lecturer','Associate Professor','Assistant Professor'])]

#plot a scatter plot
plt.figure(1)
plt.scatter(salary_academics.salary_paid, salary_academics.taxable_benefits,  color='black')
plt.title("Salary of academicians")
plt.xlabel("salary_paid")
plt.ylabel("taxable_benefits")
plt.show()

# scatter plot with color based on a categorical variable
# create a grid first and then map the graph to this grid
position = ['Professor','Lecturer','Associate Professor','Assistant Professor']
fg = sns.FacetGrid(data=salary_academics, hue='position', hue_order=position)
fg.map(plt.scatter, 'salary_paid', 'taxable_benefits').add_legend()
plt.show()

# plot of categorical vs. numeric
sns.swarmplot(x=salary_academics.position, y=salary_academics.salary_paid, data=salary_academics)
plt.show()

sns.violinplot(x=salary_academics.position, y=salary_academics.salary_paid, data=salary_academics)
plt.show()

