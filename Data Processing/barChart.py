'''
Using Seaborn, create a bar chart to visualize the distribution of a categorical variable in your dataset.
'''
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd

# Step 2 - load the dataset
titanic_data = sns.load_dataset('titanic')
print(titanic_data.head(10))
print(titanic_data.info())

# Create a bar plot
sns.barplot(x='sex', y='survived', data=titanic_data)
plt.show()

# Visualize missing values using msno.matrix
msno.matrix(titanic_data)

missing_data = titanic_data.isnull().sum()
print(missing_data)
