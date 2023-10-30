'''
Given a dataset, filter the rows to include only those where a specific column meets a certain condition using Pandas.
'''
import pandas as pd
from sklearn import datasets
# Load the Iris dataset from scikit-learn
iris = datasets.load_iris()
#print(print(iris.DESCR))
# Create a Pandas DataFrame from the Iris data
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
#sprint(iris_df)
# Define your condition
# For example, let's say you want to filter rows where the 'sepal length (cm)' is greater than 5.0
condition = iris_df['sepal length (cm)'] > 5.0
# Apply the condition to filter rows
filtered_iris_df = iris_df[condition]

# Display the filtered DataFrame
print(filtered_iris_df)