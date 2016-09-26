import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

salaryall = pd.read_excel('salary2015.xlsx')
salary_academics = salaryall[salaryall.position.isin(['Professor','Lecturer','Associate Professor','Assistant Professor'])]

#make histogram of salary
plt.figure(1)
plt.hist(salary_academics["salary_paid"])
plt.xlabel("salary_paid")
plt.show()

# basic box plot
plt.figure(2)
plt.boxplot(salary_academics.salary_paid)
plt.title("Salary paid")
plt.show()